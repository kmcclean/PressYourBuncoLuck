from random import randint


class PlayerTurn:

    def __init__(self, player, round):
        self.ptPlayer = player
        self.ptRound = round



    def takeTurn(self):

        #TODO Error Handling
        diceAmount = int(input(self.ptPlayer.getPlayerName() +  "Please select the number of dice you wish to use: "))

        diceResultList = []

        diceCounter = 0

        while diceCounter < diceAmount:
            roll = randint(1, 6)
            diceResultList.append(roll)
            diceCounter += 1

        print("You rolled " + diceResultList)


        scored = self.gotBunco(diceResultList, self.ptRound)

        if scored >= 3:
            print("You buncoed! You win the round!")
            self.ptPlayer.buncoed()
            return

        if self.buncoedOutCheck(diceResultList, self.ptRound):
            print ("You buncoed out! Lose all your points!")
            self.ptPlayer.buncoedOut()
            return

        self.ptPlayer.pointsScored(scored)
        return

    def gotBunco(self, results, round):

        buncoCheckCounter = 0

        for result in results:
            if result == round:
                buncoCheckCounter += 1

        return buncoCheckCounter

    def buncoedOutCheck(self, results, round):

        for result in results:
            if result != round:
                buncoOutCounter = 0
                for roll in results:
                    if results == roll:
                        buncoOutCounter += 1

                if buncoOutCounter >= 3:
                    return True
