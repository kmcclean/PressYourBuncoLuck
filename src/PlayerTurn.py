from random import randint
from src.ErrorHandling import ErrorHandling


# Player turn runs each player's turn.
class PlayerTurn:

    def __init__(self, player, turn_round):
        self.player_turn_player = player
        self.player_turn_round = turn_round

    def take_computer_turn(self, players_list):

        highest_points = 0

        for player in players_list:
            if player.points > highest_points:
                highest_points = player.points

        point_difference = highest_points - self.player_turn_player.points

        if point_difference <= 3:
            dice_amount = 4
        elif point_difference <= 7:
            dice_amount = 5
        elif point_difference <= 14:
            dice_amount = 6
        else:
            dice_amount = 7

        self.roll_results(dice_amount, self.player_turn_player)

    def take_human_turn(self):
        # This is where a player will select the number of dice they wish to use, roll them, and learn the result
        # of their play.
        eh = ErrorHandling()

        name = self.player_turn_player.player_name
        dice_amount_text = name + ", please select the number of dice you wish to use: "

        # TODO This should have an error handling range of 3-7.
        dice_amount = eh.range_integer_input_checking(dice_amount_text, 0, 500)

        self.roll_results(dice_amount, self.player_turn_player)

    # Here the dice are rolled, and the results are collected.
    def roll_results(self, dice_amount, player):

        dice_result_list = []
        dice_counter = 0
        while dice_counter < dice_amount:
            roll = randint(1, 6)
            dice_result_list.append(roll)
            dice_counter += 1

        # Showing the results to the player.
        print(player.player_name + " rolled " + str(dice_result_list))

        # This calculates the score the player achieved.
        scored = self.got_bunco(dice_result_list, self.player_turn_round)

        # Checks to see if the player either achieved a bunco or else buncoed out. If neither occurred, then it changes
        # the players score to reflect the new total.

        if scored >= 3:
            print(player.player_name + " buncoed! You win the round!")
            self.player_turn_player.buncoed()
            return

        if self.triple_out(dice_result_list, self.player_turn_round):
            print(player.player_name + " tripled out! Lose all your points!")
            self.player_turn_player.reset_points()
            return

        # Tells players how the others are doing.
        self.player_turn_player.scored_points(scored)
        print(self.player_turn_player.player_name + " just scored " + str(scored) + " points. They now have " +
              str(self.player_turn_player.points) + " points.\n")
        return

    # checks to see if a player achieved bunco.
    def got_bunco(self, results, this_round):

        bunco_check_counter = 0

        for result in results:
            if result == this_round:
                bunco_check_counter += 1

        return bunco_check_counter

    # This shows whether or not the player tripled out and lost all their points.
    def triple_out(self, results, this_round):

        for result in results:
            if result != this_round:
                triple_out_counter = 0
                for roll in results:
                    if result == roll:
                        triple_out_counter += 1

                if triple_out_counter >= 3:
                    return True