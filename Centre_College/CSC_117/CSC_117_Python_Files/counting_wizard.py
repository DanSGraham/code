from duelgame import Wizard

import random


class CountingWizard(Wizard):
    def __init__(self):
        self.setName("Count von Counter")
        self.setHouse("Ravenclaw")
        self.counter = 0
        
    # chooseAction() is the KEY function that the wizard uses to pick 
    # what action it should take each turn, based on where this Wizard is, 
    # and what it can see.
    #
    # See long description in YOURNAME_wizard.py for details
    #
    def chooseAction(self, locationX, locationY, currentlyFacing, lineOfSight, worldGrid, missileRechargeCounter):
        ## keep track of how many game steps have been taken
        self.counter = self.counter + 1
        self.checkResetCounter()
        ## We have a 16 step rotation, where we move in a clockwise square
        ## going north 3 steps, east 3 steps, south 3 steps, and west 3 steps
        ## Every 3th step, we cast a missile forward.
        if (self.counter == 0):
            return "CastF"
        elif (self.counter < 4):
            return "MoveN"
        elif (self.counter == 4):
            return "CastF"
        elif (self.counter < 8):
            return "MoveE"
        elif (self.counter == 8):
            return "CastF"
        elif (self.counter < 12):
            return "MoveS"
        elif (self.counter == 12):
            return "CastF"
        elif (self.counter < 16):
            return "MoveW"
            
    def checkResetCounter(self):
        if (self.counter >= 16):
            self.counter = 0
        
