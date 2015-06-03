#A program to find the best Bot MORTAL KOMBOT
#By Daniel Graham

import game
import fsmMaker
import fsmAI
import random
import time
import makeAllBots


minNumGamesEachBotPlays = 3
minimumAllowedWinRatio = .5


        
def testYourMight():
    #method to pit each bot against three other random bots from the list and determine a winner. Then record that value and remove the bad ones.
    iterations = 0
    start = time.time()
    while True:
        allBots = open("SuperBots.txt", "r")
        botString = allBots.read()
        botList = botString.split("\n\n")
        allBots.close()
        botToTest = makeAllBots.makeAllBots()
        for i in range(minNumGamesEachBotPlays):

            bot2 = random.choice(botList)
            
            bot3 = bot2
            while bot3 == bot2:
                bot3 = random.choice(botList)
            bot4 = bot2
            while bot4 == bot2 or bot4 == bot3:
                bot4 = random.choice(botList)

            botsPlaying = [botToTest, bot2, bot3, bot4]
            gamePlayed = game.localGame()
            updatedBots = gamePlayed.play_game(botsPlaying)
            botList[botList.index(bot2)] = updatedBots[1]
            botList[botList.index(bot3)] = updatedBots[2]
            botList[botList.index(bot4)] = updatedBots[3]
            botToTest = updatedBots[0]

        
        if eval(botToTest.split("@")[1]) >= minimumAllowedWinRatio:
            botList.append(botToTest)
            print "Added new bot! One more step on the path to world domination"

        updatedSuper = []    
        for m in range(len(botList)):
            if m < 7:
                updatedSuper.append(botList[m])
            else:
                if eval(botList[m].split("@")[1]) >= minimumAllowedWinRatio:
                    updatedSuper.append(botList[m])

        #print botList
        allBotsUpdate = open("SuperBots.txt", "w")
        writeString = "\n\n".join(updatedSuper)
        allBotsUpdate.write(writeString)
        allBotsUpdate.close()
                
        #Once enough bots are added, the random can come out and the database can monitor itself for top 50 percent

        iterations += 1
        if (iterations % 10 == 0):
            print "Num Bots tested: ", iterations
            print " Time (seconds) Elapsed: ", time.time() - start

        
def main():
    testYourMight()


main()
