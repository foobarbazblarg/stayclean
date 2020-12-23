#!/usr/bin/env python3
import sys
from participantCollection import ParticipantCollection


names = sys.argv[1::]

participants = ParticipantCollection()
for name in names:
    if participants.hasParticipantNamed(name):
        participant = participants.participantNamed(name)
        if participant.isStillIn:
            participant.relapseNowIfNotAlready()
            print(f"just relapsed {name}")
        else:
            print(f"{name} has already relapsed.  Skipping.")
    else:
        print(f"*** WARNING: {name} is not present in participants.txt")
participants.save()

