#!/usr/bin/python
import participantCollection


participantCollection = participantCollection.ParticipantCollection()
for participant in participantCollection.participantsWhoAreStillIn():
    participant.hasCheckedIn = True
participantCollection.save()

