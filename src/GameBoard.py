from src.Players import Players
from src.PlayerTurn import PlayerTurn
from src.ErrorHandling import ErrorHandling
#This is where the game sets itself up. It controls the player's turns and checks to see whether or not someone has one a round or the game.
class GameBoard:

    def __init__(self, players_list):
        self.players_list = players_list

    #This is the game playing. Rounds go until six are finished. A round continues until someone reaches 21 points.
    def play_game(self):
        round = 1

        while round <= 6:

            round_won = False

            while round_won == False:

                #This is where the game turns actually happen. Turns happen in order until a player reaches 21 points.
                for player in self.players_list:
                    print("\nThis is round " + str(round))
                    print("Score: ")
                    for player in self.players_list:
                        print(player.player_name + ": " + str(player.points) + " points")
                    turn = PlayerTurn(player, round)
                    turn.takeTurn()
                    if player.getPoints() >= 21:
                        print(player.getPlayerName() + " wins the round!")
                        player.won_round()
                        round_won = True
                        break
            round += 1

            #resets the points after each round.
            for player in self.players_list:
                player.reset_points()

        dummy = Players("", -1, -1, True)
        winner_list = [dummy]

        #Once all six rounds have been played, this check determines who won.
        for player in self.players_list:
            check = winner_list[0]
            check_rounds = check.rounds
            player_rounds = player.rounds
            if player_rounds > check_rounds:
                winner_list.clear()
                winner_list.append(player)

            elif player_rounds == check_rounds:
                winner_list.append(player)

        print("Your winners are: ")
        for winner in winner_list:
            print(winner.getPlayerName())
        print("Congratulations!!!")

        #This allows the players to decide if they want to continue playing.
        #This is bounced back up to the gameStart in Main, which bounces it back up to gameOpening to see if the
        #game will be replayed.
        eh = ErrorHandling()
        continue_choice_text = "\n1: Yes\n2: No\nWould you like to continue? "
        continue_choice = eh.range_integer_input_checking(continue_choice_text, 1, 2)
        if continue_choice == 1:
            return True
        elif continue_choice == 2:
            return False