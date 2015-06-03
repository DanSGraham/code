#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################
#
# HAL10000
#
########################################################################

import random
import copy
from math import *
from vinAStar import *

#Two ais, tree search and fsa

"""Information the AI needs:
    distance to all things can be calculated for each.
    Path to all can be calculated from position"""

class AI:
    """Pure AWESOME A.I, you may DEFINITELY use it to win ;-)"""
    def __init__(self):
        pass

    def process(self, game):
        """Do whatever you need with the Game object game"""
        self.game = game


    
    def printMap(self):
        """Prints out an easier to read map of the game state"""
        for line in self.game.board_map:
            print line

    def simpleDistanceTo(self,startingPos,endingPos):
        """calculates the euclidian distance from the y,x tuples, startingPos to endingPos"""
        
        distance = float(((endingPos[0] - startingPos[0])**2 + (endingPos[1] - startingPos[1])**2)**.5)
        
        return distance

    def manDistanceTo(self, startingPos, endingPos):
        """calculates the Manhattan distance from y,x tuples, startingPos to endingPos"""

        distance = abs(startingPos[0] - endingPos[0]) + abs(startingPos[1] - endingPos[1])

        return distance

    def pathDistanceTo(self, startingPos, endingPos):
        """calulates the distance the hero must travel to reach the ending pos using pathTo"""

        pathArray = self.pathTo(startingPos, [endingPos])
        if pathArray == None:
            return 9999999
        return len(self.pathTo(startingPos, [endingPos]))
        

    def calcAction(self,startingPos,endingPos):
        #This method seems unnecessary......
        """calculate the direction needed to go from (y,x) tuples startingPos to endingPos.
           if the positions are the same, you should issue the Stay command
           if they positions are not cardinal neighbors it is an error and you should return the Stay command
           Otherwise, return North,South,East,West as appropriate
        """
        
        if endingPos[0] == startingPos[0]:
            if endingPos[1] == (startingPos[1] + 1):
                return "East"
            elif endingPos[1] == (startingPos[1] - 1):
                return "West"
        elif endingPos[1] == startingPos[1]:
            if endingPos[0] == (startingPos[0] - 1):
                return "North"
            elif endingPos[0] == (startingPos[0] + 1):
                return "South"
            
        return "Stay"

    
    def canPassThrough(self,position):
        #This method is copied in vinAStar and slightly modified to allow the ending node to be pass throughable.
        
        """Is it possible to pass through this the (y,x) position stored in position?
           Returns False if there is anything in that position (mountain, mine, tavern, other heroes
            Returns True if there is nothing there.  Note a hero can pass through themself.

            Also Note: Any position that is not on the board should be deemed as impassible as well
        """
        #The only time the hero can move to a place is when the place is within the board, and either a blank space (" ") or herself (indicated by self.pos).
        if position[0] >= 0 and position[1] >= 0 and position[0] < self.game.board_size and (position[1]) < self.game.board_size and \
           (self.game.board_map[position[0]][position[1]] == " " or self.game.board_map[position[0]][position[1]] == "X" or position in self.game.heroes_locs):
            return True
        else:
            return False


    def findClosestEnemy(self):
        """Need someone to kill?  return the closest enemy hero (using Euclidian distance)"""
        
        currEnemyHero = None
        for poHero in self.game.heroes:
            if poHero.pos != self.game.hero.pos:
                if currEnemyHero == None:
                    currEnemyHero = poHero
                else:
                    testDistance = self.simpleDistanceTo(self.game.hero.pos, poHero.pos)
                    if testDistance < self.simpleDistanceTo(self.game.hero.pos, currEnemyHero.pos):
                        currEnemyHero = poHero
                        
        return currEnemyHero

    def findClosestPathEnemy(self):
        """Finds the closest enemy hero based on path length"""
        

    def findClosestEnemyNotAtTavern(self):
        """Returns the closest hero not currently at a tavern"""

        currEnemyHero = None       
        for poHero in self.game.heroes:
            if poHero.pos != self.game.heroes and not self.heroAtTavern(hero):
                if currEnemyHero == None:
                    currEnemyHero = poHero
                else:
                    testDistance = self.simpleDistanceTo(self.game.hero.pos, poHero.pos)
                    if testDistance < self.simpleDistanceTo(self.game.hero.pos, currEnemyHero.pos):
                        currEnemyHero = poHero
                        
        return currEnemyHero   

    def findMaxEarningHero(self):
        """who ever is earning the most is a worthwhile target to kill.
           This function returns the person with the most mines.
           Note, you can return your own hero
        """
        
        currMaxEarningHero = None
        for poHero in self.game.heroes:
            if currMaxEarningHero == None:
                currMaxEarningHero = poHero
            else:
                if poHero.mine_count > currMaxEarningHero.mine_count:
                    currMaxEarningHero = poHero
                    
        return currMaxEarningHero

    def findLowestHealthHero(self):
        """Returns the hero with the lowest health.
            Note: May return self."""

        lowestHealthHero = self.game.hero
        
        for poHero in self.game.heroes:
            if poHero.life < lowestHealthHero.life:
                lowestHealthHero = poHero
                
        return lowestHealthHero

    def findEnemyWithMostGold(self):
        """Returns the hero with the most gold. May be own hero"""

        highestGoldHero = self.game.hero

        for poHero in self.game.heroes:
            if poHero.gold > highestGoldHero:
                highestGoldHero = poHero
                
        return highestGoldHero

    def findClosestTavern(self):
        """the only brew for the brave and true comes from the Green Dragon! Use this function to find a brew!"""
        
        closestTavern = None
        for tavernLocation in self.game.taverns_locs:
            if closestTavern == None:
                closestTavern = tavernLocation
            else:
                if simpleDistanceTo(self.game.hero.pos, tavernLocation) < simpleDistanceTo(self.game.hero.pos, tavernLocation):
                    closestTavern = tavernLocation
                    
        return closestTavern

            
    def findClosestMine(self):
        """returns the position of the closest mine (using euclidian distance)
        Note: Can return a mine owned by your hero"""

        currClosestMine = self.game.mines_locs[0]

        for poMine in self.game.mine_locs:
            if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestMine):
                currClosestMine = poMine
                
        return currClosestMine


    def findClosestOwnMine(self):
        """Returns the position of the your closest mine"""

        currClosestOwnMine = None
        if self.game.hero.mine_count > 0:
            currClosestOwnMine = self.game.hero.mines[0]
            for poMine in self.game.hero.mines:
                if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestOwnMine):
                    currClosestMine = poMine
                    
        return currClosestOwnMine

    def findClosestEnemyMine(self):
        """Returns the position of the closest enemy Mine"""
        
        currClosestEnemyMine = None
        for poMine in self.game.mines_locs:
            if not poMine in self.game.hero.mines:
                if currClosestEnemyMine == None:
                    currClosestEnemyMine = poMine
                else:
                    if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestEnemyMine):
                        currClosestEnemyMine = poMine
                        
        return currClosesetEnemyMine
            
    def findClosestSpecificEnemyMine(self, specificHero):
        """Returns the position of the closest mine to a specific hero"""
        
        currClosestHeroMine = None
        if specificHero.mine_count > 1:
            print specificHero.mine_count
            print specificHero.mines
            currClosestHeroMine = specificHero.mines[0]
            for poMine in specificHero.mines:
                if self.simpleDistanceTo(self.game.hero.pos, poMine) < self.simpleDistanceTo(self.game.hero.pos, currClosestHeroMine):
                    currClosestHeroMine = poMine
                    
        return currClosestHeroMine
        
    def heroDistanceToSpawnPoint(self):
        """Returns the distance of your hero to the spawn Point"""
        return self.simpleDistanceTo(self.game.hero.pos,self.game.hero.spawn_pos)

    def getCardinalCoordinates(self, startingCoord):
        """Returns a list of the cardinal coordinates of the startingCoord in the order [North, East, South, West]"""
        north = (startingCoord[0] - 1, startingCoord[1])
        east = (startingCoord[0], startingCoord[1] + 1)
        south = (startingCoord[0] + 1, startingCoord[1])
        west = (startingCoord[0], startingCoord[1] - 1)
        return [north, east, south, west]
    
    def pathTo(self, startingCoordinates, endCoordinates):
        """Returns the shortest path to the end coordinates using A* search. Hueristic is the euclidian distance."""
        #Unsure if the path must start with the startingCoordinate or if it can start with the first move.
        aStarSearch = AStar(self.game.board_map, startingCoordinates, endCoordinates)
        pathEnd = aStarSearch.calcPath()
        if pathEnd == None:
            return None
        return pathEnd.getRPath([])[::-1]
                    
        
    def noDamagePathTo(self, startingCoordinates, endingCoordinates):
        """Returns a path that does not go near opponents"""
        pass            
        
        
    def attackHero(self, heroToAttack):
        """Returns a path to attack a hero in it's current state."""
        return pathTo(self.game.hero.pos, [heroToAttack.pos])

    def goToNearestTavern(self):
        """Returns a path to the nearest available tavern"""
        return pathTo(self.game.hero.pos, self.game.taverns_locs)
        
    def nearestUninterruptedTavern(self):
        """Returns the closest tavern the hero can reach without other players reaching them first."""

    def goToClosestMine(self):
        """Returns the closest available mine. May be useful to lure a hero towards a mine which may then deplete their health for me to then attack"""
        return pathTo(self.game.hero.pos, self.game.mines_locs)

    def goToNearestEnemyMine(self):
        """returns the nearest enemy controlled mine"""
        enemyMines = []
        for poMine in self.game.mines:
            if not poMine in self.game.hero.mines:
                enemyMines.append(poMine)
        pathTo(self.game.hero.pos, enemyMines)
    
    def goToNearestSpecificEnemyMine(self, hero):
        """returns the nearest mine of a specific hero"""
        pathTo(self.game.hero.pos, hero.mines)

    def heroWithLowestScore(self):
        """returns the position of the hero with the lowest score"""
        lowestHero = self.game.hero
        for poHero in self.game.heroes:
            if poHero.gold < lowestHero.gold:
                lowestHero = poHero
        return lowestHero.pos
    
    def heroAtTavern(self, hero):
        """determines if a hero is at a tavern currently"""

        tavernPatronPositions = []
        for tavernLoc in self.game.taverns_locs:
            tavernEarners = self.getCardinalCoordinates(tavernLoc)
            tavernPatronPositions += tavernEarners

        return hero.pos in tavernPatronPositions
        

    def runFromHeroes(self):
        """Moves away from adjacent heroes. Not smart, but it works."""
        possibleMoves = self.getCardinalCoordinates(self.game.hero.pos)
        for poMove in possibleMoves:
            if self.canPassThrough(poMove):
                return [self.game.hero.pos] + [poMove]
            
        return [self.game.hero.pos]

    def getHeroHealth(self, heroWantHealth):
        """Returns the health of the desired hero"""
        return heroWantHealth.life


    def orderHerosByDistance(self):
        heroList = []
        ownPosition = self.game.hero.pos
        for pHero in self.game.heroes:
            if pHero.pos != ownPosition:
                if len(heroList) == 0:
                    heroList.append(pHero)
                else:
                    for i in range(len(heroList)):
                        if self.pathDistanceTo(ownPosition, pHero.pos) < self.pathDistanceTo(ownPosition, heroList[i].pos):
                            heroList.insert(i, pHero)
                            break
                    if not pHero in heroList:
                        heroList.append(pHero)
        return heroList

    def orderTavernsByDistance(self):
        tavernList = []
        ownPosition = self.game.hero.pos
        for pTav in self.game.taverns_locs:
            if len(tavernList) == 0:
                tavernList.append(pTav)
            else:
                for i in range(len(tavernList)):
                    if self.pathDistanceTo(ownPosition, pTav) < self.pathDistanceTo(ownPosition, tavernList[i]):
                        tavernList.insert(i, pTav)
                        break
                if not pTav in tavernList:
                    tavernList.append(pTav)

            if len(tavernList) >= 4:
                tavernList = tavernList[0:4]
        return tavernList

    def orderUnownedMinesByDistance(self):
        mineList = []
        ownPosition = self.game.hero.pos
        for pMine in self.game.mines_locs:
                                
            if not pMine in self.game.hero.mines:
                if len(mineList) == 0:
                    mineList.append(pMine)
                else:
                    if not pMine in mineList:
                        for i in range(len(mineList)):
                            if self.pathDistanceTo(ownPosition, pMine) < self.pathDistanceTo(ownPosition, mineList[i]):
                                mineList.insert(i, pMine)
                                break
                        if not pMine in mineList:
                            mineList.append(pMine)
            if len(mineList) >= 4:
                mineList = mineList[0:4]
                
        return mineList
            

    def createInputs(self, numInputs):
        #When classifying using only ownHero information, the error lowers until a plateau, what one would expect. Now trying to add more data to classify.
        """returns a list of numbers to represent the inputs to each of the neurons in the Neural Network"""
        """List of inputs:
            Distance to closest hero
            difference in mines
            difference in gold
            difference in life
            repeat for next closest hero and so on
            distance to closest mine
            distance to closest mine owned by enemy with most mines
            distance to closest mine owned by enemy with most gold
            distance to closest tavern
            """
        
        inputList = []
        ownHero = self.game.hero
        orderHeros = self.orderHerosByDistance()
        orderTaverns = self.orderTavernsByDistance()
        orderMines = self.orderUnownedMinesByDistance()
        
        inputList.append(ownHero.life / float(100))
        inputList.append(ownHero.gold / float(10000))
        if ownHero.pos == ownHero.spawn_pos:
            inputList.append(1)
        else:
            inputList.append(0)
            
        inputList.append(ownHero.mine_count / float(len(self.game.mines)))
        if self.heroAtTavern(ownHero):
            inputList.append(1)
        else:
            inputList.append(0)
            
        mineRank = 1
        goldRank = 1
        healthRank = 1
        
        for pHero in orderHeros:
            if pHero.mine_count > ownHero.mine_count:
                mineRank += 1
            if pHero.gold > ownHero.gold:
                goldRank += 1
            if pHero.life > ownHero.life:
                healthRank += 1
                
        inputList.append(mineRank / 4.0)
        inputList.append(goldRank / 4.0)
        inputList.append(healthRank / 4.0)
        
        #pHero = None
        for pHero in orderHeros:
            inputList.append(self.pathDistanceTo(ownHero.pos, pHero.pos))
            inputList.append(pHero.life / float(100))
            inputList.append((ownHero.life - pHero.life) / float(100))
            inputList.append(pHero.gold / float(10000))
            inputList.append((ownHero.gold - pHero.gold) / float(10000))
            
            if pHero.pos == pHero.spawn_pos:
                inputList.append(1)
            else:
                inputList.append(0)

            #THERE SEEMS TO BE AN ISSUE GETTING pHero.mines. 
            #inputList.append(pHero.mine_count / float(len(self.game.mines)))
            inputList.append((pHero.mine_count - ownHero.mine_count) / float(len(self.game.mines)))
            #if pHero.mine_count >= 1:
            #    inputList.append(self.pathDistanceTo(ownHero.pos, self.findClosestSpecificEnemyMine(pHero)))
            #else:
            #    inputList.append(self.game.board_size * 2)
                
            if self.heroAtTavern(pHero):
               inputList.append(1)
            else:
                inputList.append(0)
            
            minesAdded = 0
            for pMine in orderMines:
                inputList.append(self.pathDistanceTo(pHero.pos, pMine))
                minesAdded += 1
            while minesAdded < 4:
                inputList.append(self.game.board_size * 2)
                minesAdded += 1


            mineRank = 1
            goldRank = 1
            healthRank = 1
                             
            for pHero1 in self.game.heroes:
                if pHero1.pos != pHero.pos:
                    if pHero1.mine_count > pHero.mine_count:
                        mineRank += 1
                    if pHero1.gold > pHero.gold:
                        goldRank += 1
                    if pHero1.life > pHero.life:
                        healthRank += 1
                
            inputList.append(mineRank / 4.0)
            inputList.append(goldRank / 4.0)
            inputList.append(healthRank / 4.0)

        
        minesAdded = 0
        for pMine in orderMines:
            inputList.append(self.pathDistanceTo(ownHero.pos, pMine))
            
            for pHero in orderHeros:
                if pMine in pHero.mines:
                    inputList.append(pHero.mine_count)
                else:
                    inputList.append(0)
                    
                #inputList.append(self.pathDistanceTo(pHero.pos, pMine))
                if pHero.pos in self.getCardinalCoordinates(pMine):
                    inputList.append(1)
                else:
                    inputList.append(0)
                    
            minesAdded += 1
        while minesAdded < 4:
            for i in range(7):
                inputList.append(self.game.board_size*2)

            minesAdded += 1
            
        for pTavern in orderTaverns:
            inputList.append(self.pathDistanceTo(ownHero.pos, pTavern))
            for pHero in orderHeros:
                if pHero.pos in self.getCardinalCoordinates(pTavern):
                    inputList.append(1)
                else:
                    inputList.append(0)

        


##        print "Pre add large size"
##        print len(inputList)
        x = len(inputList)
        for i in range(numInputs - x):
            inputList.append(self.game.board_size*2)

##        print "Len Mines:"
##        print len(orderMines)
##        print "Len taverns"
##        print len(orderTaverns)
##        print "len Heros"
##        print len(orderHeros)
##        print len(inputList)
        #print inputList
        return inputList
        

    def determineClass(self, classes, destPoint):
        """returns the class the destPoint belongs to. The return value will be a number from 0 up to classes."""
        #self.printMap()
        #print self.game.hero.mines
        classVal = 0
        ownPosition = self.game.hero.pos
        #distOfPoint = self.pathDistanceTo(ownPosition, destPoint)

        """all ordered by location"""
        orderHeros = self.orderHerosByDistance()
        
##        print "Hero Position"
##        print ownPosition
##
##        print "Hero Positions"
##        for ptHero in orderHeros:
##            print ptHero.pos
##            print self.pathDistanceTo(ownPosition, ptHero.pos)
##
##        print "Tavern Position"
##        print orderTaverns
##        for t in orderTaverns:
##            print self.pathDistanceTo(ownPosition, t)
##
##        print "Mine Positions"
##        print orderMines
##        for m in orderMines:
##            print self.pathDistanceTo(ownPosition, m)
        #print "Hero Positions"
        for pHero in orderHeros:
            #print pHero.pos
            if destPoint == pHero.pos:
                return classVal
            #else:
                classVal += 1

        orderMines = self.orderUnownedMinesByDistance()
        #print "Mine Positions"
        #print orderMines
        for minePos in orderMines:
            #print minePos
            if destPoint == minePos:
                return classVal
            else:
                classVal += 1

        orderTaverns = self.orderTavernsByDistance()
        classVal = 7
        #print "Tavern Positions"
        for tavernPos in orderTaverns:
            #print tavernPos
            if destPoint == tavernPos:
                return classVal
            else:
                classVal += 1

        

        return """CLASS VAL ERROR"""


    def classInverse(self, classNum):
        orderHeros = self.orderHerosByDistance()
        orderTaverns = self.orderTavernsByDistance()
        orderMines = self.orderUnownedMinesByDistance()

        heroPositions = []
        for pHero in orderHeros:
            heroPositions.append(pHero.pos)
        possOutputs = heroPositions
        mineNum = len(orderMines)
        for i in range(4 - mineNum):
            orderMines.append("ERROR")
            
        possOutputs += orderMines
        possOutputs += orderTaverns

        return possOutputs[classNum]



    def respawn(heroToRespawn, heroesList, self):
        heroToRespawn.pos = hero.spawn_pos
        heroToRespawn.life = 100
        heroToRespawn.mines = []
        heroToRespawn.mine_count = 0
        spawnToCheck = hero.spawn_pos
        for hero in heroesList:
            if hero.pos == spawnToCheck:
                hero.pos = hero.spawn_pos
                hero.life = 100
                hero.mines = []
                hero.mine_count = 0
                self.respawn(hero, heroesList)
                break
    
    def recDetNextBoard(currentBoard, depthLeft, qualitySearching, bestOptionValue, heroToSearchInt, heroesList, self):
        #Searches the depth until it runs out then returns the best possible value it discovered on that branch.
        if depthLeft == 0:
            return bestOptionValue
        else:
            heroToSearchInt = heroToSearchInt % len(self.game.heroes)
            currHero = copy.deepcopy(heroesList[heroToSearchInt])
            possibleMoves = self.getCardinalCoordinates(currHero.pos) + [currHero.pos]
            for pMove in possibleMoves:
                nextBoard = currentBoard
                if self.canPassThrough(pMove):
                    if currHero.pos in self.game.spawn_points_locs:
                        nextBoard[currHeroPos[0]][currHeroPos[1]] = "X"
                    else:
                        nextBoard[currHeroPos[0]][currHeroPos[1]] = " "
                    currHero.pos = pMove
                    nextBoard[pMove[0]][pMove[1]] = "H"
                    
                if nextBoard[pMove[0]][pMove[1]] == "T":
                    if currHero.gold >= 2:
                        currHero.gold -= 2
                        currHero.life += 50
                        if currHero.life > 100:
                            currHero.life = 100

                if nextBoard[pMove[0]][pMove[1]] == "$":
                    if pMove not in currHero.mines:
                        currHero.life -= 20
                        if currHero.life > 0:
                            currHero.mines.append(pMove)
                            currHero.mine_count += 1
                            for pHero in heroesList:
                                if pMove in pHero.mines:
                                    pHero.mines.remove(pMove)
                                    pHero.mine_count -= 1
                            nextBoard = currentBoard
                        else:
                            self.respawn(currHero, heroesList)
                            nextBoard = self.game.board_map
                            for p2Hero in heroesList:
                                nextBoard[p2Hero.pos[0]][p2Hero.pos[1]] = "H"
                                                        
                adjSpace = self.getCardinalCoordinates(currHero.pos)
                for pHero in heroesList:
                    if pHero.pos in adjSpace:
                        pHero.life -= 20
                        if pHero.life < 0:
                            currHero.mines += pHero.mines
                            currHero.mine_count += pHero.mine_count
                            self.respawn(pHero, heroesList)

                currHero.gold += currHero.mine_count

                if currHero.life > 1:
                    currHero.life -= 1

                #Recursive call now!

                #TURN OVER NEED TO CALL THE METHOD AGAIN!

            

            
                            
                        
        
    def determineNextBoard(currentBoard, self)
    # A method to return the next board.
    # Depth search seems best. Two possible methods. One is to store information so that I can lookup that information instead of recalculating everytime. Another way is to solve recursively storing the best possible option thus far.
    def decide(self):
        """Must return a tuple containing in that order:
          1 - path_to_goal :
                  A list of coordinates representing the path to your
                 bot's goal for this turn:
                 - i.e: [(y, x) , (y, x), (y, x)]
                 where y is the vertical position from top and x the
                 horizontal position from left.

          2 - action:
                 A string that will be displayed in the 'Action' place.
                 - i.e: "Go to mine"

          3 - decision:
                 A list of tuples containing what would be useful to understand
                 the choice you're bot has made and that will be printed
                 at the 'Decision' place.

          4- hero_move:
                 A string in one of the following: West, East, North,
                 South, Stay

          5 - nearest_enemy_pos:
                 A tuple containing the nearest enemy position (see above)

          6 - nearest_mine_pos:
                 A tuple containing the nearest mine position (see above)

          7 - nearest_tavern_pos:
                 A tuple containing the nearest tavern position (see above)"""

        actions = ['mine', 'tavern', 'fight']

        decisions = {'mine': [("Mine", 30), ('Fight', 10), ('Tavern', 5)],
                    'tavern': [("Mine", 10), ('Fight', 10), ('Tavern', 50)],
                    'fight': [("Mine", 15), ('Fight', 30), ('Tavern', 10)]}

        walkable = []
        path_to_goal = []
        dirs = ["North", "East", "South", "West", "Stay"]

        for y in range(self.game.board_size):
            for x in range(self.game.board_size):
                if (y, x) not in self.game.walls_locs or \
                        (y, x) not in self.game.taverns_locs or \
                        (y, x) not in self.game.mines_locs:

                    walkable.append((y, x))

        # With such a random path, path highlighting would
        # display a random continuous line of red bullets over the map.
        first_cell = self.game.hero.pos
        path_to_goal.append(first_cell)

        for i in range(int(round(random.random()*self.game.board_size))):
            for i in range(len(walkable)):
                random.shuffle(walkable)
                if (walkable[i][0] - first_cell[0] == 1 and
                        walkable[i][1] - first_cell[1] == 0) or \
                        (walkable[i][1] - first_cell[1] == 1 and
                        walkable[i][0] - first_cell[0] == 0):
                    path_to_goal.append(walkable[i])
                    first_cell = walkable[i]
                    break

        hero_move = random.choice(dirs)
        action = random.choice(actions)
        decision = decisions[action]
        nearest_enemy_pos = random.choice(self.game.heroes).pos
        nearest_mine_pos = random.choice(self.game.mines_locs)
        nearest_tavern_pos = random.choice(self.game.mines_locs)

        return (path_to_goal,
                action,
                decision,
                hero_move,
                nearest_enemy_pos,
                nearest_mine_pos,
                nearest_tavern_pos)


if __name__ == "__main__":
    
    pass
