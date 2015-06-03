#!/usr/bin/env python
# -*- coding: utf-8 -*-


import boardCreation
from random import *
from vinAStar import *
from vinNode import *
import fsmAI
import ast
#import localBot

class Hero:
    """The Hero object"""
    def __init__(self, hero):
        try:
            # Training bots have no elo or userId
            self.elo = hero['elo']
            self.user_id = hero['userId']
            self.bot_last_move = hero['lastDir']
        except KeyError:
            self.elo = 0
            self.user_id = 0
            self.last_move = None

        self.bot_id = hero['id']
        self.life = hero['life']
        self.gold = hero['gold']
        self.pos = (hero['pos']['x'], hero['pos']['y'])
        self.spawn_pos = (hero['spawnPos']['x'], hero['spawnPos']['y'])
        self.crashed = hero['crashed']
        self.mine_count = hero['mineCount']
        self.mines = []
        self.name = hero['name'].encode("utf-8")

class localHero:
    """The Local Hero object"""
    def __init__(self, heroString):
        
        self.bot_id = heroString
        self.life = 100
        self.gold = 0
        self.pos = None
        self.spawn_pos = None
        #self.crashed = hero['crashed']
        self.mine_count = 0
        self.mines = []
        #Hero name will hold the key to the hero ai
        self.totalWins = None
        self.gamesPlayed = None
        self.name = heroString

class localGame:
    """The game object that gather
    all game state informations"""
    def __init__(self):
        #self.mines = {}
        self.mines_locs = []
        self.spawn_points_locs = []
        self.taverns_locs = []
        self.hero = None
        self.heroes = []
        self.heroes_locs = []
        self.walls_locs = []
        self.turn = None
        self.max_turns = None
        self.finished = None
        self.board_size = None
        self.board_map = []


    def local_process_textBoard(self, boardIndex):
        #takes the boardIndex board from the text document and processes that board.
        openFile = open("RandomGameBoards.txt", "r")
        fullFile = openFile.read()
        openFile.close()
        currIndex = 0
        endIndex = fullFile.find(")\n", currIndex)
        for i in range(boardIndex):
            currIndex = endIndex + 1
            endIndex = fullFile.find(")\n", currIndex)
            
        boardInfo = fullFile[currIndex:endIndex + 1]
        startInfo = boardInfo.find("(")
        boardMap = boardInfo[:startInfo-1].split("\n")
        self.board_map = boardMap
        infoString = boardInfo[startInfo:]
        #print infoString
        start = infoString.find("[")
        end = infoString.find("]", start)
        #print infoString[start:end + 1]
        mineArray = ast.literal_eval(infoString[start:end + 1])
        self.mines_locs = mineArray
        start = infoString.find("[", end)
        end = infoString.find("]", start)
        #print infoString[start:end + 1]
        spawnArray = ast.literal_eval(infoString[start:end + 1])
        self.spawn_points_locs = spawnArray
        start = infoString.find("[", end)
        end = infoString.find("]", start)
        tavernArray = ast.literal_eval(infoString[start:end + 1])
        self.taverns_locs = tavernArray
        start = infoString.find("[", end)
        end = infoString.find("]", start)
        heroArray = ast.literal_eval(infoString[start:end + 1])
        self.heroes_locs = heroArray
        for i in range(len(heroArray)):
            self.heroes[i].pos = heroArray[i]
            self.heroes[i].spawn_pos = heroArray[i]
            #print heroArray[i]
        start = infoString.find("[", end)
        end = infoString.find("]", start)
        wallArray = ast.literal_eval(infoString[start:end + 1])
        self.walls_locs = wallArray
        start = infoString.find(",", end)
        end = infoString.find(")", start)
        self.board_size = int(infoString[start + 1:end ])
        
    def local_process_board(self, boardMap):
        #takes the boardIndex board from the text document and processes that board.
        
        self.board_size = len(boardMap)
        map_line = ""
        newBoard = []
        char = None
        heroSpawn = 0
        for y in range(len(boardMap)):
            line = boardMap[y]
            newLine = ""
            for x in range(1, len(boardMap) * 2, 2):
                if line[x] == " " or line[x] == "#":
                    newLine += line[x]
                    if line[x] == "#":
                        self.walls_locs.append((y, x/2))
                        
                elif line[x] == "]":
                    newLine += "T"
                    self.taverns_locs.append((y, x / 2))
                    
                elif line[x] == "-":
                    self.mines_locs.append((y, x / 2))
                    #self.mines.append((y, x / 2))
                    newLine += "$"
                else:
                    self.heroes[int(line[x]) - 1].spawn_pos = (y, x / 2)
                    self.heroes[int(line[x]) - 1].pos = (y, x / 2)
                    self.heroes_locs.append((y, x / 2))
                    self.spawn_points_locs.append((y, x / 2))
                    newLine += "H"
                    
            newBoard.append(newLine)
            
        self.board_map = newBoard
            
                    
    def local_process_heroes(self, heroes):
        for pHero in heroes:
            heroToAdd = localHero(pHero)
            self.heroes.append(heroToAdd)

    def respawn(self,heroToRespawn):
        respawnList = []
        for tHero in self.heroes:
            if tHero.pos != heroToRespawn.pos:
                respawnList.append(tHero)
                
        respawnPIndex = self.heroes_locs.index(heroToRespawn.pos)
        self.heroes_locs.remove(heroToRespawn.pos)
        if heroToRespawn.pos not in self.spawn_points_locs:
            updateList = list(self.board_map[heroToRespawn.pos[0]])
            updateList[heroToRespawn.pos[1]] = " "
            self.board_map[heroToRespawn.pos[0]] = "".join(updateList)
        else:
            updateList = list(self.board_map[heroToRespawn.pos[0]])
            updateList[heroToRespawn.pos[1]] = "X"
            self.board_map[heroToRespawn.pos[0]] = "".join(updateList)

        print  "RESPAWN DATA"
        print "CURRENT POSITION"
        print heroToRespawn.pos
        print heroToRespawn.spawn_pos
        heroToRespawn.pos = heroToRespawn.spawn_pos
        updateList = list(self.board_map[heroToRespawn.pos[0]])
        updateList[heroToRespawn.pos[1]] = "H"
        self.board_map[heroToRespawn.pos[0]] = "".join(updateList)
        self.heroes_locs.insert(respawnPIndex, heroToRespawn.pos)
        heroToRespawn.life = 100
        heroToRespawn.mines = []
        heroToRespawn.mine_count = 0
        spawnToCheck = heroToRespawn.spawn_pos
        for pHero in respawnList:
            if pHero.pos == spawnToCheck:
                self.respawn(pHero)
                break
    
    def play_turn(self, aiToPlay):
        
        for i in range(len(self.heroes)):
            self.hero = self.heroes[i]
            aiToPlay.process(self)
            aiToPlay.printMap()
            heroesList = self.heroes
            nextMove = aiToPlay.decide()[0]
            print "Hero info and next Move"
            print "Hero pos: " + str(self.hero.pos)
            print "Hero mine: " + str(self.hero.mines)
            print "Hero life: " + str(self.hero.life)
            print "Hero gold: " + str(self.hero.gold)
            print "Other Heros " + str(heroesList)
            print nextMove
            print self.taverns_locs
            currHero = self.hero
            nextBoard = self.board_map
            hero_loc_index = self.heroes_locs.index(self.hero.pos)
            self.heroes_locs.remove(self.hero.pos)
            if nextMove not in self.taverns_locs \
               and nextMove not in self.mines_locs \
               and nextMove not in self.heroes_locs:
                
                if currHero.pos in self.spawn_points_locs:
                    updateList = list(nextBoard[currHero.pos[0]])
                    updateList[currHero.pos[1]] = "X"
                    nextBoard[currHero.pos[0]] = "".join(updateList)
                    
                else:
                    updateList = list(nextBoard[currHero.pos[0]])
                    updateList[currHero.pos[1]] = " "
                    nextBoard[currHero.pos[0]] = "".join(updateList)
  
                self.hero.pos = nextMove
                self.heroes_locs.insert(hero_loc_index, nextMove)
                #print currHero.pos[0]
                updateList = list(nextBoard[currHero.pos[0]])
                updateList[currHero.pos[1]] = "H"
                #print currHero.pos[0]
                nextBoard[currHero.pos[0]] = "".join(updateList)
                    
            elif nextBoard[nextMove[0]][nextMove[1]] == "T":
                if currHero.gold >= 2:
                    currHero.gold -= 2
                    currHero.life += 50
                    if currHero.life > 100:
                        currHero.life = 100
                self.heroes_locs.insert(hero_loc_index, self.hero.pos)
                nextBoard = self.board_map
                
            elif nextBoard[nextMove[0]][nextMove[1]] == "$":
                if not nextMove in currHero.mines:
                    currHero.life -= 20
                    if currHero.life > 0:
                        currHero.mines.append(nextMove)
                        currHero.mine_count += 1
                        for pHero in heroesList:
                            if pHero.pos != currHero.pos and nextMove in pHero.mines:
                                pHero.mines.remove(nextMove)
                                pHero.mine_count -= 1
                                
                        nextBoard = self.board_map
                        self.heroes_locs.insert(hero_loc_index, self.hero.pos)
                        
                    else:
                        self.heroes_locs.insert(hero_loc_index, self.hero.pos)
                        self.respawn(currHero)
                else:
                    self.heroes_locs.insert(hero_loc_index, self.hero.pos)
                    nextBoard = self.board_map
            else: #if they move into another hero
                nextBoard = self.board_map
                self.heroes_locs.insert(hero_loc_index, self.hero.pos)

            self.board_map = nextBoard    
            adjSpace = aiToPlay.getCardinalCoordinates(currHero.pos)
            for pHero in heroesList:
                if pHero.pos in adjSpace:
                    pHero.life -= 20
                    if pHero.life < 0:
                        currHero.mines += pHero.mines
                        currHero.mine_count += pHero.mine_count
                        self.respawn(pHero)

            currHero.gold += currHero.mine_count

            if currHero.life > 1:
                currHero.life -= 1
                    
    def play_game(self):
        #Create heroes
        #pick board
        #use one instance of the AI to process all heroes. Ai uses the self.hero.id to determine actions.
        
        brain = fsmAI.AI()
        numTurns = 500
        for i in range(numTurns):
            self.play_turn(brain)
#def getAndMakeHeroes(self):
        #A method to get heroes from a text file and interpret the hero. Then create the appropriate ai.


    def test_game(self):
        heroesForTest = ["a", "b", "c", "d"]
        self.local_process_heroes(heroesForTest)
        self.local_process_textBoard(0)
        brain = fsmAI.AI()
        numTurns = 500
        for i in range(numTurns):
            self.play_turn(brain)
            print "End Turn " + str(i)
            print
        
    def create_random_board(self):
        #Generates 1000 random boards and stores it to a text file
        heroesForTest = ["a", "b", "c", "d"]
        self.local_process_heroes(heroesForTest)
        validBoard = False
        #Creates 1000 random boards
        boardFile = open("randomGameBoards.txt", "a")
        for i in range(1000):
            writeString = ""
            validBoard = False
            while not validBoard:
                self.mines_locs = []
                self.spawn_points_locs = []
                self.taverns_locs = []
                self.heroes_locs = []
                self.walls_locs = []
                self.board_size = None
                self.board_map = []
                boardSize = randint(4, 12) * 2
                mineFreq = randint(1, 25) / 100.0
                borderFreq = randint(1, 25) /  100.0
                validBoard = True
                self.local_process_board(boardCreation.generateFBoard(boardSize, borderFreq, mineFreq))
                if len(self.mines_locs) > 0:
                    for spawn in self.heroes_locs:
                        for loc2 in self.mines_locs:
                            testPath =  AStar(self.board_map, spawn, [loc2]).calcPath()
                            if not testPath:
                                #print "Mine Fail"
                                validBoard = False
                                break
                        if validBoard == False:
                            break
                        for tav in self.taverns_locs:
                            testPath =  AStar(self.board_map, spawn, [tav]).calcPath()
                            if not testPath:
                                #print "Tavern Fail"
                                validBoard = False
                                break
                        if validBoard == False:
                            break
                        for spawn2 in self.heroes_locs:
                            testPath =  AStar(self.board_map, spawn, [spawn2]).calcPath()
                            if not testPath:
                                #print "Spawn Fail"
                                validBoard = False
                                break
                        if validBoard == False:
                            break
                else:
                    validBoard = False

                #print self.board_map
                
            for line in self.board_map:
                writeString += line + "\n"
            
            writeString += "(" + str(self.mines_locs) + "," + str(self.spawn_points_locs) + "," + str(self.taverns_locs) \
                           + "," + str(self.heroes_locs) + "," + str(self.walls_locs) + "," + str(self.board_size) + ")\n"
            boardFile.write(writeString)

            if i % 100 == 0: print str(i) + "/ 1000"
        boardFile.close()    
                    
                    
   # def playTurn(self):
        #Plays a turn of the game by asking each hero what they will do. And encating that.
        #for hero in self.game.heroes:
   
class Game:
    """The game object that gather
    all game state informations"""
    def __init__(self, state):
        self.state = state
        self.mines = {}
        self.mines_locs = []
        self.spawn_points_locs = {}
        self.taverns_locs = []
        self.hero = None
        self.heroes = []
        self.heroes_locs = []
        self.walls_locs = []
        self.url = None
        self.turn = None
        self.max_turns = None
        self.finished = None
        self.board_size = None
        self.board_map = []

        self.process_data(self.state)

    def process_data(self, state):
        """Parse the game state"""
        self.set_url(state['viewUrl'])
        self.process_hero(state['hero'])
        self.process_game(state['game'])

    def set_url(self, url):
        """Set the game object url var"""
        self.url = url

    def process_hero(self, hero):
        """Process the hero data"""
        self.hero = Hero(hero)

    def process_game(self, game):
        """Process the game data"""
        process = {'board': self.process_board,
                    'heroes': self.process_heroes}
        self.turn = game['turn']
        self.max_turns = game['maxTurns']
        self.finished = game['finished']
        for key in game:
            if key in process:
                process[key](game[key])

    def process_board(self, board):
        """Process the board datas
            - Retrieve walls locs, tavern locs
            - Converts tiles in a displayable form"""
        self.board_size = board['size']
        tiles = board['tiles']
        map_line = ""
        char = None
        for y in range(0, len(tiles), self.board_size * 2):
            line = tiles[y:y+self.board_size*2]
            for x in range(0, len(line), 2):
                tile = line[x:x+2]
                tile_coords = (y/self.board_size/2, x/2)
                if tile[0] == " ":
                    # It's passable
                    char = " "
                elif tile[0] == "#":
                    # It's a wall
                    char = "#"
                    self.walls_locs.append(tile_coords)
                elif tile[0] == "$":
                    # It's a mine
                    char = "$"
                    self.mines_locs.append(tile_coords)
                    self.mines[tile_coords] = tile[1]
                    if tile[1] == str(self.hero.bot_id):
                        # This mine is belong to me:-)
                        self.hero.mines.append(tile_coords)
                elif tile[0] == "[":
                    # It's a tavern
                    char = "T"
                    self.taverns_locs.append(tile_coords)
                elif tile[0] == "@":
                    # It's a hero
                    char = "H"
                    if not int(tile[1]) == self.hero.bot_id:
                        # I don't want to be put in an array !
                        # I'm not a number, i'm a free bot:-)
                        self.heroes_locs.append(tile_coords)
                    else:
                        # And I want to be differenciated
                        char = "@"
                map_line = map_line + str(char)
            self.board_map.append(map_line)
            map_line = ""

    def process_heroes(self, heroes):
        """Add heroes"""
        for hero in heroes:
            self.spawn_points_locs[(hero['spawnPos']['y'], hero['spawnPos']['x'])] = hero['id']
            self.heroes.append(Hero(hero))
            # Add spawn points to map
            line = list(self.board_map[int(hero['spawnPos']['x'])])
            if line[int(hero['spawnPos']['y'])] != "@" and \
                    line[int(hero['spawnPos']['y'])] != "H":
                line[int(hero['spawnPos']['y'])] = "X"
            line = "".join(line)
            self.board_map[int(hero['spawnPos']['x'])] = line


    
        
    
            
