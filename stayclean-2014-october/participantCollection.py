from participant import Participant

class ParticipantCollection:
    def __init__(self):
        self.participants = []
        f = open(self.fileName(), 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            participant = Participant()
            participant.setFromLine(line)
            self.participants.append(participant)
        self.sort()

    def hasParticipantNamed(self, nameString):
        return self.participantNamed(nameString) != None

    def sort(self):
        self.participants.sort(key=lambda participant: participant.name.lower())

    def participantNamed(self, nameString):
        participants = [participant for participant in self.participants if participant.name == nameString]
        if participants:
            return participants[0]
        else:
            return None

    def addNewParticipantNamed(self, nameString):
        if not self.hasParticipantNamed(nameString):
            participant = Participant()
            participant.name = nameString
            self.participants.append(participant)
        self.sort()

    def size(self):
        return len(self.participants)

    def participantsWhoAreStillIn(self):
        return [participant for participant in self.participants if participant.isStillIn]

    def participantsWhoAreStillInAndHaveCheckedIn(self):
        return [participant for participant in self.participantsWhoAreStillIn() if participant.hasCheckedIn]

    def participantsWhoAreStillInAndHaveNotCheckedIn(self):
        return [participant for participant in self.participantsWhoAreStillIn() if not participant.hasCheckedIn]

    def sizeOfParticipantsWhoAreStillIn(self):
        return len(self.participantsWhoAreStillIn())

    def fileName(self):
        return "./participants.txt"

    def save(self):
        f = open(self.fileName(), 'w')
        for participant in self.participants:
            f.write(participant.asLine() + "\n")
        f.close()
