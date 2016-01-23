from src.GameBoard import GameBoard
from src.Players import Players
from src.ErrorHandling import ErrorHandling
# TODO List:
# Musts:
# Add AI
# Read/write results


class Main:

    print("Welcome to Press Your Bunco! Please select from the following options:")

    def game_opening(self):

        eh = ErrorHandling()

        # This continues to run the game until the players quit.
        while True:
            game_continue = True

            # The players can choose to either read the rules of Press Your Bunco or else play the game.
            choice_text = "\n1: Play Press Your Bunco. \n2: See the rules.\nChoose an option: "
            choice = eh.range_integer_input_checking(choice_text, 1, 2)
            if choice == 1:
                game_continue = self.game_start()
            elif choice == 2:
                self.press_your_bunco_rules()

            if game_continue is False:
                break

    # Prints the game rules.
    def press_your_bunco_rules(self):
        print("The object of press your bunco is to win more rounds than your opponents. There are 6 rounds to bunco. In each of the rounds, the goal to be the first to score 21 points. "
              "\nThe way to score points is to roll the round number. Each successful roll is worth a point for the rolling player. A ""Bunco"" occurs when a player rolls three successful rolls at once. This results in automatically winning the round."
              "\nIn Press Your Bunco, you are given the option to choose the number of dice that your roll, between 3 and 7. The more dice you roll, the more points you can score on your turn. But be careful! Should you get three or more of any combination that isn't the round number, you lose all of your points for the round.")


    # This function starts the game by setting up the game with the appropriate number of players, and then allowing them to add themselves to the game.
    def game_start(self):

        eh = ErrorHandling()

        human_players_input = "How many human players? "
        human_players = eh.range_integer_input_checking(human_players_input, 1, float('inf'))
        # human_players = eh.positive_integer_input_checking(human_players_input)

        counter = 0
        player_list = []

        # This adds the number of players to the player_list, creating a new instance of each player.
        while counter < human_players:
            name_text = "What is player " + str((counter + 1)) + "'s name? "
            name = eh.non_blank_string(name_text)
            p = Players(name, 0, 0, False)
            player_list.append(p)

            counter += 1

        computer_players_input = "How many computer players? "
        computer_players = eh.range_integer_input_checking(computer_players_input, 0, float('inf'))

        computer_count = 0

        while computer_count < computer_players:
            computer_player_name = "Computer Player " + str(computer_count + 1)
            p = Players(computer_player_name, 0, 0, True)
            player_list.append(p)
            computer_count += 1

        print("Let's play Press Your Bunco!")

        # This is where the game is played. First the board is set up. Then the game is played by people.
        game = GameBoard(player_list)
        return game.play_game()

# Starts the game.
m = Main()
m.game_opening()