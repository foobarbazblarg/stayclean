#!/usr/bin/env python3
from participantCollection import ParticipantCollection
import re
import datetime
import string
import pyperclip

# If this directory is the directory for November, this script gets run on December 1,
# and currentMonthIndex gets the index of November, i.e. 11.
currentMonthIndex = datetime.date.today().month - 1
if currentMonthIndex == 0:
    currentMonthIndex = 12

currentMonthName = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[currentMonthIndex]
uppercaseMonth = currentMonthName.upper()
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
    answer += "CONGRATULATIONS TO THE VICTORS OF THE STAY CLEAN UPPERCASE_MONTH CHALLENGE!\n"
    answer += "Hey everybody, take a second to post a congratulatory comment to the victors of the Stay Clean CURRENT_MONTH_NAME challenge, listed below. **NUMBER_STILL_IN** out of INITIAL_NUMBER original participants made it. that's **PERCENT_STILL_IN%**. Victors, feel free to post a comment with your thoughts about the month. Was there anything specific that worked to keep you clean? What advice do you have for the rest of us? Here are our **NUMBER_STILL_IN victors**:\n\n"
    answer += templateForParticipants()
    return answer

'''
Hey everybody, take a second to post a congratulatory comment to the victors of the Stay Clean November challenge, listed below. **38** out of 287 original participants made it. that's **13%**. Victors, feel free to post a comment with your thoughts about the month. Was there anything specific that worked to keep you clean? What advice do you have for the rest of us? Here are our **38 victors**:

'''


def stringToPrint():
    answer = templateToUse()
    answer = re.sub('NUMBER_STILL_IN', str(numberStillIn), answer)
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('PERCENT_STILL_IN', str(percentStillIn), answer)
    answer = re.sub('CURRENT_MONTH_INDEX', str(currentMonthIndex), answer)
    answer = re.sub('CURRENT_MONTH_NAME', currentMonthName, answer)
    answer = re.sub('UPPERCASE_MONTH', uppercaseMonth, answer)
    return answer

outputString = stringToPrint()
print("=============================================================")
print(outputString)
print("=============================================================")
pyperclip.copy(outputString)


