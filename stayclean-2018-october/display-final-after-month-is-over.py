#!/usr/bin/python
# TODO: issues with new oauth2 stuff.  Keep using older version of Python for now.
# #!/usr/bin/env python

from participantCollection import ParticipantCollection
import re
import datetime
import pyperclip

# Edit Me!
# This script gets run on the first day of the following month, and that month's URL is
# what goes here.  E.g. If this directory is the directory for February, this script gets
# run on March 1, and this URL is the URL for the March challenge page.
nextMonthURL = "https://www.reddit.com/r/pornfree/comments/9t9kh3/stay_clean_november_this_thread_updated_daily/"

# If this directory is the directory for November, this script gets run on December 1,
# and currentMonthIndex gets the index of November, i.e. 11.
currentMonthIndex = datetime.date.today().month - 1
if currentMonthIndex == 0:
    currentMonthIndex = 12

currentMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[currentMonthIndex]
nextMonthIndex = currentMonthIndex % 12 + 1
nextMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[nextMonthIndex]

participants = ParticipantCollection()
numberStillIn = participants.sizeOfParticipantsWhoAreStillIn()
initialNumber = participants.size()
percentStillIn = int(round(100 * numberStillIn / initialNumber, 0))


def templateForParticipants():
    answer = ""
    for participant in participants.participantsWhoAreStillInAndHaveCheckedIn():
        answer += "/u/" + participant.name
        answer += "\n\n"
    return answer


def templateToUse():
    answer = ""
    answer += "The Stay Clean CURRENT_MONTH_NAME challenge is now over.  Join us for **[the NEXT_MONTH_NAME challenge](NEXT_MONTH_URL)**.\n"
    answer += "\n"
    answer += "**NUMBER_STILL_IN** out of INITIAL_NUMBER participants made it all the way through the challenge. That's **PERCENT_STILL_IN%**.\n"
    answer += "\n"
    answer += "Congratulations to these participants, all of whom were victorious:\n\n"
    answer += templateForParticipants()
    return answer


def stringToPrint():
    answer = templateToUse()
    answer = re.sub('NUMBER_STILL_IN', str(numberStillIn), answer)
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('PERCENT_STILL_IN', str(percentStillIn), answer)
    answer = re.sub('CURRENT_MONTH_INDEX', str(currentMonthIndex), answer)
    answer = re.sub('CURRENT_MONTH_NAME', currentMonthName, answer)
    answer = re.sub('NEXT_MONTH_INDEX', str(nextMonthIndex), answer)
    answer = re.sub('NEXT_MONTH_NAME', nextMonthName, answer)
    answer = re.sub('NEXT_MONTH_URL', nextMonthURL, answer)
    return answer

outputString = stringToPrint()
print "============================================================="
print outputString
print "============================================================="
pyperclip.copy(outputString)


