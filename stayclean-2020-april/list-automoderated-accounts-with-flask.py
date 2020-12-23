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
shadowbanned_accounts_string = ''
shadowbanned_spam_accounts_string = ''
shadowbanned_accounts = shadowbanned_accounts_string.split()
shadowbanned_accounts = [acct.replace(",", "") for acct in shadowbanned_accounts]
shadowbanned_accounts.reverse()
shadowbanned_spam_accounts = shadowbanned_spam_accounts_string.split()
shadowbanned_spam_accounts = [acct.replace(",", "") for acct in shadowbanned_spam_accounts]
shadowbanned_spam_accounts.reverse()

flaskport = 7000

app = Flask(__name__)
app.debug = True


@app.route('/listautomoderatedaccounts.html')
def listautomoderatedaccounts():
    global commentHashesAndComments
    commentHashesAndComments = {}
    stringio = StringIO()
    stringio.write('<html>\n<head>\n</head>\n\n')

    stringio.write('<h3>Non-spam (total: {0})</h3>\n'.format(len(shadowbanned_accounts)))
    for shadowbanned_account in shadowbanned_accounts:
        stringio.write('<a href="https://www.reddit.com/u/{0}" target="_blank">{0}</a>'.format(shadowbanned_account))
        stringio.write("<br>\n")
    stringio.write('\n\n')
    stringio.write('<h3>Spam (total: {0})</h3>\n'.format(len(shadowbanned_spam_accounts)))
    for shadowbanned_account in shadowbanned_spam_accounts:
        stringio.write('<a href="https://www.reddit.com/u/{0}" target="_blank">{0}</a>'.format(shadowbanned_account))
        stringio.write("<br>\n")
    stringio.write('</html>')
    pageString = stringio.getvalue()
    stringio.close()
    return Response(pageString, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=flaskport)

