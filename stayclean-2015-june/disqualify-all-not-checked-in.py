#!/usr/bin/python
import participantCollection


participantCollection = participantCollection.ParticipantCollection()
for participant in participantCollection.participantsWhoAreStillIn():
    if not participant.hasCheckedIn:
        print "disqualifying " + participant.name
        participant.isStillIn = False
participantCollection.save()

