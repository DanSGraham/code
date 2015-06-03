#A program to find the best Bot MORTAL KOMBOT
#By Daniel Graham

import game
import fsmMaker
import fsmAI
import random
import time

maxStatements = 10
maxStatementSize = 2
minNumGamesEachBotPlays = 2
minimumAllowedWinRatio = .5


        
def testYourMight():
    #method to pit each bot against three other random bots from the list and determine a winner. Then record that value and remove the bad ones.
    iterations = 0
    start = time.time()
    while True:
        allBots = open("SuperBotsTEST.txt", "r")
        botString = allBots.read()
        botList = botString.split("\n\n")
        allBots.close()
        remainBots = []
        for i in range(minNumGamesEachBotPlays):
            bot1 = random.choice(botList)
            
            bot2 = random.choice(botList)
            while bot2 == bot1:
                bot2 = random.choice(botList)
            
            bot3 = bot2
            while bot3 == bot2 or bot3 == bot1:
                bot3 = random.choice(botList)
            bot4 = bot2
            while bot4 == bot2 or bot4 == bot3 or bot4 == bot1:
                bot4 = random.choice(botList)

            botsPlaying = [bot1, bot2, bot3, bot4]
            gamePlayed = game.localGame()
            updatedBots = gamePlayed.play_game(botsPlaying)
            botList[botList.index(bot1)] = updatedBots[0]
            botList[botList.index(bot2)] = updatedBots[1]
            botList[botList.index(bot3)] = updatedBots[2]
            botList[botList.index(bot4)] = updatedBots[3]

        
        updatedSuper = sorted(botList, key=lambda score: eval(score.split("@")[1]), reverse = True)
        #print botList
        allBotsUpdate = open("SuperBotsTEST.txt", "w")
        writeString = "\n\n".join(updatedSuper)
        allBotsUpdate.write(writeString)
        allBotsUpdate.close()
                
        #Once enough bots are added, the random can come out and the database can monitor itself for top 50 percent

        iterations += 1
        if (iterations % 100 == 0):
            print "Num Bots tested: ", iterations
            print " Time (seconds) Elapsed: ", time.time() - start

        
def main():
    testYourMight()


main()
