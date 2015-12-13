#!/usr/bin/python

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



# Edit me!
challengePageSubmissionId = '(insertpageidhere)'
flaskport = 8891

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
    o = OAuth2Util.OAuth2Util(redditSession, print_log = True, configfile="../reddit-oauth-credentials.cfg")
    o.refresh(force=True)
    return redditSession

def getSubmissionForRedditSession(redditSession):
    submission = redditSession.get_submission(submission_id=challengePageSubmissionId)
    submission.replace_more_comments(limit=None, threshold=0)
    return submission

def getCommentsForSubmission(submission):
    return praw.helpers.flatten_tree(submission.comments)

def retireCommentHash(commentHash):
    with open("retiredcommenthashes.txt", "a") as commentHashFile:
        commentHashFile.write(commentHash + '\n')

def retiredCommentHashes():
    with open("retiredcommenthashes.txt", "r") as commentHashFile:
        # return commentHashFile.readlines()
        return commentHashFile.read().splitlines()

@app.route('/moderatechallenge.html')
def moderatechallenge():
    global commentHashesAndComments
    commentHashesAndComments = {}
    stringio = StringIO()
    stringio.write('<html>\n<head>\n</head>\n\n')

    # redditSession = loginAndReturnRedditSession()
    redditSession = loginOAuthAndReturnRedditSession()
    submission = getSubmissionForRedditSession(redditSession)
    flat_comments = getCommentsForSubmission(submission)
    retiredHashes = retiredCommentHashes()
    i = 1
    stringio.write('<iframe name="invisibleiframe" style="display:none;"></iframe>\n')
    stringio.write("<h3>")
    stringio.write(os.getcwd())
    stringio.write("<br>\n")
    stringio.write(submission.title)
    stringio.write("</h3>\n\n")
    stringio.write('<form action="copydisplaytoclipboard.html" method="post" target="invisibleiframe">')
    stringio.write('<input type="submit" value="Copy display.py stdout to clipboard">')
    stringio.write('</form>')
    for comment in flat_comments:
        # print comment.is_root
        # print comment.score
        i += 1
        commentHash = sha1()
        commentHash.update(comment.permalink)
        commentHash.update(comment.body.encode('utf-8'))
        commentHash = commentHash.hexdigest()
        if commentHash not in retiredHashes:
            commentHashesAndComments[commentHash] = comment
            stringio.write("<hr>\n")
            stringio.write('<font color="blue"><b>')
            stringio.write(str(comment.author))  # can be None if author was deleted.  So check for that and skip if it's None.
            stringio.write('</b></font>')

            stringio.write('<form action="takeaction.html" method="post" target="invisibleiframe">')
            stringio.write('<input type="submit" name="actiontotake" value="Checkin">')
            stringio.write('<input type="submit" name="actiontotake" value="Signup and checkin">')
            stringio.write('<input type="submit" name="actiontotake" value="Relapse">')
            stringio.write('<input type="submit" name="actiontotake" value="Reinstate">')
            stringio.write('<input type="submit" name="actiontotake" value="Skip comment">')
            stringio.write('<input type="submit" name="actiontotake" value="Skip comment and don\'t upvote">')
            stringio.write('<input type="hidden" name="username" value="' + b64encode(str(comment.author)) + '">')
            stringio.write('<input type="hidden" name="commenthash" value="' + commentHash + '">')
            stringio.write('<input type="hidden" name="commentpermalink" value="' + comment.permalink + '">')
            stringio.write('</form>')

            stringio.write(comment.body.encode('utf-8'))
            stringio.write("\n<br><br>\n\n")

    stringio.write('</html>')
    pageString = stringio.getvalue()
    stringio.close()
    return Response(pageString, mimetype='text/html')

@app.route('/takeaction.html', methods=["POST"])
def takeaction():
    username = b64decode(request.form["username"])
    commentHash = str(request.form["commenthash"])
    commentPermalink = request.form["commentpermalink"]
    actionToTake = request.form["actiontotake"]
    # print commentHashesAndComments
    comment = commentHashesAndComments[commentHash]
    # print "comment:  " + str(comment)
    if actionToTake == 'Checkin':
        print "checkin - " + username
        subprocess.call(['./checkin.py', username])
        comment.upvote()
        retireCommentHash(commentHash)
    if actionToTake == 'Signup and checkin':
        print "signup and checkin - " + username
        subprocess.call(['./signup-and-checkin.sh', username])
        comment.upvote()
        retireCommentHash(commentHash)
    elif actionToTake == 'Relapse':
        print "relapse - " + username
        subprocess.call(['./relapse.py', username])
        comment.upvote()
        retireCommentHash(commentHash)
    elif actionToTake == 'Reinstate':
        print "reinstate - " + username
        subprocess.call(['./reinstate.py', username])
        comment.upvote()
        retireCommentHash(commentHash)
    elif actionToTake == 'Skip comment':
        print "Skip comment - " + username
        comment.upvote()
        retireCommentHash(commentHash)
    elif actionToTake == "Skip comment and don't upvote":
        print "Skip comment and don't upvote - " + username
        retireCommentHash(commentHash)
    return Response("hello", mimetype='text/html')



@app.route('/copydisplaytoclipboard.html', methods=["POST"])
def copydisplaytoclipboard():
    print "TODO: Copy display to clipboard"
    subprocess.call(['./display.py'])
    return Response("hello", mimetype='text/html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=flaskport)

