#A Neural Network Implemented in Python
#By DanG
import numpy as np
import math
import time
import neural_network
import random
import sys
import json


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

    def predict(self, inputSet):
        """Predicts an output based on the trained values"""
        self.network.calculate(inputSet)

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
#    test_brain.predict(np.array([2,4,6,3,1,8,5,7,9,0]))

if __name__ == "__main__":
    main(sys.argv[1:])
