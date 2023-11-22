#!/usr/bin/env python3
from participantCollection import ParticipantCollection


if __name__ == "__main__":
    participants = ParticipantCollection()
    for participant in participants.participantsWhoAreStillIn():
        print("disqualifying " + participant.name)
        participant.isStillIn = False
    participants.save()

