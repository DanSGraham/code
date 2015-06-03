from duelgame import *
import random

# Rename both this .PY file, and this class and replace YourName with your own name.
#
# This class is a "subclass" of Wizard... that is, it inherits
# ALL of the data and methods that the generic Wizard class has, but
# we can add additional functionality (like chooseAction(), in this case)
#
# ******************************************************************************
# * The official dueling rules are that you should not access or modify other  *
# * Wizard class data members or methods EXCEPT for the chooseAction() method! *
# ******************************************************************************
#
class YourNameWizard(Wizard):
    
    
    def __init__(self):
        # we call the setName() method, which was INHERITED
        # from this class's parent class (WIZARD)
        self.setName("DanielTheAgile")
        self.setHouse("Slytherin")
        self.myActionList = ['MoveN', 'MoveS', 'MoveE', 'MoveW',
                             'MoveF', 'MoveO', 'MoveL', 'MoveR',
                             'CastN', 'CastS', 'CastE', 'CastW', 
                             'CastF', 'CastO', 'CastL', 'CastR']
        
    def missileNextTurn(self, worldGrid):
        
        missileList = self.world.getMissileList()
        next_turn_missile_location = []
        for missile in missileList:
            current_location = missile.getLocation()
            current_direction = missile.direction
            if current_direction == 'N':
                next_location = ['S',(current_location[0], current_location[1] + 1)]
            elif current_direction == 'S':
                next_location = ['N',(current_location[0], current_location[1] - 1)]
            elif current_direction == 'W':
                next_location = ['E',(current_location[0] - 1, current_location[1])]
            elif current_direction == 'E':
                next_location = ['W',(current_location[0] + 1, current_location[1])]
            next_turn_missile_location.append(next_location)
            
        return next_turn_missile_location
    
    def approachWizard(self, worldGrid):
        """Gets Close to wizard if turned away"""
        
    def runFromWizard(self, worldGrid,direction_conversions):
        wizardList = self.world.getWizardList()
        for wizard in wizardList:
           for key in direction_conversions:
               if wizard.getLocation() == key:
                   if (direction_conversions[key] == 'N' and wizard.facing == 'S') or (direction_conversions[key] == 'E' and wizard.facing == 'W') or (direction_conversions[key] == 'S' and wizard.facing == 'N') or (direction_conversions[key] == 'W' and wizard.facing == 'E'):
                       print "Facing Me"
                       return True
        return False

    def outOfBounds(self,point):
        print point
        for j in range(2):
            if point[j] < 0 or point[j] > 7:
                return True
        return False
            
    def runAway(self, worldGrid, adjacent, direction_conversions, missile = None ):
        moveList = ['N', 'E', 'S', 'W']
        for unopen in adjacent:
            moveList.remove(unopen)
        if missile != None:
            moveList.remove(missile)
        for direction in moveList:
            for key in direction_conversions:
                if direction_conversions[key] == direction and not(self.outOfBounds(key)):
                    return 'Move' + direction
            return 'Block'
                    
    def shoot(self, lineOfSight):
        sight = lineOfSight
        for item in sight:
            if item == 'W':
                return True
        

        
    def isAdjacent(self, worldGrid, direction_conversions):
       wizardList = self.world.getWizardList() 
       incomingMissiles = self.missileNextTurn(worldGrid)
       unopen_squares = []
       for wizard in wizardList:
           for key in direction_conversions:
               if wizard.getLocation() == key:
                   unopen_squares.append(direction_conversions[key])
       for missiles in incomingMissiles:
           for key in direction_conversions:
               if missiles[1] == key and unopen_squares.count(direction_conversions[key]) < 1:
                   unopen_squares.append(direction_conversions[key])
       return unopen_squares

    def chaseOpponent(self, worldGrid):
        """Chases closest opponent"""
    def fireMissile(self, worldGrid):
        """Fires Missile if facing Opponent"""


    
       # This function may return one action word ('MoveX/CastX/FaceX/Block')
    # where X may be replaced with any of the characters 
    #   * N/S/E/W  (for the four cardinal directions, North, South, East, West)
    #   * F/L/R/O  (for Forward, Left, Right, and Opposite 
    #       - relative to the direction the Wizard is currently facing
    # 
    # Some examples:
    #  * 'MoveS' will cause the wizard to attempt to move South (regardless of which way it is currently facing)
    #  * 'CastF' will cast a magic missile spell forward in the direction the wizard is facing (if they don't need to recharge)
    #  * 'FaceN' will cause the wizard to face north,
    #  * 'FaceL' will cause the wizard to rotate 90 degrees to the left (counter-clockwise)
    #  * 'FaceF' will cause the wizard to essentially do NOTHING.
    #  * 'Block' will use a defensive spell to dispel any missile that is *immediately* (1 square) in front of you.
    #     (Note that you can only block in the direction that you are already facing.)
    #
    # Notes on movement:
    #  - Moving in a direction also causes you to face that direction.
    #  - If the square you try to move to is occupied, you won't move, but you will face that way.
    #
    # Any other return values will be ignored. 
    # Also, if your method generates an error while running, then no action will be taken.

    def chooseAction(self, locationX, locationY, currentlyFacing, lineOfSight, worldGrid, missileRechargeCounter):
        missileList = self.world.getMissileList()
        wizardList = self.world.getWizardList()
        direction_conversions = {(locationX, locationY + 1):'N', (locationX, locationY - 1):'S', (locationX + 1, locationY):'E',(locationX - 1, locationY): 'W'}
        if self.runFromWizard(worldGrid, direction_conversions):
            print "Too Close"
            adjacent_objects = self.isAdjacent(worldGrid, direction_conversions)
            return self.runAway(worldGrid, adjacent_objects, direction_conversions)
        
        next_turn_missile_location = self.missileNextTurn(worldGrid)
        for missile in next_turn_missile_location:
            if self.getLocation() == missile[1]:
                print "Incoming"
                adjacent_objects = self.isAdjacent(worldGrid, direction_conversions)
                return self.runAway(worldGrid, adjacent_objects, direction_conversions, missile[0])
            

        else:
            return random.choice(self.myActionList)
            
                
        
                
##                for key in direction_conversions:
##                    if key != missile and key[0] <= 7 and key[0] >= 0 and key[1] <= 7 and key[1] >= 0:
##                        #ONLY ACCOUNTS FOR ONE MISSILE SINCE THE RETURN STATEMENT BREAKS THE LOOP
##                        print "Move" + direction_conversions[key]
##                        return "Move" + direction_conversions[key]
        #Stay one square away from other wizards
        #Face and move towards other wizards. Fire Missiles at others
        #right now, just tries to move forward every turn
        
        # Old debugging stuff - probalby delete.
        # print worldGrid
        # print
        #print locationX, locationY

        
        
