#!/usr/bin/python
import sys
from participantCollection import ParticipantCollection


names = sys.argv[1::]

participants = ParticipantCollection()
for name in names:
    if participants.hasParticipantNamed(name):
        participants.participantNamed(name).isStillIn = True
        print "just reinstated " + name
    else:
        print "*** WARNING: " + name + " is not present in participants.txt"
participants.save()

