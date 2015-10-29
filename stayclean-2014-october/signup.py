#!/usr/bin/python
import sys
import participantCollection


names = sys.argv[1::]

participantCollection = participantCollection.ParticipantCollection()
for name in names:
    if participantCollection.hasParticipantNamed(name):
        print name + " has already signed up.  Skipping."
    else:
        participantCollection.addNewParticipantNamed(name)
        print "just added " + name
participantCollection.save()

