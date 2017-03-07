#!/usr/bin/env python
from participantCollection import ParticipantCollection


participants = ParticipantCollection()
for participant in participants.participantsWhoAreStillIn():
    participant.hasCheckedIn = False
participants.save()

