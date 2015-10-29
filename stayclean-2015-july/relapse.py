#!/usr/bin/python
import sys
import participantCollection


names = sys.argv[1::]

participantCollection = participantCollection.ParticipantCollection()
for name in names:
    if participantCollection.hasParticipantNamed(name):
        participant = participantCollection.participantNamed(name)
        if participant.isStillIn:
            participant.relapseNowIfNotAlready()
            print "just relapsed " + name
        else:
            print name + " has already relapsed.  Skipping."
    else:
        print "*** WARNING: " + name + " is not present in participants.txt"
participantCollection.save()

