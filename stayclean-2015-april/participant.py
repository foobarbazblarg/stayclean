import datetime


class Participant:
    def __init__(self):
        self.name = ""
        self.isStillIn = True
        self.hasCheckedIn = False
        self.relapseDate = None

    def setFromLine(self, lineString):
        # format of participants.txt line:
        # name hasCheckedIn isStillIn
        # e.g.:
        # foobarbazblarg True True
        words = lineString.split()
        self.name = words[0]
        self.hasCheckedIn = words[1] == 'True'
        self.isStillIn = words[2] == 'True'
        if len(words)>=4:
            self.relapseDate = datetime.datetime.strptime(words[3], "%Y.%m.%d").date()

    def relapseNowIfNotAlready(self):
        if self.isStillIn:
            self.isStillIn = False
            self.relapseDate = datetime.date.today()

    def relapseDayOfWeekIndex(self):
        if self.relapseDate:
            return self.relapseDate.weekday()
        else:
            return None

    def relapseDayOfWeekName(self):
        if self.relapseDayOfWeekIndex():
            return {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}[self.relapseDayOfWeekIndex()]
        else:
            return None

    def asLine(self):
        answer = self.name + " " + str(self.hasCheckedIn) + " " + str(self.isStillIn)
        if self.relapseDate:
            answer += " "
            answer += self.relapseDate.strftime("%Y.%m.%d")
        return answer
