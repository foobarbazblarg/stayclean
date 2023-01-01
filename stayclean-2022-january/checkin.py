#!/usr/bin/env python3
import sys
from participantCollection import ParticipantCollection


if __name__ == "__main__":
    names = sys.argv[1::]
    participants = ParticipantCollection()
    for name in names:
        if participants.hasParticipantNamed(name):
            participants.participantNamed(name).hasCheckedIn = True
            print(f"just checked in {name}")
        else:
            print(f"*** WARNING: {name} is not present in participants.txt")
    participants.save()

