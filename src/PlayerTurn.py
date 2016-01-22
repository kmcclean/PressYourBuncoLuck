from random import randint

#Player turn runs each player's turn.
class PlayerTurn:

    def __init__(self, player, round):
        self.player_turn_player = player
        self.player_turn_round = round


    #This is where a player will select the number of dice they wish to use, roll them, and learn the result of their play.
    def takeTurn(self):
        #TODO Error Handling
        name = self.player_turn_player.player_name
        dice_amount = int(input(name + ", please select the number of dice you wish to use: "))
        dice_result_list = []
        dice_counter = 0

        #Here the dice are rolled, and the results are collected.
        while dice_counter < dice_amount:
            roll = randint(1, 6)
            dice_result_list.append(roll)
            dice_counter += 1

        #Showing the results to the player.
        print("You rolled " + str(dice_result_list))

        #This calculates the score the player achieved.
        scored = self.got_bunco(dice_result_list, self.player_turn_round)

        #Checks to see if the player either achieved a bunco or else buncoed out. If neither occurred, then it changes
        # the players score to reflect the new total.

        if scored >= 3:
            print("You buncoed! You win the round!")
            self.player_turn_player.buncoed()
            return

        if self.triple_out(dice_result_list, self.player_turn_round):
            print ("You tripled out! Lose all your points!")
            self.player_turn_player.reset_points()
            return

        #Tells players how the others are doing.
        self.player_turn_player.scored_points(scored)
        print(self.player_turn_player.getPlayerName() + " just scored " + str(scored) + " points. They now have " +
              str(self.player_turn_player.getPoints()) + " points.")
        return

    #checks to see if a player achieved bunco.
    def got_bunco(self, results, round):

        bunco_check_counter = 0

        for result in results:
            if result == round:
                bunco_check_counter += 1

        return bunco_check_counter

    #This shows whether or not the player tripled out and lost all their points.
    def triple_out(self, results, round):

        for result in results:
            if result != round:
                triple_out_counter = 0
                for roll in results:
                    if result == roll:
                        triple_out_counter += 1

                if triple_out_counter >= 3:
                    return True