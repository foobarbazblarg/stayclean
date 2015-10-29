#!/usr/bin/python
import participantCollection


participantCollection = participantCollection.ParticipantCollection()
numberStillIn = participantCollection.sizeOfParticipantsWhoAreStillIn()
initialNumber = participantCollection.size()
print "There are currently **" + str(numberStillIn) + " out of " + str(initialNumber) +"** original participants.  That's **" + str(int(round(100*numberStillIn/initialNumber,0))) + "%**  Here is the list of participants still with the challenge:\n"
for participant in participantCollection.participantsWhoAreStillIn():
    if participant.hasCheckedIn:
        print "/u/" + participant.name
    else:
        print "/u/" + participant.name + " ~"
    print ""

