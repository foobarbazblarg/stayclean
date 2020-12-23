#!/usr/bin/env python

import subprocess
import datetime
import praw
import pyperclip
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


# Edit me!
challengePageSubmissionId = 'egfht9'
flaskport = 8997
readAllCommentsWhichCanBeSlower = False

sorryTooLateToSignUpReplyText = "Sorry, but the late signup grace period is over, so you can't officially join this challenge.  But feel free to follow along anyway, and comment all you want."
reinstatedReplyText = "OK, I've reinstated you.  You should start showing up on the list again starting tomorrow."

app = Flask(__name__)
app.debug = True
commentHashesAndComments = {}
submission = None


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


def getSubmissionForRedditSession(redditSession):
    # submission = redditSession.get_submission(submission_id=challengePageSubmissionId)
    submission = redditSession.submission(id=challengePageSubmissionId)
    if readAllCommentsWhichCanBeSlower:
        submission.comments.replace_more(limit=None)
        # submission.replace_more_comments(limit=None, threshold=0)
    return submission


def getCommentsForSubmission(submission):
    # return [comment for comment in praw.helpers.flatten_tree(submission.comments) if comment.__class__ == praw.models.Comment]
    commentForest = submission.comments
    # commentForest.replace_more(limit=None, threshold=0)
    return [comment for comment in commentForest.list() if comment.__class__ == praw.models.Comment]


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
    global submission
    currentDayOfMonthIndex = datetime.date.today().day
    currentMonthIndex = datetime.date.today().month
    lateCheckinGracePeriodIsInEffect = currentDayOfMonthIndex <= 14 and currentMonthIndex == 1
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
    stringio.write('<input type="submit" name="actiontotake" value="Copy display.py stdout to clipboard">')
    stringio.write('<input type="submit" name="actiontotake" value="Automatically post display.py stdout">')
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
            participant = ParticipantCollection().participantNamed(authorName)
            stringio.write("<hr>\n")
            stringio.write('<font color="blue"><b>')
            stringio.write(authorName)
            stringio.write('</b></font><br>')
            if ParticipantCollection().hasParticipantNamed(authorName):
                stringio.write(' <small><font color="green">(member)</font></small>')
                if participant.isStillIn:
                    stringio.write(' <small><font color="green">(still in)</font></small>')
                else:
                    stringio.write(' <small><font color="red">(out)</font></small>')
                if participant.hasCheckedIn:
                    stringio.write(' <small><font color="green">(checked in)</font></small>')
                else:
                    stringio.write(' <small><font color="orange">(not checked in)</font></small>')
                if participant.hasRelapsed:
                    stringio.write(' <small><font color="red">(relapsed)</font></small>')
                else:
                    stringio.write(' <small><font color="green">(not relapsed)</font></small>')
            else:
                stringio.write(' <small><font color="red">(not a member)</font></small>')
            stringio.write('<form action="takeaction.html" method="post" target="invisibleiframe">')

            # stringio.write('<input type="submit" name="actiontotake" value="Checkin" style="color:white;background-color:green">')
            # stringio.write('<input type="submit" name="actiontotake" value="Signup and checkin">')

            if lateCheckinGracePeriodIsInEffect:
                stringio.write('<input type="submit" name="actiontotake" value="Checkin">')
                stringio.write('<input type="submit" name="actiontotake" value="Signup and checkin" style="color:white;background-color:green">')
            else:
                stringio.write('<input type="submit" name="actiontotake" value="Checkin" style="color:white;background-color:green">')
                stringio.write('<input type="submit" name="actiontotake" value="Signup and checkin">')

            stringio.write('<input type="submit" name="actiontotake" value="Relapse" style="color:white;background-color:red">')
            stringio.write('<input type="submit" name="actiontotake" value="Reinstate with automatic comment">')
            stringio.write('<input type="submit" name="actiontotake" value="Reply with sorry-too-late comment">')
            stringio.write('<input type="submit" name="actiontotake" value="Skip comment">')
            stringio.write('<input type="submit" name="actiontotake" value="Skip comment and don\'t upvote">')
            stringio.write('<input type="hidden" name="username" value="' + b64encode(authorName) + '">')
            stringio.write('<input type="hidden" name="bodyencodedformlcorpus" value="' + b64encode(comment.body.encode('utf-8')) + '">')
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
    bodyEncodedForMLCorpus = str(request.form["bodyencodedformlcorpus"])
    actionToTake = request.form["actiontotake"]
    # print commentHashesAndComments
    comment = commentHashesAndComments[commentHash]
    # print "comment:  " + str(comment)
    if actionToTake == 'Checkin':
        print "checkin - " + username
        subprocess.call(['./checkin.py', username])
        comment.upvote()
        retireCommentHash(commentHash)
        recordMLCorpusCheckin(bodyEncodedForMLCorpus)
    if actionToTake == 'Signup and checkin':
        print "signup and checkin - " + username
        subprocess.call(['./signup-and-checkin.sh', username])
        comment.upvote()
        retireCommentHash(commentHash)
        recordMLCorpusSignupAndCheckin(bodyEncodedForMLCorpus)
    elif actionToTake == 'Relapse':
        print "relapse - " + username
        subprocess.call(['./relapse.py', username])
        comment.upvote()
        retireCommentHash(commentHash)
        recordMLCorpusRelapse(bodyEncodedForMLCorpus)
    elif actionToTake == 'Reinstate with automatic comment':
        print "reinstate - " + username
        subprocess.call(['./reinstate.py', username])
        comment.reply(reinstatedReplyText)
        comment.upvote()
        retireCommentHash(commentHash)
        recordMLCorpusReinstate(bodyEncodedForMLCorpus)
    elif actionToTake == 'Reply with sorry-too-late comment':
        print "reply with sorry-too-late comment - " + username
        comment.reply(sorryTooLateToSignUpReplyText)
        comment.upvote()
        retireCommentHash(commentHash)
        recordMLCorpusTooLate(bodyEncodedForMLCorpus)
    elif actionToTake == 'Skip comment':
        print "Skip comment - " + username
        comment.upvote()
        retireCommentHash(commentHash)
        recordMLCorpusSkip(bodyEncodedForMLCorpus)
    elif actionToTake == "Skip comment and don't upvote":
        print "Skip comment and don't upvote - " + username
        retireCommentHash(commentHash)
        recordMLCorpusSkip(bodyEncodedForMLCorpus)
    return Response("hello", mimetype='text/html')


@app.route('/copydisplaytoclipboard.html', methods=["POST"])
def copydisplaytoclipboard():
    actionToTake = request.form["actiontotake"]
    if actionToTake == 'Copy display.py stdout to clipboard':
        subprocess.call(['./display.py'])
    if actionToTake == 'Automatically post display.py stdout':
        subprocess.call(['./display.py'])
        submissionText = pyperclip.paste()
        submission.edit(submissionText)
    return Response("hello", mimetype='text/html')

def recordMLCorpusCheckin(aString):
    with open("../new-ml-corpus-year-long-checkin.txt", "a") as f:
        f.write(aString)
        f.write("\n")

def recordMLCorpusSignupAndCheckin(aString):
    with open("../new-ml-corpus-year-long-signup-and-checkin.txt", "a") as f:
        f.write(aString)
        f.write("\n")

def recordMLCorpusRelapse(aString):
    with open("../new-ml-corpus-year-long-relapse.txt", "a") as f:
        f.write(aString)
        f.write("\n")

def recordMLCorpusReinstate(aString):
    with open("../new-ml-corpus-year-long-reinstate.txt", "a") as f:
        f.write(aString)
        f.write("\n")

def recordMLCorpusTooLate(aString):
    with open("../new-ml-corpus-year-long-too-late.txt", "a") as f:
        f.write(aString)
        f.write("\n")

def recordMLCorpusSkip(aString):
    with open("../new-ml-corpus-year-long-skip.txt", "a") as f:
        f.write(aString)
        f.write("\n")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=flaskport)

