# Wizard Duel game, by Dr. Stonedahl (April 2013)
#
# This is the main file, with the Wizard, Missile, & World classes
# which contains most of the implementation of the Wizard Duel game.
#
# You should NOT modify this file, though you are welcome to look at it
# in order to learn how I wrote the game. (There's quite a bit of code here...)
#
# Instead, you SHOULD rename and edit the YOURNAME_wizard.py file, and 
# edit the "runduel.py" file to include whichever wizards you want to duel.
#

from graphics import *
import random
import time

DELAY_FACTOR = 1.0
WORLD_WIDTH=8
WORLD_HEIGHT=8
WORLD_CENTER_X = WORLD_WIDTH / 2 - 0.5
WORLD_CENTER_Y = WORLD_HEIGHT / 2 - 0.5
IMAGE_NAME_LIST = ["wizard_penguin0.gif","wizard_penguin1gif","wizard_penguin2.gif",
                   "wizard_penguin3.gif","wizard_penguin4.gif","wizard_penguin5.gif"]
HOUSE_IMAGE_LIST = ['gandalf.gif', 'gryffindor.gif', 'ravenclaw.gif', 
                    'elphaba.gif', 'slytherin.gif', 'hufflepuff.gif',
                    'oz.gif']
          
###################### (Generic) Wizard Class #####################

#This class embodies a lot of code that is general to all Wizard objects
# that will compete in the wizard duel... data members like name, house, 
# and facing direction, and methods like getLocation(), draw(), and undraw(),
# which is functionality that all Wizards must have.
#
# However, it does NOT specify a working chooseAction() method.  
# Subclasses of Wizard must implement that method, so that instances
# of those subclasses will be able to make decisions about what actions
# to take during the duel.
#
class Wizard(object):
    def getName(self):          # accessor for wizard's name
        return self.name
    def setName(self,newName):  # mutator for wizard's name
        self.name = newName
    def getHouse(self):         # accessor for wizard's house
        return self.house
    def setHouse(self,house):   # mutator for wizard's name
        self.house = house
    def getX(self):             # get the wizard's x-coordinate
        return self.image.getAnchor().getX()
    def getY(self):             # get the wizard's y-coordinate
        return self.image.getAnchor().getY()
    def getLocation(self):      # get the wizard's location as a 2-tuple
        return (self.getX(),self.getY()) 

    # if a subclass doesn't "override" (create their own version of)
    # the chooseAction() method, then we will raise an Exception!
    def chooseAction(self, locationX, locationY, currentlyFacing, lineOfSight, worldGrid, missileRechargeCounter):
        raise "Subclasses must provide their own implementation of chooseAction()!"
    
    # A number of things must be done to get the wizard situated in the world:
    # e.g. create the image, the arrow indicator, and text for the name below the image.
    def setupInWorld(self,imageFile,startX,startY,startFacing,world):
        self.world = world
        self.image = Image(Point(startX,startY),imageFile)
        self.textWidget = Text(Point(startX,startY-0.4),self.getName())
        self.textWidget.setTextColor('white')
        self.textWidget.setSize(10)
        self.facing = startFacing
        self.lookArrow = Image(Point(startX,startY),'arrow'+self.facing+'.gif')
        self.waitToCastMissileCounter = 0

    # draw the wizard in the window
    def draw(self,win):
        self.image.draw(win)
        self.textWidget.draw(win)
        self.lookArrow.draw(win)
    
    #undraw the wizard
    def undraw(self):
        self.image.undraw()
        self.textWidget.undraw()
        self.lookArrow.undraw()
    
    # change which direction the wizard is facing to newDirection.
    def setFacing(self,newDirection,win):
        if newDirection != self.facing:
            self.lookArrow.undraw()
            self.facing = newDirection
            self.lookArrow = Image(Point(self.getX(),self.getY()),'arrow'+self.facing+'.gif')
            self.lookArrow.draw(win)
        
    # move the wizard one unit in a certain direction (unless the way is blocked)
    def move(self, direction,win):
        self.setFacing(direction,win)
        (destX,destY) = self.world.getNeighborLocation(self.getX(),self.getY(),direction)
        if not self.world.isBlocked(destX,destY):
            dx = destX - self.getX()
            dy = destY - self.getY()
            self.image.move(dx,dy)
            self.textWidget.move(dx,dy)
            self.lookArrow.move(dx,dy)
    
    # choose and execute one action for this round.
    def act(self,win):
        x,y = self.getLocation()
        lineOfSight = self.world.getLineOfSight(x,y,self.facing)
        worldGrid = self.world.getGrid()
        action = self.chooseAction(x,y,self.facing,lineOfSight,worldGrid, self.waitToCastMissileCounter)
        
        if self.waitToCastMissileCounter > 0:
            self.waitToCastMissileCounter -= 1
            
        if action == None:
            pass
        elif action.startswith('Face'):
            dirCode = action[-1]
            direction = self.world.calculateCardinalDirection(self.facing,dirCode)
            self.setFacing(direction,win)
        elif action.startswith('Move'):
            dirCode = action[-1]
            direction = self.world.calculateCardinalDirection(self.facing,dirCode)
            self.move(direction,win)
        elif action.startswith('Cast'):
            if (self.waitToCastMissileCounter == 0):
                dirCode = action[-1]
                direction = self.world.calculateCardinalDirection(self.facing,dirCode)
                self.setFacing(direction,win)
                magicMissile = Missile(x,y,self.facing,self.world)
                self.world.addMissile(magicMissile)
                magicMissile.move()
                self.waitToCastMissileCounter = 4
        elif action == 'Block':
            blockX,blockY=self.world.getNeighborLocation(x,y,self.facing)
            if (self.world.isInsideWorld(blockX,blockY)):
                objInFront = self.world.getObjectAt(blockX,blockY)
                if isinstance(objInFront,Missile):
                    self.world.drawZap(blockX,blockY)
                    self.world.removeFromWorld(objInFront)
        else:
            print "ERROR: Unknown action: " + str(action)
            

            
            
            
###################### Missile Class #####################
   
# represents a magic missile, which moves through the world
# and causes anything that it hits to suddenly vanish
class Missile:
    #The constructor for the Missile object, which takes in the
    # starting location (startX and startY), as well as the direction
    # of travel, and a reference to the world object.
    def __init__(self,startX,startY,direction,world):
        self.image = Image(Point(startX,startY),'fireball'+direction+'.gif')
        self.direction = direction
        self.world = world
    
    def getLocation(self):                  #get the Missile's location
        return (self.getX(),self.getY())
    def getX(self):                         #get the Missile's x-coordinate
        return self.image.getAnchor().getX()
    def getY(self):                         #get the Missile's y-coordinate
        return self.image.getAnchor().getY()
    
    def draw(self,win):       #draw the Missile in the GraphWin window
        self.image.draw(win)

    def undraw(self):         #undraw the Missile
        self.image.undraw()
    
    # Move the Missile (straight forward one square).  If it hits anything,
    # then we make both the missile and its target vanish.
    def move(self):           
        world = self.world
        newX,newY = world.getNeighborLocation(self.getX(),self.getY(),self.direction)
        if world.isInsideWorld(newX,newY):
            dx,dy=world.getMovementOffsets(self.direction)
            objectInDestination = self.world.getObjectAt(newX,newY)
            self.image.move(dx,dy)
            if (objectInDestination != None):
                world.drawZap(newX,newY)
                world.removeFromWorld(objectInDestination)
                world.removeFromWorld(self)
        else:
            world.removeFromWorld(self)
            
            
            
            
###################### World Class #####################

# The world class contains many methods needed to represent
# the dueling arena.  Notably it contains a list of the 
# wizards and missiles that are currently in the arena,
# and ways to add/remove/interact with them.
class World:
    #constructor for the World class -- win should be a GraphWin object 
    def __init__(self,win):
        self.win = win
        self.wizardList = []
        self.missileList = []

    def getWizardList(self):    #returns the list of Wizards in the arena
        return self.wizardList
    
    def getMissileList(self):   #returns the list of Missiles in the arena
        return self.missileList

    def addMissile(self,mis):   #adds a new Missile object to the arena
        self.missileList.append(mis)
        mis.draw(self.win)

    def addWizard(self,wiz):     #adds a new Wizard object to the arena
        self.wizardList.append(wiz)

    def removeFromWorld(self,obj):   #removes an object from the arena
        if isinstance(obj,Wizard):
            self.wizardList.remove(obj)
        elif isinstance(obj,Missile):
            self.missileList.remove(obj)
        obj.undraw()
            
    def isBlocked(self,x,y):     #is there already an object at location x,y?
        return not self.isInsideWorld(x,y) or self.getObjectAt(x,y) != None
    
    #is location x,y inside the world's bounds? (i.e. on the screen)
    def isInsideWorld(self,x,y): 
        return (x>=0) and (x < WORLD_WIDTH) and (y>=0) and (y < WORLD_HEIGHT)
    
    #returns the object at location x,y (or None, if no object is there)
    def getObjectAt(self,x,y):
        for obj in self.wizardList + self.missileList:
            if round(obj.getX()) == x and round(obj.getY() == y):
                return obj
        return None
    
    # based on the old direction (N/S/E/W), and a direction code
    #  (which could be N/S/E/W, or F/L/R/O), calculate the new direction
    def calculateCardinalDirection(self,oldDirection,newDirectionCode):
        DIRS = ['N','E','S','W'] 
        if newDirectionCode in DIRS: #if it's a cardinal direction, return it.
            return newDirectionCode
        else: #otherwise rotate according to the rotation code
            rotation = ['F', 'R', 'O', 'L'].index(newDirectionCode)
            currentIndex = DIRS.index(oldDirection)
            return DIRS[(currentIndex + rotation) % 4]

        
        
    # returns a tuple representing the amount that x and y would need 
    # to change in order to move in a specified cardinal direction.
    def getMovementOffsets(self,direction):
        if direction == 'N':
            return (0,1)
        elif direction == 'S':
            return (0,-1)
        elif direction == 'W':
            return (-1,0)
        elif direction == 'E':
            return (1,0)
        else:
            raise "Unreasonable direction given:  " + str(direction)

    # returns a tuple containing the new x and y values that you would arrive
    # at if you moved in the given direction from the given x and y location.
    def getNeighborLocation(self,x,y,direction):
        dx,dy = self.getMovementOffsets(direction)
        return (x+dx,y+dy)

    # returns a list of characters representing the line of sight from
    # a given location (x,y) in a certain direction, out to the edge of the world.
    # e.g., ['-', 'M', 'W', '-'] would mean that there are four squares
    # between you (at x,y) and the edge of the world, and moving outward
    # from you, these four squares contain:
    # nothing, a missile, a wizard, and nothing
    def getLineOfSight(self,x,y,direction):
        visionList =[]
        x,y = self.getNeighborLocation(x,y,direction)
        while self.isInsideWorld(x,y):
            visionList.append(self.getCharacterCode(x,y))
            x,y = self.getNeighborLocation(x,y,direction)
        return visionList

    # returns a nested list (grid) representing the world state using the 
    # characters 'W', 'M' and '-'
    def getGrid(self):
        return [ [ self.getCharacterCode(x,y) \
                    for y in range(WORLD_HEIGHT)] \
                    for x in range(WORLD_WIDTH)]

    # What's at a given location?
    # returns 'W' for Wizard, 'M' for Missile, and '-' for empty squares
    def getCharacterCode(self,x,y):
        obj = self.getObjectAt(x,y)
        if isinstance(obj,Wizard):
            return 'W'
        elif isinstance(obj,Missile):
            return 'M'
        else:
            return '-'
        
    #returns a random location within the bounds of the world
    def getRandomLocation(self):
        return (random.randrange(WORLD_WIDTH),random.randrange(WORLD_HEIGHT))
    
    #returns a random EMPTY grid location in the world
    def getRandomEmptyLocation(self):
        locX,locY = self.getRandomLocation()
        while self.isBlocked(locX,locY):
            locX,locY = self.getRandomLocation()
        return (locX,locY)
    
    # prints out a text-based representation of the world --
    # (could be useful for debugging)
    def printGrid(self):
        for rowNum in range(WORLD_HEIGHT-1,-1,-1):
            for colNum in range(WORLD_WIDTH):
                print self.getCharacterCode(colNum,rowNum),
            print
        print
    
    # draw an animated circular "Zap" effect at the specified location
    # (just for show)
    def drawZap(self,x, y):
        radius = 0.02
        circles = []
        for i in range(25):
            c = Circle(Point(x,y),radius)
            c.setOutline(color_rgb(255-i*10,0,i*10))
            c.draw(self.win)
            radius = radius + 0.02
            timeDelay(self.win,0.01)
            circles.append(c)
        for c in circles:
            c.undraw()
            timeDelay(self.win,0.01)
            
    # do one full movement round for each of the missiles,
    # followed by each of the wizards.
    def doSingleRound(self,):
        for missile in list(self.getMissileList()):
            if missile in self.getMissileList():
                missile.move()
                timeDelay(self.win,0.1)
        for wiz in list(self.getWizardList()):
            if wiz in self.getWizardList():
                wiz.act(self.win)
                timeDelay(self.win,0.1)


# Convenience class for displaying a text message 
# with shadow effect (by using 3 text objects)
class DisplayMessage:
    def __init__(self, msg):
        self.text = Text(Point(WORLD_CENTER_X-0.03,WORLD_CENTER_Y+0.03),msg)
        self.text.setSize(18)
        self.text.setStyle('bold')
        self.text.setTextColor('black')
        self.text2 = self.text.clone()
        self.text2.move(0.03,-0.03)
        self.text3 = self.text.clone()
        self.text3.move(-0.03,0.03)
        self.text.setTextColor('white')
        
    def draw(self,win):
        self.text2.draw(win)
        self.text3.draw(win)
        self.text.draw(win)
    def undraw(self):
        self.text.undraw()
        self.text2.undraw()
        self.text3.undraw()
    def setText(self, newText):
        self.text.setText(newText)
        self.text2.setText(newText)
        self.text3.setText(newText)
    
###################### General Functions #####################

# Pause before continuing
def timeDelay(win,seconds):
    if (DELAY_FACTOR > 0):
        time.sleep(seconds*DELAY_FACTOR)
    else:
        win.getMouse()
        
# Runs a full duel between the given competitors up to maxRounds rounds.
#   competitors should be a list of Wizard objects 
#     (technically instances of *subclasses* of the general Wizard class)
#   maxRounds should be an integer.
def doFullDuel(competitors, maxRounds):
    win = GraphWin("Wizard Duel Game", 80*WORLD_WIDTH, 80*WORLD_HEIGHT)
    win.setCoords(-0.5,-0.5,WORLD_WIDTH-0.5,WORLD_HEIGHT-0.5)
    grass = Image(Point(WORLD_WIDTH/2,WORLD_HEIGHT/2),"grass_big.gif")
    grass.draw(win)

    world = World(win)
    
    # place the wizards randomly on the board, and assign them
    # penguin images.
    for i in range(len(competitors)):
        wiz = competitors[i]
        startX,startY = world.getRandomEmptyLocation()
        startFacing = random.choice(['N','E','S','W'])
        imgFile ="wizard_penguin"+str(i%6)+".gif"
        if hasattr(wiz,'jailed'):
            imgFile = "wizard_jailed.gif"
        wiz.setupInWorld(imgFile,startX,startY,startFacing,world)
        world.addWizard(wiz)       
        wiz.draw(win)

    startMessage = DisplayMessage("The duel is about to begin!")
    startMessage.draw(win)
    timeDelay(win,3)
    startMessage.undraw()
        
    roundNum = 0
    while len(world.getWizardList()) > 1 and roundNum < maxRounds:
        world.doSingleRound()
        #world.printGrid()
        timeDelay(win,1)
        roundNum = roundNum + 1        
    
    remainingWizards = world.getWizardList()

    if len(remainingWizards) == 0:
        winMessage = DisplayMessage("Poof!  All the wizards disappeared!")
    elif len(remainingWizards) == 1:
        wiz = remainingWizards[0]
        winMessage = DisplayMessage(wiz.getName() + " of " + wiz.getHouse() + " is victorious!")
        houseImageFileName = wiz.getHouse().lower() + ".gif"
        if houseImageFileName in HOUSE_IMAGE_LIST:
            winImage = Image(Point(WORLD_CENTER_X,5), houseImageFileName)
            winImage.draw(win)
    else:
        msg = "The duel was a tie between these Wizards:\n"
        for wiz in remainingWizards:
            msg = msg + wiz.getName() + ", "
        msg = msg[:-2]
        winMessage = DisplayMessage(msg)
    winMessage.draw(win)
    
    #win.getMouse()
    timeDelay(win,5)
    win.close()
    return remainingWizards
        
# for my convenience, if I try to run this file, it will run runduel.main()
if __name__ == '__main__':
    import runduel
    runduel.main()
