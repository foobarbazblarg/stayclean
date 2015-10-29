#!/usr/bin/python
import participantCollection
import pyperclip


participantCollection = participantCollection.ParticipantCollection()

def stringToPrint():
    answer = ""
    answer += "Here are the **" + str(participantCollection.size()) + " participants** who have already signed up:\n\n"
    for participant in participantCollection.participants:
        answer += "/u/" + participant.name
        answer += "\n\n"
    return answer

outputString = stringToPrint()
print "============================================================="
print outputString
print "============================================================="
pyperclip.copy(outputString)
