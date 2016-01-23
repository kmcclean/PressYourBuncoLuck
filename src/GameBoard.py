from src.Players import Players
from src.PlayerTurn import PlayerTurn
from src.ErrorHandling import ErrorHandling


# This is where the game sets itself up. It controls the player's turns and checks to see whether or not someone has
# won a round or the game.
class GameBoard:

    def __init__(self, players_list):
        self.players_list = players_list

    # This is the game playing. Rounds go until six are finished. A round continues until someone reaches 21 points.
    def play_game(self):
        round_number = 1

        while round_number <= 6:

            round_won = False

            while round_won is False:

                # This is where the game turns actually happen. Turns happen in order until a player reaches 21 points.
                for player in self.players_list:
                    print("\nThis is round " + str(round_number))
                    print("Score: ")
                    for player_name in self.players_list:
                        print(player_name.player_name + ": " + str(player_name.points) + " points")
                    turn = PlayerTurn(player, round_number)

                    if player.is_comp is True:
                        turn.take_computer_turn(self.players_list)
                    elif player.is_comp is False:
                        turn.take_human_turn()

                    if player.points >= 21:
                        print(player.player_name + " wins the round!")
                        player.won_round()
                        round_won = True
                        break
            round_number += 1

            # resets the points after each round.
            for player in self.players_list:
                player.reset_points()

        dummy = Players("", -1, -1, True)
        winner_list = [dummy]

        # Once all six rounds have been played, this check determines who won.
        for player in self.players_list:
            check = winner_list[0]
            check_rounds = check.rounds
            player_rounds = player.rounds
            if player_rounds > check_rounds:
                winner_list.clear()
                winner_list.append(player)

            elif player_rounds == check_rounds:
                winner_list.append(player)

        verb_tense = ""
        if len(winner_list) == 1:
            verb_tense = " is"
        else:
            verb_tense = "s are"
        print("Your winner" + verb_tense + ": ")
        for winner in winner_list:
            print(winner.player_name)
        print("Congratulations!!!")

        file = open('alltimewinners.txt', 'r')
        winners_dictionary = {}
        for line in file:
            print("Line test: " + line)
            line = line.strip("\n")
            line_list = line.split(" , ")
            winners_dictionary[line_list[0]] = line_list[1]

        file.close()
        file = open("alltimewinners.txt", "w")

        keys = winners_dictionary.keys()

        for winner in winner_list:
            if winner.is_comp is True:
                winner_name = "Computer"
            else:
                winner_name = winner.player_name

            new = True
            for key in keys:
                if winner_name == key:
                    winners_dictionary[key] = str(int(winners_dictionary.get(key)) + 1)
                    new = False
                    break

            if new == True:
                winners_dictionary[winner_name] = 1

        winners_writing_list = []
        for key in winners_dictionary:
            winner_string = str(key) + " , " + str(winners_dictionary.get(key)) + "\n"
            winners_writing_list.append(winner_string)

        for line in winners_writing_list:
            file.write(line)

        file.close()

        # This allows the players to decide if they want to continue playing.
        # This is bounced back up to the gameStart in Main, which bounces it back up to gameOpening to see if the
        # game will be replayed.
        eh = ErrorHandling()
        continue_choice_text = "\n1: Yes\n2: No\nWould you like to continue? "
        continue_choice = eh.range_integer_input_checking(continue_choice_text, 1, 2)

        if continue_choice == 1:
            return True
        elif continue_choice == 2:
            return False