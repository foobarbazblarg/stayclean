#!/usr/bin/env python3
import praw
from hashlib import sha1
from flask import Flask
from flask import Response
from cStringIO import StringIO
import OAuth2Util
import markdown
import bleach
# encoding=utf8
import sys
from typing import List

reload(sys)
sys.setdefaultencoding('utf8')


# Edit me!
activeCommentHashFiles = ['retiredcommenthashes.txt',
                          '../stayclean-2016/retiredcommenthashes.txt',
                          '../stayclean-2018-january/retiredcommenthashes.txt',
                          '../stayclean-2016-december/retiredcommenthashes.txt',
                          '../stayclean-2016-november/retiredcommenthashes.txt',
                          '../stayclean-2016-october/retiredcommenthashes.txt',
                          '../stayclean-2016-september/retiredcommenthashes.txt',
                          '../stayclean-2016-august/retiredcommenthashes.txt',
                          '../stayclean-2016-july/retiredcommenthashes.txt',
                          '../stayclean-2016-june/retiredcommenthashes.txt',
                          '../stayclean-2016-may/retiredcommenthashes.txt',
                          '../stayclean-2016-april/retiredcommenthashes.txt',
                          '../stayclean-2016-march/retiredcommenthashes.txt',
                          '../stayclean-2016-february/retiredcommenthashes.txt']
flaskport = 8800

app = Flask(__name__)
app.debug = True
# commentHashesAndComments = {}
submission = None

# TODO - typ hint
def loginOAuthAndReturnRedditSession() -> praw.Reddit:
    redditSession = praw.Reddit(user_agent='Test Script by /u/foobarbazblarg')
    OAuth2Util.OAuth2Util(redditSession, print_log=True, configfile="../reddit-oauth-credentials.cfg")
    # TODO:  Testing comment of refresh.  We authenticate fresh every time, so presumably no need to do o.refresh().
    # o = OAuth2Util.OAuth2Util(redditSession, print_log=True, configfile="../reddit-oauth-credentials.cfg")
    # o.refresh(force=True)
    return redditSession


# TODO - type hint
def getSubmissionForRedditSession(redditSession):
    submission = redditSession.get_submission(submission_id=challengePageSubmissionId)
    # submission.replace_more_comments(limit=None, threshold=0)
    return submission


def retiredCommentHashes():
    answer = []
    for filename in activeCommentHashFiles:
        with open(filename, "r") as commentHashFile:
            # return commentHashFile.readlines()
            answer += commentHashFile.read().splitlines()
    return answer


@app.route('/unread')
def unread():
    # global commentHashesAndComments
    global submission
    # commentHashesAndComments = {}
    stringio = StringIO()
    stringio.write('<html>\n<head>\n</head>\n\n')

    redditSession = loginOAuthAndReturnRedditSession()
    unreadMessages = redditSession.get_unread(limit=None)
    retiredHashes = retiredCommentHashes()
    i = 1
    stringio.write('<iframe name="invisibleiframe" style="display:none;"></iframe>\n')
    stringio.write("<h3>")
    stringio.write("my unread messages")
    stringio.write("</h3>\n\n")
    for unreadMessage in unreadMessages:
        i += 1
        commentHash = sha1()
        if unreadMessage.__class__ == praw.objects.Comment:
            # This next line takes 2 seconds.  It must need to do an HTTPS transaction to get the permalink.
            # Not much we can do about that, I guess.
            # print int(round(time.time() * 1000))
            commentHash.update(unreadMessage.permalink)
            # print int(round(time.time() * 1000))
        else:
            commentHash.update(str(unreadMessage.author))
        commentHash.update(unreadMessage.body.encode('utf-8'))
        commentHash = commentHash.hexdigest()
        if commentHash not in retiredHashes:
            # commentHashesAndComments[commentHash] = unreadMessage
            authorName = str(unreadMessage.author)  # can be None if author was deleted.  So check for that and skip if it's None.
            # participant = ParticipantCollection().participantNamed(authorName)
            stringio.write("<hr>\n")
            stringio.write('<font color="blue"><b>')
            stringio.write(authorName)
            stringio.write('</b></font><br>')
            if unreadMessage.__class__ == praw.objects.Comment:
                stringio.write('<small><font color="gray">' + bleach.clean(unreadMessage.submission.title) + '</font></small><br>')
            else:
                stringio.write('<b>' + bleach.clean(unreadMessage.subject) + '</b><br>')
            stringio.write(bleach.clean(markdown.markdown(unreadMessage.body.encode('utf-8')), tags=['p']))
            stringio.write("\n<br><br>\n\n")
    stringio.write('</html>')
    pageString = stringio.getvalue()
    stringio.close()
    return Response(pageString, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=flaskport)

