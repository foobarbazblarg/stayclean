#!/usr/bin/python
from participantCollection import ParticipantCollection
import re
import datetime
import string
import pyperclip

year = 2016

# If this directory is the directory for November, this script gets run on December 1,
# and currentMonthIndex gets the index of November, i.e. 11.
currentMonthIndex = datetime.date.today().month - 1
if currentMonthIndex == 0:
    currentMonthIndex = 12

currentMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[currentMonthIndex]
uppercaseMonth = string.upper(currentMonthName)
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
    answer += "CONGRATULATIONS TO THE VICTORS OF THE STAY CLEAN _YEAR_ YEAR-LONG CHALLENGE!\n"
    answer += "Hey everybody, take a second to post a congratulatory comment to the victors of the Stay Clean _YEAR_ year-long challenge, listed below. **NUMBER_STILL_IN** out of INITIAL_NUMBER original participants made it. that's **PERCENT_STILL_IN%**. Here are our **NUMBER_STILL_IN victors**:\n\n"
    answer += templateForParticipants()
    return answer


def stringToPrint():
    answer = templateToUse()
    answer = re.sub('NUMBER_STILL_IN', str(numberStillIn), answer)
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('PERCENT_STILL_IN', str(percentStillIn), answer)
    answer = re.sub('CURRENT_MONTH_INDEX', str(currentMonthIndex), answer)
    answer = re.sub('CURRENT_MONTH_NAME', currentMonthName, answer)
    answer = re.sub('UPPERCASE_MONTH', uppercaseMonth, answer)
    answer = re.sub('_YEAR_', str(year), answer)
    return answer

outputString = stringToPrint()
print "============================================================="
print outputString
print "============================================================="
pyperclip.copy(outputString)


