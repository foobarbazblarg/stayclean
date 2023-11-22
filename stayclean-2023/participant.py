import datetime
from typing import Optional


class Participant:
    def __init__(self):
        self.name = ""
        self.isStillIn = True
        self.hasCheckedIn = False
        self.relapseDate = None

    @property
    def hasRelapsed(self) -> bool:
        return self.relapseDate is not None

    def setFromLine(self, lineString) -> None:
        # format of participants.txt line:
        # name hasCheckedIn isStillIn
        # e.g.:
        # foobarbazblarg True True
        # print(lineString)
        words = lineString.split()
        self.name = words[0]
        self.hasCheckedIn = words[1] == 'True'
        self.isStillIn = words[2] == 'True'
        if len(words) >= 4:
            self.relapseDate = datetime.datetime.strptime(words[3], "%Y.%m.%d").date()

    def relapseNowIfNotAlready(self) -> None:
        if self.isStillIn:
            self.isStillIn = False
            self.relapseDate = datetime.date.today()

    def relapseDayOfWeekIndex(self) -> Optional[int]:
        if self.relapseDate:
            return self.relapseDate.weekday()
        else:
            return None

    def relapseDayOfWeekName(self) -> Optional[str]:
        if self.relapseDayOfWeekIndex():
            return {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}[self.relapseDayOfWeekIndex()]
        else:
            return None

    def totalNonRelapsedDaysSinceDate(self, startDate) -> int:
        if self.isStillIn:
            endDate = datetime.date.today()
        else:
            endDate = self.relapseDate
        return (endDate - startDate).days + 1

    def asLine(self) -> str:
        answer = self.name + " " + str(self.hasCheckedIn) + " " + str(self.isStillIn)
        if self.relapseDate:
            answer += " "
            answer += self.relapseDate.strftime("%Y.%m.%d")
        return answer
