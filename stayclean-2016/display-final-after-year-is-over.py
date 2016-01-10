#!/usr/bin/python
from participantCollection import ParticipantCollection
import re
import pyperclip

# Edit me!
nextYearURL = ""

year = 2016

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
    answer += "The Stay Clean _YEAR_ year-long challenge is now over.  Join us for **[the NEXT_YEAR challenge](NEXT_YEAR_URL)**.\n"
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
    answer = re.sub('NEXT_YEAR_URL', nextYearURL, answer)
    answer = re.sub('_YEAR_', str(year), answer)
    answer = re.sub('NEXT_YEAR', str(year + 1), answer)
    return answer

outputString = stringToPrint()
print "============================================================="
print outputString
print "============================================================="
pyperclip.copy(outputString)


