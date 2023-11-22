#!/usr/bin/env python3
# TODO: issues with new oauth2 stuff.  Keep using older version of Python for now.
# #!/usr/bin/env python
from participantCollection import ParticipantCollection


if __name__ == "__main__":
    participants = ParticipantCollection()
    for participant in participants.participantsWhoAreStillIn():
        participant.hasCheckedIn = False
    participants.save()

