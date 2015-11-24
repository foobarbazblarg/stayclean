#!/usr/bin/python
import sys
from participantCollection import ParticipantCollection


names = sys.argv[1::]

participants = ParticipantCollection()
for name in names:
    if participants.hasParticipantNamed(name):
        participant = participants.participantNamed(name)
        if participant.isStillIn:
            participant.relapseNowIfNotAlready()
            print "just relapsed " + name
        else:
            print name + " has already relapsed.  Skipping."
    else:
        print "*** WARNING: " + name + " is not present in participants.txt"
participants.save()

