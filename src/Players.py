# this class holds all of the information on the players.
class Players:

    def __init__(self, name, rounds_won, points_this_round, is_computer):

        self.player_name = name
        self.rounds = rounds_won
        self.points = points_this_round
        self.is_comp = is_computer

    # This increases the number of rounds won by the player.
    def won_round(self):
        self.rounds += 1

    # resets the score to zero.
    def reset_points(self):
        self.points = 0

    # Changes the score by a bunco result.
    def buncoed(self):
        self.points = 21

    # adds the new points onto the score.
    def scored_points(self, new_points):
        self.points += new_points
