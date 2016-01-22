#this class holds all of the information on the players.
class Players:

    def __init__(self, name, roundsWon, pointsThisRound, isComputer):

        self.player_name = name
        self.rounds = roundsWon
        self.points = pointsThisRound
        self.is_comp = isComputer

    #This increases the number of rounds won by the player.
    def won_round(self):
        self.rounds += 1

    #resets the score to zero.
    def reset_points(self):
        self.points = 0

    #Gets the player's name.
    def getPlayerName(self):
        return self.player_name

    #Gets their points total.
    def getPoints(self):
        return self.points

    #Gets their rounds won total.
    def getRoundsWon(self):
        return self.rounds

    #Changes the score by a bunco result.
    def buncoed(self):
        self.points = 21

    #adds the new points onto the score.
    def scored_points(self, newPoints):
        self.points += newPoints
