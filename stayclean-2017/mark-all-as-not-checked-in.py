#!/usr/bin/python
# TODO: issues with new oauth2 stuff.  Keep using older version of Python for now.
# #!/usr/bin/env python
from participantCollection import ParticipantCollection


participants = ParticipantCollection()
for participant in participants.participantsWhoAreStillIn():
    participant.hasCheckedIn = False
participants.save()

