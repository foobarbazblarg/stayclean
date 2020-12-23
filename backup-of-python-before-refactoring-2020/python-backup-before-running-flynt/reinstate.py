#!/usr/bin/env python3
import sys
from participantCollection import ParticipantCollection


names = sys.argv[1::]

participants = ParticipantCollection()
for name in names:
    if participants.hasParticipantNamed(name):
        participants.participantNamed(name).isStillIn = True
        print(f"just reinstated {name}")
    else:
        print(f"*** WARNING: {name} is not present in participants.txt")
participants.save()

