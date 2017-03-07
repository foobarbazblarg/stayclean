#!/usr/bin/env python
from participantCollection import ParticipantCollection
import pyperclip


participants = ParticipantCollection()


def stringToPrint():
    answer = ""
    answer += "Here are the **" + str(participants.size()) + " participants** who have already signed up:\n\n"
    for participant in participants.participants:
        answer += "/u/" + participant.name
        answer += "\n\n"
    return answer

outputString = stringToPrint()
print "============================================================="
print outputString
print "============================================================="
pyperclip.copy(outputString)
