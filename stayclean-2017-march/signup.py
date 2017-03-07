#!/usr/bin/python
import sys
from participantCollection import ParticipantCollection


names = sys.argv[1::]

participants = ParticipantCollection()
for name in names:
    if participants.hasParticipantNamed(name):
        print name + " has already signed up.  Skipping."
    else:
        participants.addNewParticipantNamed(name)
        print "just added " + name
participants.save()

