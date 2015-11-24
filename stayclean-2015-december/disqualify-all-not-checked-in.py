#!/usr/bin/python
from participantCollection import ParticipantCollection


participants = ParticipantCollection()
for participant in participants.participantsWhoAreStillIn():
    if not participant.hasCheckedIn:
        print "disqualifying " + participant.name
        participant.isStillIn = False
participants.save()

