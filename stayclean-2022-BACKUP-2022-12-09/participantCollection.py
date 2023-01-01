from participant import Participant
import datetime
from typing import Optional
from typing import List
from typing import Dict


class ParticipantCollection:
    __slots__ = ['fileName', 'participants']

    def __init__(self, fileNameString='./participants.txt'):
        self.fileName = fileNameString
        self.participants = []
        f = open(self.fileName, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            participant = Participant()
            participant.setFromLine(line)
            self.participants.append(participant)
        self.sort()

    def hasParticipantNamed(self, nameString) -> bool:
        return self.participantNamed(nameString) is not None

    def sort(self) -> None:
        self.participants.sort(key=lambda participant: participant.name.lower())

    def participantNamed(self, nameString) -> Optional[Participant]:
        participants = [participant for participant in self.participants if participant.name == nameString]
        if participants:
            return participants[0]
        else:
            return None

    def addNewParticipantNamed(self, nameString) -> None:
        if not self.hasParticipantNamed(nameString):
            participant = Participant()
            participant.name = nameString
            self.participants.append(participant)
        self.sort()

    def size(self) -> int:
        return len(self.participants)

    def participantsWhoAreStillIn(self) -> List[Participant]:
        return [participant for participant in self.participants if participant.isStillIn]

    def participantsWhoAreStillInAndHaveCheckedIn(self) -> List[Participant]:
        return [participant for participant in self.participantsWhoAreStillIn() if participant.hasCheckedIn]

    def participantsWhoAreStillInAndHaveNotCheckedIn(self) -> List[Participant]:
        return [participant for participant in self.participantsWhoAreStillIn() if not participant.hasCheckedIn]

    def participantsWithRelapseDates(self) -> List[Participant]:
        return [participant for participant in self.participants if participant.relapseDate is not None]

    def allRelapseDates(self) -> List[datetime.date]:
        return [participant.relapseDate for participant in self.participantsWithRelapseDates()]

    def relapseDatesAndParticipants(self) -> Dict[datetime.date, List[Participant]]:
        answer = {}
        for participant in self.participantsWithRelapseDates():
            date = participant.relapseDate
            if date not in answer:
                answer[date] = []
            answer[date].append(participant)
        return answer

    def relapseDayOfWeekIndexesAndParticipants(self) -> Dict[int, List[Participant]]:
        answer = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        for participant in self.participantsWithRelapseDates():
            answer[participant.relapseDayOfWeekIndex()].append(participant)
        return answer

    def sizeOfParticipantsWhoAreStillIn(self) -> int:
        return len(self.participantsWhoAreStillIn())

    def save(self) -> None:
        f = open(self.fileName, 'w')
        for participant in self.participants:
            f.write(participant.asLine() + "\n")
        f.close()
