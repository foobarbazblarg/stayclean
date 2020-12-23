#!/usr/bin/env python3
from participantCollection import ParticipantCollection


participants = ParticipantCollection()
for participant in participants.participantsWhoAreStillIn():
    participant.hasCheckedIn = False
participants.save()

