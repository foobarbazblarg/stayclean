#!/usr/bin/python
import sys
import participantCollection


names = sys.argv[1::]

participantCollection = participantCollection.ParticipantCollection()
for name in names:
    if participantCollection.hasParticipantNamed(name):
        participantCollection.participantNamed(name).hasCheckedIn = True
        print "just checked in " + name
    else:
        print "*** WARNING: " + name + " is not present in participants.txt"
participantCollection.save()

