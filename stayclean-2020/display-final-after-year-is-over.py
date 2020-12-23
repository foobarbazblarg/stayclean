#!/usr/bin/env python3
from participantCollection import ParticipantCollection
import re
import pyperclip

# Edit me!
nextYearURL = "(2021 URL GOES HERE)"
year = 2020


participants = ParticipantCollection()
numberStillIn = participants.sizeOfParticipantsWhoAreStillIn()
initialNumber = participants.size()
percentStillIn = int(round(100 * numberStillIn / initialNumber, 0))


def templateForParticipants() -> str:
    answer = ""
    for participant in participants.participantsWhoAreStillInAndHaveCheckedIn():
        answer += "/u/" + participant.name
        answer += "\n\n"
    return answer


def templateToUse() -> str:
    return f'''The Stay Clean _YEAR_ year-long challenge is now over.  Join us for **[the NEXT_YEAR challenge](NEXT_YEAR_URL)**.

**NUMBER_STILL_IN** out of INITIAL_NUMBER participants made it all the way through the challenge. That's **PERCENT_STILL_IN%**.

Congratulations to these participants, all of whom were victorious:

{templateForParticipants()}'''


def stringToPrint() -> str:
    answer = templateToUse()
    answer = re.sub('NUMBER_STILL_IN', str(numberStillIn), answer)
    answer = re.sub('INITIAL_NUMBER', str(initialNumber), answer)
    answer = re.sub('PERCENT_STILL_IN', str(percentStillIn), answer)
    answer = re.sub('NEXT_YEAR_URL', nextYearURL, answer)
    answer = re.sub('_YEAR_', str(year), answer)
    answer = re.sub('NEXT_YEAR', str(year + 1), answer)
    return answer


if __name__ == "__main__":
    outputString = stringToPrint()
    print("=============================================================")
    print(outputString)
    print("=============================================================")
    pyperclip.copy(outputString)


