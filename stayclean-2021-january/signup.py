#!/usr/bin/python3
import sys
from participantCollection import ParticipantCollection


if __name__ == "__main__":
    names = sys.argv[1::]
    participants = ParticipantCollection()
    for name in names:
        if participants.hasParticipantNamed(name):
            print(f"{name} has already signed up.  Skipping.")
        else:
            participants.addNewParticipantNamed(name)
            print(f"just added {name}")
    participants.save()

