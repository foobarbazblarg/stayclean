class Participant:
    def __init__(self):
        self.name = ""
        self.isStillIn = True
        self.hasCheckedIn = False

    def setFromLine(self, lineString):
        # format of participants.txt line:
        # name hasCheckedIn isStillIn
        # e.g.:
        # foobarbazblarg True True
        words = lineString.split()
        self.name = words[0]
        self.hasCheckedIn = words[1] == 'True'
        self.isStillIn = words[2] == 'True'

    def asLine(self):
        return self.name + " " + str(self.hasCheckedIn) + " " + str(self.isStillIn)

