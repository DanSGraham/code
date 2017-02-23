#A Neural Network Implemented in Python
#By DanG
import numpy as np
import math
import time
import neural_network
import random
import sys
import json


#TODO: 
#Code various training regimes
#Test SLPercep and MLPercep

class Brain:
    'A generic neural network object'

    def __init__(self, networkInputFile):
        """Initializes the brain"""
        self.network = neural_network.create_network(networkInputFile)

    def load(self, brainFile):
        """Loads a brain from an existing file"""

    def save(self, destinationName):
        """Saves a brain to a file"""

    def ponder(self, trainingSet):
        """Trains a brain on the training set"""
        inVal = trainingSet[0]
        outVal = trainingSet[1]
        print self.network.calculate(inVal)
        for i in range(1000):
            wVal, bVal = self.network.correction(outVal)
            self.network.adjustment(wVal, bVal)
            self.network.calculate(inVal)

        print self.network.calculate(inVal)

    def predict(self, inputSet):
        """Predicts an output based on the trained values"""
        return self.network.calculate(inputSet)

    def evolve(self):
        """Grows new neurons and links. Trims trivial neurons and links"""

#Brain has attributes, network, braintype.

#Depending on brain type brain can have limited resources.

#brain can ponder (train on a dataset)
#Brain can predict (test a dataset)
#Brain can load from file.
#Brain can save to file.

def main(argv):
    with open(argv[0]) as json_data:
        test_brain = Brain(json_data)
    test_brain.predict(np.array([2,4]))
    test_brain.ponder((np.array([2,4]), np.array([.5,.25])))
    print "EXPECTED:"
    print np.array([.5, .25])

if __name__ == "__main__":
    main(sys.argv[1:])
