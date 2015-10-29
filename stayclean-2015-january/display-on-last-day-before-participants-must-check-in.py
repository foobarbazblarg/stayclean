#!/usr/bin/python
import participantCollection


participantCollection = participantCollection.ParticipantCollection()
numberStillIn = participantCollection.sizeOfParticipantsWhoAreStillIn()
initialNumber = participantCollection.size()
print "There are currently **" + str(numberStillIn) + " out of " + str(initialNumber) +"** original participants.  That's **" + str(int(round(100*numberStillIn/initialNumber,0))) + "%**."
print "These participants have checked in at least once in the last 15 days:"
print ""
for participant in participantCollection.participantsWhoAreStillInAndHaveCheckedIn():
    print "/u/" + participant.name
    print ""

print "These participants have not reported a relapse, so they are still in the running, but **if they do not check in by the end of today, they will be removed from the list, and will not be considered victorious**:"
print ""
for participant in participantCollection.participantsWhoAreStillInAndHaveNotCheckedIn():
    print "/u/" + participant.name + " ~"
    print ""

