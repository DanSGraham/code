import duelgame
import random
import azkaban
from graphics import *

from randomwizard import RandomWizard
from scaredywizard import ScaredyWizard
from DanielGraham_wizard2 import DanielGrahamWizard1
from DanielGraham_wizard3 import  DanielGrahamWizard


def main():
    wizardsOfOz = [RandomWizard(),ScaredyWizard(), DanielGrahamWizard1()]
    wizardsSlytherin = [DanielGrahamWizard()]
    
    wizards = wizardsSlytherin + wizardsOfOz
    
    duelgame.DELAY_FACTOR = .1    #larger=slower, smaller=faster
    numRounds = 80  # you can change the max number of rounds
    numDuels  = 100
    winningTable = {} # keep track of how many wins each wizard has
    for w in wizards:
        winningTable[w.getName()] = 0
    
    scoreWindow = GraphWin("The Score Board:", 200,200)
    scoreWindow.setCoords(-1,-1,1,1)
    scoreText = Text(Point(0,0), "No scores yet")
    scoreText.draw(scoreWindow)
    
    for i in range(numDuels):
        random.shuffle(wizards)
        winners = duelgame.doFullDuel(wizards,numRounds) 
        if azkaban.screen(winners): # can't be too careful...
            # if wizards tie, they share the victory point among them.
            for w in winners:
                winningTable[w.getName()] = winningTable[w.getName()] + 1.0 / len(winners)
            
            scorePairs = winningTable.items() #list of tuples of the form: [('name1', score1), ('name2', 'score2')]
            scorePairs.sort(key=(lambda x: x[1]), reverse=True) # sort by the score item ([1]) of each tuple
            sText = ""
            for pair in scorePairs:
                sText  = sText + pair[0] + ": " + "%.2f"%pair[1] + "\n"
            scoreText.setText(sText)
            print sText + "\n"
   
    scoreWindow.getMouse()
    scoreWindow.close()
    
if __name__ == '__main__':
    main()
    
    
