#A Neural Network Implemented in Python
#By DanG

import json
import math
import random
import sys
import time
import numpy as np
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import neural_network


#TODO: 
#Test the recurrant properties of the RNN. Try a data set with some recurrance.
#Seems like it is wrong...
#Add convolution layers
#Add LSTMN functionality
#Create template input brain file and input file
#Allow for general layer addition.
#Docstring
#Currently going with a 70/30 train to test method.
#Do ROC analysis for error
#print out graph of improvement over time or error over time.
#Code various training regimes
#Test SLPercep and MLPercep



class Brain:



    'A generic neural network object'

    def __init__(self, networkInputFile):

        """Initializes the brain"""
        self.network = neural_network.create_network(networkInputFile)
        
        self.maxEpochs = None
        if networkInputFile["trainingMethod"] == "Batch":
            self.tFactor = networkInputFile["trainingProperties"][
                                            "trainingFactor"]
            self.bSize = networkInputFile["trainingProperties"]["batchSize"]
            self.training_method = batch_train
            if "maxEpochs" in networkInputFile["trainingProperties"]:
                self.maxEpochs = networkInputFile["trainingProperties"]["maxEpochs"]
        if networkInputFile["trainingMethod"] == "Online":
            self.tFactor = networkInputFile["trainingProperties"][
                                            "trainingFactor"]
            self.bSize = 1
            self.training_method = online_train
        if networkInputFile["trainingMethod"] == "Stochastic":
            self.tFactor = networkInputFile["trainingProperties"][
                                            "trainingFactor"]
            self.bSize = networkInputFile["trainingProperties"]["batchSize"]
            self.maxEpochs = networkInputFile["trainingProperties"][
                                              "maxEpochs"]


            self.average_error = []
            self.training_method = stochastic_train

        if "trainingSet" in networkInputFile:
            self.trainingSet = networkInputFile["trainingSet"]
        

    def load(self, brainFile):

        """Loads a brain from an existing file"""

    def save(self, destinationName):

        """Saves a brain to a file"""

    def learn(self, trainingFile):

        """Trains a brain on the training set"""
        #Single training set.
        with open(trainingFile) as json_file:
                trainingSet = json.load(json_file)

        input_vals = trainingSet["inputSet"]
        output_vals = trainingSet["outputSet"]

        for i in range(len(input_vals)):
            input_vals[i] = np.array(input_vals[i])
            output_vals[i] = np.array(output_vals[i])
        
        #Run training method
        return self.training_method(
                self, input_vals, output_vals, 
                self.bSize, self.maxEpochs
            )

    def predict(self, inputSet):

        """Predicts an output based on the trained values"""
        return self.network.calculate(inputSet)

    def evolve(self):

        """Grows new neurons and links. Trims trivial neurons and links"""

##----------------------Training Methods---------------------------------------

def batch_train(brain, input_set, output_set, batch_size, epochs=1):
    total_err_list = []
    for epoch in range(epochs):
        network = brain.network
        leftover_data = len(input_set) % batch_size
        upper_limit = len(input_set) - leftover_data

        for i in range(0, upper_limit, batch_size):

            for j in range(batch_size):
                network_output = network.calculate(input_set[i + j])
                Tot_E = network.correction(output_set[i + j])
            network.adjustment(batch_size)
     
        for k in range(leftover_data):
            network_output = network.calculate(input_set[upper_limit + k])
            Tot_E = network.correction(output_set[upper_limit + k])
        if leftover_data != 0:
            network.adjustment(leftover_data)
        total_err_list.append(Tot_E) 
    return total_err_list

def online_train(brain, input_set, output_set, batch_size, epochs=1):

    return batch_train(brain, input_set, output_set, 1, epochs)

def single_epoch(
        brain, input_matrix, output_matrix, 
        minibatch_size, train_to_test_ratio=0.7):

    network = brain.network
    #Trains a single epoch.
    in_copy = []
    out_copy = []
    index_list = range(len(input_matrix))
    random.shuffle(index_list)
    for i in range(int(len(input_matrix) * train_to_test_ratio)):
        in_copy.append(np.copy(input_matrix[index_list[i]]))
        out_copy.append(np.copy(output_matrix[index_list[i]]))
    batch_train(brain, in_copy, out_copy, minibatch_size, train_factor)
    #Determine error in test set. 
    tot_SSE = 0.0
    for j in range(
            int(len(input_matrix) * train_to_test_ratio), len(input_matrix)):
        network.calculate(input_matrix[index_list[j]])
        Tot_E = network.correction(output_matrix[index_list[j]])
        tot_SSE += Tot_E

    return tot_SSE

def stochastic_train(
        brain, input_set, output_set, 
        batch_size,  max_epochs):

    network = brain.network 
    SSE_list = []
    for i in range(max_epochs):
        SSE_list.append(single_epoch(
            brain, input_set, output_set, batch_size))
    return SSE_list

#Brain has attributes, network, braintype.

#Depending on brain type brain can have limited resources.

#brain can train (train on a dataset)
#Brain can predict (test a dataset)
#Brain can load from file.
#Brain can save to file.



def main(argv):

    with open(argv[0]) as json_data:
        data_dict = json.load(json_data)
    compareBrains(data_dict)


def compareBrains(data_dict):

    test_brain = Brain(data_dict)

    #Simple Test 
    print "MY BRAIN RESULTS"
    in_data = [0.25, 0.1]
    test_brain.predict(np.array(in_data))
    test_brain.predict(np.array(in_data))
    test_brain.predict(np.array(in_data))
    test_brain.predict(np.array(in_data))
    print test_brain.predict(np.array(in_data))
    in_data2 = [random.random(), random.random()]
    test_brain.predict(np.array(in_data))
    print test_brain.learn(test_brain.trainingSet[0])
    print [math.sin(in_data[0]) - math.sin(in_data[1]), math.sin(in_data[0]) + math.sin(in_data[1])]
    test_brain.predict(np.array(in_data))
    in_data2 = [random.random(), random.random()]
    test_brain.predict(np.array(in_data2))
    in_data2 = [random.random(), random.random()]
    test_brain.predict(np.array(in_data2))
    in_data2 = [random.random(), random.random()]
    test_brain.predict(np.array(in_data2))
    in_data2 = [random.random(), random.random()]
    print test_brain.predict(np.array(in_data2))
    in_data2 = [random.random(), random.random()]


    print "PYBRAIN RESULTS"
    #Use Pybrain to compare output results
    #Build pybrain
    compare_brain = buildNetwork(2, data_dict["networkProperties"]["hiddenLayerSizes"][0], 2, bias=True)
    print compare_brain.activate(in_data)
    #Build Dataset
    ds = SupervisedDataSet(2,2)
    trainingFile = test_brain.trainingSet[0] 
    with open(trainingFile) as json_file:
        trainingSet = json.load(json_file)

    input_vals = trainingSet["inputSet"]
    output_vals = trainingSet["outputSet"]

    for i in range(len(input_vals)):
        ds.addSample((input_vals[i][0],input_vals[i][1]), (output_vals[i][0],output_vals[i][1]))

    trainer = BackpropTrainer(compare_brain, ds)

    for i in range(data_dict["trainingProperties"]["maxEpochs"]):
        trainer.train()

    print "EXPECTED VS OUTPUT"
    print [math.sin(in_data[0]) - math.sin(in_data[1]), math.sin(in_data[0]) + math.sin(in_data[1])]
    print compare_brain.activate(in_data)

if __name__ == "__main__":
    main(sys.argv[1:])

