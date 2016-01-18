from random import randint


# TODO List:
# Musts:
# Add error handling
# Add AI
#
class Main:

    print("Welcome to Press Your Bunco! Please select from the following options:")

    #TODO add error handling
    def gameOpening(self):

        #This continues to run the game until the players quit.
        while True:
            gameContinue = True

            #The players can choose to either read the rules of Press Your Bunco or else play the game.
            choice = int(input("\n1: Play Press Your Bunco. \n2: See the rules.\n"))
            if choice == 1:
                gameContinue = self.gameStart()
            elif choice == 2:
                self.pressYourBuncoRules()

            if gameContinue is False:
                break

    #Prints the game rules.
    def pressYourBuncoRules(self):
        print("The object of press your bunco is to win more rounds than your opponents. There are 6 rounds to bunco. In each of the rounds, the goal to be the first to score 21 points. "
              "\nThe way to score points is to roll the round number. Each successful roll is worth a point for the rolling player. A ""Bunco"" occurs when a player rolls three successful rolls at once. This results in automatically winning the round."
              "\nIn Press Your Bunco, you are given the option to choose the number of dice that your roll, between 3 and 7. The more dice you roll, the more points you can score on your turn. But be careful! Should you get three or more of any combination that isn't the round number, you lose all of your points for the round.")


    #This function starts the game by setting up the game with the appropriate number of players, and then allowing them to add themselves to the game.
    def gameStart(self):
        #TODO error handling
        players = int(input("How many human players? "))

        counter = 0
        playerList = []

        #TODO error handling
        #This adds the number of players to the playerList, creating a new instance of each player.
        while counter < players:

            name = input("What is player " + str((counter + 1)) + "'s name? ")
            p = Players(name, 0, 0, False)
            playerList.append(p)

            counter += 1

        print("Let's play Press Your Bunco!")

        #This is where the game is played. First the board is set up. Then the game is played by people.
        game = GameBoard(playerList)
        return game.playGame()


#This is where the game sets itself up. It controls the player's turns and checks to see whether or not someone has one a round or the game.
class GameBoard:

    def __init__(self, playersList):
        self.playersList = playersList

    #This is the game playing. Rounds go until six are finished. A round continues until someone reaches 21 points.
    def playGame(self):
        round = 1
        roundWon = False

        while round <= 6:

            while roundWon == False:

                #This is where the game turns actually happen. Turns happen in order until a player reaches 21 points.
                for player in self.playersList:
                    print("This is round " + str(round))
                    turn = PlayerTurn(player, round)
                    turn.takeTurn()
                    if player.pointsScored >= 21:
                        print(player.getName() + " wins the round!")
                        player.newRoundsWon()
                        roundWon = True
            round += 1

            #resets the points after each round.
            for player in self.playersList:
                player.resetPoints()

        dummy = Players("", -1, -1, True)
        winnerList = [dummy]

        #Once all six rounds have been played, this check determines who won.
        for player in self.playersList:
            check = winnerList[0]
            if player.getRoundsWon > check.getRoundsWon():
                winnerList.clear()
                winnerList.append(player)

            elif player.getRoundsWon == check.getRoundsWon():
                winnerList.append(player)

        print("Your winners are: ")
        for winner in winnerList:
            print(winner.getPlayerName())
        print("Congratulations!!!")

        #TODO error handling
        #This allows the players to decide if they want to continue playing.
        #This is bounced back up to the gameStart in Main, which bounces it back up to gameOpening to see if the
        #game will be replayed.
        continueChoice = int(input("\nWould you like to continue?\n1: Yes\n2: No"))
        if continueChoice == 1:
            return True
        elif continueChoice == 2:
            return False


#Player turn runs each player's turn.
class PlayerTurn:

    def __init__(self, player, round):
        self.ptPlayer = player
        self.ptRound = round


    #This is where a player will select the number of dice they wish to use, roll them, and learn the result of their play.
    def takeTurn(self):
        #TODO Error Handling

        diceAmount = int(input(self.ptPlayer.getPlayerName() +  ", please select the number of dice you wish to use: "))
        diceResultList = []
        diceCounter = 0

        #Here the dice are rolled, and the results are collected.
        while diceCounter < diceAmount:
            roll = randint(1, 6)
            diceResultList.append(roll)
            diceCounter += 1

        #Showing the results to the player.
        print("You rolled " + str(diceResultList))

        #This calculates the score the player achieved.
        scored = self.gotBunco(diceResultList, self.ptRound)

        #Checks to see if the player either achieved a bunco or else buncoed out. If neither occurred, then it changes
        # the players score to reflect the new total.

        if scored >= 3:
            print("You buncoed! You win the round!")
            self.ptPlayer.buncoed()
            return

        if self.buncoedOutCheck(diceResultList, self.ptRound):
            print ("You buncoed out! Lose all your points!")
            self.ptPlayer.resetPoints()
            return

        #Tells players how the others are doing.
        self.ptPlayer.pointsScored(scored)
        print(self.ptPlayer.getPlayerName() + " just scored " + str(scored) + " points. They now have " +
              self.ptPlayer.getPoints() + " points.")
        return

    #checks to see if a player achieved bunco.
    def gotBunco(self, results, round):

        buncoCheckCounter = 0

        for result in results:
            if result == round:
                buncoCheckCounter += 1

        return buncoCheckCounter

    #TODO not creating the right results.
    #This shows whether or not the player flopped out and lost all their points.
    def buncoedOutCheck(self, results, round):

        for result in results:
            if result != round:
                buncoOutCounter = 0
                for roll in results:
                    if results == roll:
                        buncoOutCounter += 1

                if buncoOutCounter >= 3:
                    return True

#this class holds all of the information on the players.
class Players:

    def __init__(self, name, roundsWon, pointsThisRound, isComputer):

        self.playerName = name
        self.rounds = roundsWon
        self.points = pointsThisRound
        self.isComp = isComputer

    #This increases the number of rounds won by the player.
    def newRoundWon(self):
        self.rounds += 1

    #resets the score to zero.
    def resetPoints(self):
        self.points = 0

    #Gets the player's name.
    def getPlayerName(self):
        return self.playerName

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
    def pointsScored(self, newPoints):
        self.points += newPoints

#Starts the game.
m = Main()
m.gameOpening()