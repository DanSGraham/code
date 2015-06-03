from duelgame import Wizard

import random

# This class is a "subclass" of Wizard... that is, it inherits
# ALL of the data and methods that the generic Wizard class has, but
# we can add additional functionality (like chooseAction(), in this case)
#
class ScaredyWizard(Wizard):
    def __init__(self):
        # we call the setName() method, which was INHERITED
        # from this class's parent class (WIZARD)
        self.setName("ScaredyWiz")
        self.setHouse("Hufflepuff")
    
    # chooseAction() is the KEY function that the wizard uses to pick 
    # what action it should take each turn, based on where this Wizard is, 
    # and what it can see.
    #
    # See long description in YOURNAME_wizard.py for details
    #
    def chooseAction(self, locationX, locationY, currentlyFacing, lineOfSight, worldGrid, missileRechargeCounter):
        if 'M' in lineOfSight:   # ScaredyWizard flees whenever it sees a missile
            return 'MoveO'
        elif 'W' in lineOfSight:  # and casts magic missile whenever it sees a wizard
            return 'CastF'
        elif len(lineOfSight) == 0:  # and turns whenever it hits a wall
            return 'FaceL'
        else:                   #and moves forward otherwise
            return 'MoveF'
        
        
