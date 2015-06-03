#A program to find the best Bot MORTAL KOMBOT
#By Daniel Graham

import game
import fsmMaker
import fsmAI
import random
import time

maxStatementSize = 3
minNumGamesEachBotPlays = 3
minimumAllowedWinRatio = .5


        
def testYourMight():
    #method to pit each bot against three other random bots from the list and determine a winner. Then record that value and remove the bad ones.
    iterations = 0
    start = time.time()
    while True:
        allBots = open("SuperBots1.txt", "r")
        botString = allBots.read()
        botList = botString.split("\n\n")
        allBots.close()
        remainBots = []
        sortedList = sorted(botList, key=lambda score: eval(score.split("@")[1]), reverse = True)
        for j in range(2):
            pNewBot = sortedList[j]
            newBotLines = pNewBot.split("\n")
            newPLine = fsmMaker.makeNewLine(maxStatementSize)
            for k in range(len(newBotLines)):
                newBotLines.insert(k, newPLine)
                newBotLines[len(newBotLines) - 1] = newBotLines[len(newBotLines) - 1].split("@")[0]
                newBotLines[len(newBotLines) - 1] += "@0.0/0.0"
                botToTest = "\n".join(newBotLines)
                for i in range(minNumGamesEachBotPlays):

                    bot2 = sortedList[0]
                    
                    bot3 = bot2
                    while bot3 == bot2:
                        bot3 = sortedList[1]
                    bot4 = bot2
                    while bot4 == bot2 or bot4 == bot3:
                        bot4 = random.choice(sortedList)

                    botsPlaying = [botToTest, bot2, bot3, bot4]
                    gamePlayed = game.localGame()
                    updatedBots = gamePlayed.play_game(botsPlaying)
                    sortedList[sortedList.index(bot2)] = updatedBots[1]
                    sortedList[sortedList.index(bot3)] = updatedBots[2]
                    sortedList[sortedList.index(bot4)] = updatedBots[3]
                    botToTest = updatedBots[0]

        
                if eval(botToTest.split("@")[1]) >= minimumAllowedWinRatio:
                    sortedList.append(botToTest)
                    print "Added new bot! One more step on the path to world domination"
                newBotLines.pop(k)

        updatedSuper = []    
        for m in range(len(sortedList)):
            if m < 7:
                updatedSuper.append(sortedList[m])
            else:
                if eval(sortedList[m].split("@")[1]) >= minimumAllowedWinRatio:
                    updatedSuper.append(sortedList[m])

        #print botList
        allBotsUpdate = open("SuperBots1.txt", "w")
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
