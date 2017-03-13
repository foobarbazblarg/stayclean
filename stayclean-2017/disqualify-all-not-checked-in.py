#!/usr/bin/python
# TODO: issues with new oauth2 stuff.  Keep using older version of Python for now.
# #!/usr/bin/env python
from participantCollection import ParticipantCollection


participants = ParticipantCollection()
for participant in participants.participantsWhoAreStillIn():
    if not participant.hasCheckedIn:
        print "disqualifying " + participant.name
        participant.isStillIn = False
participants.save()

