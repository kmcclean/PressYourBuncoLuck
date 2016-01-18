class Players:

    def __init__(self, name, roundsWon, pointsThisRound, isComputer):

        self.playerName = name
        self.rounds = roundsWon
        self.points = pointsThisRound
        self.isComp = isComputer

    def newRoundWon(self):
        self.rounds += 1

    def resetPoints(self):
        self.points = 0

    def getPlayerName(self):
        return self.playerName

    def getPoints(self):
        return self.points

    def getRound(self):
        return self.rounds

    def buncoed(self):
        self.points = 21

    def buncoedOut(self):
        self.points = 0

    def pointsScored(self, newPoints):

        self.points += newPoints
