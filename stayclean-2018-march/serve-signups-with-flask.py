#!/usr/bin/env python

import subprocess
import praw
from hashlib import sha1
from flask import Flask
from flask import Response
from flask import request
from cStringIO import StringIO
from base64 import b64encode
from base64 import b64decode
from ConfigParser import ConfigParser
import OAuth2Util
import os
import markdown
import bleach
# encoding=utf8
import sys
from participantCollection import ParticipantCollection

reload(sys)
sys.setdefaultencoding('utf8')


# Edit Me!
# Each day after you post a signup post, copy its 6-character ID to this array.
signupPageSubmissionIds = [ '7zrrj1', '7zxkpq', '8055hn', '80ddrf', '80nbm1', '80waq3' ]
flaskport = 8993

app = Flask(__name__)
app.debug = True
commentHashesAndComments = {}


def loginAndReturnRedditSession():
    config = ConfigParser()
    config.read("../reddit-password-credentials.cfg")
    user = config.get("Reddit", "user")
    password = config.get("Reddit", "password")
    # TODO:  password auth is going away, and we will soon need to do oauth.
    redditSession = praw.Reddit(user_agent='Test Script by /u/foobarbazblarg')
    redditSession.login(user, password, disable_warning=True)
    # submissions = redditSession.get_subreddit('pornfree').get_hot(limit=5)
    # print [str(x) for x in submissions]
    return redditSession


def loginOAuthAndReturnRedditSession():
    redditSession = praw.Reddit(user_agent='Test Script by /u/foobarbazblarg')
    # New version of praw does not require explicit use of the OAuth2Util object.  Presumably because reddit now REQUIRES oauth.
    # o = OAuth2Util.OAuth2Util(redditSession, print_log=True, configfile="../reddit-oauth-credentials.cfg")
    # TODO:  Testing comment of refresh.  We authenticate fresh every time, so presumably no need to do o.refresh().
    # o.refresh(force=True)
    return redditSession


def getSubmissionsForRedditSession(redditSession):
    # submissions = [redditSession.get_submission(submission_id=submissionId) for submissionId in signupPageSubmissionIds]
    submissions = [redditSession.submission(id=submissionId) for submissionId in signupPageSubmissionIds]
    for submission in submissions:
        submission.comments.replace_more(limit=None)
        # submission.replace_more_comments(limit=None, threshold=0)
    return submissions


def getCommentsForSubmissions(submissions):
    comments = []
    for submission in submissions:
        commentForest = submission.comments
        comments += [comment for comment in commentForest.list() if comment.__class__ == praw.models.Comment]
    return comments


def retireCommentHash(commentHash):
    with open("retiredcommenthashes.txt", "a") as commentHashFile:
        commentHashFile.write(commentHash + '\n')


def retiredCommentHashes():
    with open("retiredcommenthashes.txt", "r") as commentHashFile:
        # return commentHashFile.readlines()
        return commentHashFile.read().splitlines()


@app.route('/moderatesignups.html')
def moderatesignups():
    global commentHashesAndComments
    commentHashesAndComments = {}
    stringio = StringIO()
    stringio.write('<html>\n<head>\n</head>\n\n')

    # redditSession = loginAndReturnRedditSession()
    redditSession = loginOAuthAndReturnRedditSession()
    submissions = getSubmissionsForRedditSession(redditSession)
    flat_comments = getCommentsForSubmissions(submissions)
    retiredHashes = retiredCommentHashes()
    i = 1
    stringio.write('<iframe name="invisibleiframe" style="display:none;"></iframe>\n')
    stringio.write("<h3>")
    stringio.write(os.getcwd())
    stringio.write("<br>\n")
    for submission in submissions:
        stringio.write(submission.title)
        stringio.write("<br>\n")
    stringio.write("</h3>\n\n")
    stringio.write('<form action="copydisplayduringsignuptoclipboard.html" method="post" target="invisibleiframe">')
    stringio.write('<input type="submit" value="Copy display-during-signup.py stdout to clipboard">')
    stringio.write('</form>')
    for comment in flat_comments:
        # print comment.is_root
        # print comment.score
        i += 1
        commentHash = sha1()
        commentHash.update(comment.fullname)
        commentHash.update(comment.body.encode('utf-8'))
        commentHash = commentHash.hexdigest()
        if commentHash not in retiredHashes:
            commentHashesAndComments[commentHash] = comment
            authorName = str(comment.author)  # can be None if author was deleted.  So check for that and skip if it's None.
            stringio.write("<hr>\n")
            stringio.write('<font color="blue"><b>')
            stringio.write(authorName)  # can be None if author was deleted.  So check for that and skip if it's None.
            stringio.write('</b></font><br>')
            if ParticipantCollection().hasParticipantNamed(authorName):
                stringio.write(' <small><font color="green">(member)</font></small>')
                # if ParticipantCollection().participantNamed(authorName).isStillIn:
                #    stringio.write(' <small><font color="green">(in)</font></small>')
                # else:
                #    stringio.write(' <small><font color="red">(out)</font></small>')
            else:
                stringio.write(' <small><font color="red">(not a member)</font></small>')
            stringio.write('<form action="takeaction.html" method="post" target="invisibleiframe">')
            stringio.write('<input type="submit" name="actiontotake" value="Signup" style="color:white;background-color:green">')
            # stringio.write('<input type="submit" name="actiontotake" value="Signup and checkin">')
            # stringio.write('<input type="submit" name="actiontotake" value="Relapse">')
            # stringio.write('<input type="submit" name="actiontotake" value="Reinstate">')
            stringio.write('<input type="submit" name="actiontotake" value="Skip comment">')
            stringio.write('<input type="submit" name="actiontotake" value="Skip comment and don\'t upvote">')
            stringio.write('<input type="hidden" name="username" value="' + b64encode(authorName) + '">')
            stringio.write('<input type="hidden" name="commenthash" value="' + commentHash + '">')
            # stringio.write('<input type="hidden" name="commentpermalink" value="' + comment.permalink + '">')
            stringio.write('</form>')

            stringio.write(bleach.clean(markdown.markdown(comment.body.encode('utf-8')), tags=['p']))
            stringio.write("\n<br><br>\n\n")

    stringio.write('</html>')
    pageString = stringio.getvalue()
    stringio.close()
    return Response(pageString, mimetype='text/html')


@app.route('/takeaction.html', methods=["POST"])
def takeaction():
    username = b64decode(request.form["username"])
    commentHash = str(request.form["commenthash"])
    # commentPermalink = request.form["commentpermalink"]
    actionToTake = request.form["actiontotake"]
    # print commentHashesAndComments
    comment = commentHashesAndComments[commentHash]
    # print "comment:  " + str(comment)
    if actionToTake == 'Signup':
        print "signup - " + username
        subprocess.call(['./signup.py', username])
        comment.upvote()
        retireCommentHash(commentHash)
    # if actionToTake == 'Signup and checkin':
    #     print "signup and checkin - " + username
    #     subprocess.call(['./signup-and-checkin.sh', username])
    #     comment.upvote()
    #     retireCommentHash(commentHash)
    # elif actionToTake == 'Relapse':
    #     print "relapse - " + username
    #     subprocess.call(['./relapse.py', username])
    #     comment.upvote()
    #     retireCommentHash(commentHash)
    # elif actionToTake == 'Reinstate':
    #     print "reinstate - " + username
    #     subprocess.call(['./reinstate.py', username])
    #     comment.upvote()
    #     retireCommentHash(commentHash)
    elif actionToTake == 'Skip comment':
        print "Skip comment - " + username
        comment.upvote()
        retireCommentHash(commentHash)
    elif actionToTake == "Skip comment and don't upvote":
        print "Skip comment and don't upvote - " + username
        retireCommentHash(commentHash)
    return Response("hello", mimetype='text/html')


@app.route('/copydisplayduringsignuptoclipboard.html', methods=["POST"])
def copydisplayduringsignuptoclipboard():
    print "TODO: Copy display to clipboard"
    subprocess.call(['./display-during-signup.py'])
    return Response("hello", mimetype='text/html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=flaskport)

