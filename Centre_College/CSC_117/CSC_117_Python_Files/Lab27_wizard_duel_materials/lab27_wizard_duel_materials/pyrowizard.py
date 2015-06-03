from duelgame import Wizard

import random

# This class is a "subclass" of Wizard... that is, it inherits
# ALL of the data and methods that the generic Wizard class has, but
# we can add additional functionality (like chooseAction(), in this case)
#
class PyroWizard(Wizard):
    def __init__(self):
        # we call the setName() method, which was INHERITED
        # from this class's parent class (WIZARD)
        self.setName("PyroWizard")
        self.setHouse("Gandalf")
   
    # chooseAction() is the KEY function that the wizard uses to pick 
    # what action it should take each turn, based on where this Wizard is, 
    # and what it can see.
    #
    # See long description in YOURNAME_Wizard.py for details
    #
    def chooseAction(self, locationX, locationY, currentlyFacing, lineOfSight, worldGrid, missileRechargeCounter):
        #PyroWizard goes to the south edge, and then fires continuously upward!
        if locationY > 0:
            return 'MoveS'
        else:
            return 'CastN'
        
        
