#!/usr/bin/python
import participantCollection


participantCollection = participantCollection.ParticipantCollection()
print "Here are the **" + str(participantCollection.size()) + " participants** who have already signed up:\n"
for participant in participantCollection.participants:
    print "/u/" + participant.name
    print ""

