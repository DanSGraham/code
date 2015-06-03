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
class DanielGrahamWizard(Wizard):
    
    
    def __init__(self):
        # we call the setName() method, which was INHERITED
        # from this class's parent class (WIZARD)
        self.setName("MCHammer4.0")
        self.setHouse("Slytherin")
        self.myActionList = ['CastN', 'CastS', 'CastE', 'CastW', 
                             'CastF', 'CastO', 'CastL', 'CastR']

    def dangerWizard(self, wizard):
        if wizard.waitToCastMissileCounter <= 1:
            return True
        else:
            return False
            
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
        
    def runFromWizard(self, worldGrid, direction_conversions):
        wizardList = self.world.getWizardList()
        for wizard in wizardList:
           for key in direction_conversions:
               if wizard.getLocation() == key and self.dangerWizard(wizard):
                    return True
        return False

    def outOfBounds(self,point):
        for j in range(2):
            if point[j] < 0 or point[j] > 7:
                return True
        return False
            
    def runAway(self, worldGrid, adjacent, direction_conversions, missile_strike_list = None ):
        moveList = ['N', 'E', 'S', 'W']
        for unopen in adjacent:
            moveList.remove(unopen)
        if missile_strike_list != None:
            for missile in missile_strike_list:
                if (missile[0] in moveList):
                    moveList.remove(missile[0])
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

   # def analyze(self):
        #analyzes the board for target priorities.

        #Target Priorities:
        #Wizards that move adjacent to my wizard and are not facing and still have time on the countdown timer
        #wizards that move adjacent to my wizard and are facing and still have time on the countdown timer
        #move to a wizards adjacent square if they have a count of 2 or greater.
        #Wizards with multiple missiles impending
        #Wizards headed to corners(difficult)
        #closest wizard

    
        

        
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
        
        next_turn_missile_location = self.missileNextTurn(worldGrid)
        missile_strike_list = []
        for missile in next_turn_missile_location:
            if self.getLocation() == missile[1]:
                missile_strike_list.append(missile)
        if missile_strike_list != []:
            adjacent_objects = self.isAdjacent(worldGrid, direction_conversions)
            return self.runAway(worldGrid, adjacent_objects, direction_conversions, missile_strike_list)
        if self.runFromWizard(worldGrid, direction_conversions):
            adjacent_objects = self.isAdjacent(worldGrid, direction_conversions)
            return self.runAway(worldGrid, adjacent_objects, direction_conversions)
        adjacent_wizards = self.isAdjacent(worldGrid, direction_conversions)
        if adjacent_wizards != []:
            return 'Cast' + adjacent_wizards[0]
        if self.shoot(lineOfSight):
            return 'CastF'
        
        return random.choice(self.myActionList)
            
                

        #CURRENTLY RUNS AWAY FROM MISSILES TO OPEN SPACE. HERE ARE SCENERIOS THAT WOULD RESULT IN DEATH:
            #IF TWO MISSILES STRIKE AT SAME TIME. FIXED IN VERSION 2
            #IF BOXED IN ON ALL FOUR SIDES BY POTENTIAL MISSILES OR PLAYERS (FIX WOULD BE TO FACE A MISSILE AND KILL IT or NEVER GET BOXED IN
            
        #PRIORITIES FOR FIRING MISSILES
            #1 IF WIZARD CAN FIRE A MISSILE THAT SIMULTANEOUSLY HITS A WIZARD WITH A DIFFERENT MISSILE
            #2 IF A WIZARD IS TRYING THE GO TO A CORNER STRATEGY. IDENTIFY THAT A WIZARD IS MOVING IN THE DIRECTION OF A CORNER AND
                # FIRE A MISSILE TO HIT THEM BEFORE THEY GET THERE
            #3 IF A WIZARD IS ADJACENT. YISHENG'S MOVED TO THE CLOSEST WIZARD AND GOT ON HIS DIAGONOL. THEN HE WAITED FOR THE OTHER WIZARD TO MOVE AND FIRED MISSILE WHEN WIZARD ADJACENT.
        # OTHER NOTES:
            #MARK WIZARDS AS DEADLY OR SAFE? SAFE WIZARDS HAVE THE COUNTER STILL COUNTING DOWN, DEADLY WIZARDS CAN FIRE
        #PRIORITIES FOR MOVEMENT
            #1.NOT DYING
             #2. OPTIMAL MISSILE PLACEMENT
         #NOTES ABOUT YISHENG'S:
                #CANNOT DEFEND AGAINST TWO MISSILES AT ONCE. MIGHT NOT BE ABLE TO DEFEND AGAINST A MISSILE INCOMING EITHER
                # MOVES TOWARDS THE CLOSEST PENGUIN BY A SAFE ROUTE, IE NO ADJACENT SQUARES. ALSO MIGHT DETERMINE IF THEY FIRED A MISSILE.
                # DIFFICULT TO DETERMINE DIAGNOL MOVEMENT. SO IF YS IS ONLY ONE HORIZONTAL SQUARE AWAY, I THINK IT HAS A HARD TIME MOVING TO THE DIAGONL. IT CANNOT MOVE IN AN L FORMATION. MAYBE?

        #Stay one square away from other wizards
        #Face and move towards other wizards. Fire Missiles at others
        #right now, just tries to move forward every turn
        # A GOOD TEST OF INFALLIBALITY WOULD BE TO TRY TO MAKE A KILL WIZARD THAT CAN KILL THE RUN AWAY WIZARD. BY IMPROVING EACH WE CAN MAKE THE ULTIMATE WIZARD
        #ALSO A TEST MIGHT BE GOOD. A PROGRAM THAT RUNS THE DUEL A THOUSAND TIMES AND RETURNS WHO WON MOST. COULD PIT PREVIOUS WIZARDS AGAINST UPDATED MODELS.

        
        
