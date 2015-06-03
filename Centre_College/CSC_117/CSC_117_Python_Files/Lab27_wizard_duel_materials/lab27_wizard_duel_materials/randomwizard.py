from duelgame import Wizard

import random

# This class is a "subclass" of Wizard... that is, it inherits
# ALL of the data and methods that the generic Wizard class has, but
# we can add additional functionality (like chooseAction(), in this case)
#
class RandomWizard(Wizard):
    def __init__(self):
        # we call the setName() method, which was INHERITED
        # from this class's parent class (WIZARD)
        self.setName("RandomWiz")
        self.setHouse("Gryffindor")
        self.myActionList = ['MoveN', 'MoveS', 'MoveE', 'MoveW',
                             'MoveF', 'MoveO', 'MoveL', 'MoveR',
                             'CastN', 'CastS', 'CastE', 'CastW', 
                             'CastF', 'CastO', 'CastL', 'CastR',
                             'FaceN', 'FaceS', 'FaceE', 'FaceW', 
                             'FaceF', 'FaceO', 'FaceL', 'FaceR', 
                             'Block']
    
    # chooseAction() is the KEY function that the wizard uses to pick 
    # what action it should take each turn, based on where this Wizard is, 
    # and what it can see.
    #
    # See long description in YOURNAME_Wizard.py for details
    #
    def chooseAction(self, locationX, locationY, currentlyFacing, lineOfSight, worldGrid, missileRechargeCounter):
        # RandomWizard simply chooses a random action each time, from
        # the list stored in the myActionList data member...
        return random.choice(self.myActionList)
        
        
