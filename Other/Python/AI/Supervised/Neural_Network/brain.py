#A Neural Network Implemented in Python
#By DanG
import numpy as np
import math
import time
import neural_network
import random
import sys
import json

from pybrain.structure import FeedForwardNetwork, SigmoidLayer, FullConnection


#TODO: 
#Add debug/evaluation methods to test effectiveness of different methods
#print out graph of improvement over time or error over time.
#Code various training regimes
#Test SLPercep and MLPercep

class Brain:
    'A generic neural network object'

    def __init__(self, networkInputFile):
        """Initializes the brain"""
        self.network = neural_network.create_network(networkInputFile)
        
        self.tVerbose = False
        if networkInputFile["trainingMethod"] == "Batch":
            self.tFactor = networkInputFile["trainingProperties"]["trainingFactor"]
            self.bSize = networkInputFile["trainingProperties"]["batchSize"]
            if "verbose" in networkInputFile["trainingProperties"]:
                self.tVerbose = networkInputFile["trainingProperties"]["verbose"]
            self.training_method = batch_train 
        if networkInputFile["trainingMethod"] == "Online":
            self.tFactor = networkInputFile["trainingProperties"]["trainingFactor"]
            if "verbose" in networkInputFile["trainingProperties"]:
                self.tVerbose = networkInputFile["trainingProperties"]["verbose"]
            self.bSize = 1
            self.training_method = online_train

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
        return self.training_method(self.network, input_vals, output_vals, self.bSize, self.tFactor, self.tVerbose)

    def predict(self, inputSet):
        """Predicts an output based on the trained values"""
        return self.network.calculate(inputSet)

    def evolve(self):
        """Grows new neurons and links. Trims trivial neurons and links"""

##----------------------Training Methods---------------------------------------

def batch_train(network, input_set, output_set, batch_size, train_factor, verbose=False):

    leftover_data = len(input_set) % batch_size
    upper_limit = len(input_set) - leftover_data

    training_error = 0.0

    for i in range(0, upper_limit, batch_size):
        weights_error = []
        bias_error = []
        batch_error = 0.0

        for n in range(len(network.network_weights)):
            weights_error.append(np.zeros(network.network_weights[n].shape))
            bias_error.append(np.zeros(network.network_bias[n].shape))

        for j in range(batch_size):
            network_output = network.calculate(input_set[i + j])
            w_err_tmp, b_err_tmp = network.correction(output_set[i + j])

            for n in range(len(weights_error)):
                weights_error[n] += w_err_tmp[n]
                bias_error[n] += b_err_tmp[n]

            batch_error += np.divide(np.sum(np.multiply(np.divide(np.abs(\
                               output_set[i + j] - network_output), \
                               output_set[i + j]), 100.0)), len(network_output))

        batch_error = batch_error / float(batch_size)
        if verbose:
            print batch_error, "% batch train error"
        
        training_error += batch_error

        for n in range(len(weights_error)):
            weights_error[n] = np.multiply((float(train_factor) / batch_size), weights_error[n])
            bias_error[n] = np.multiply((float(train_factor) / batch_size), bias_error[n])
        
        network.adjustment(weights_error, bias_error)

    
    weights_error = []
    bias_error = []
    batch_error = 0.0
    for n in range(len(network.network_weights)):
        weights_error.append(np.zeros(network.network_weights[n].shape))
        bias_error.append(np.zeros(network.network_bias[n].shape))

    for k in range(leftover_data):
        network_output = network.calculate(input_set[upper_limit + k])
        w_err_tmp, b_err_tmp = network.correction(output_set[upper_limit + k])
        for n in range(len(weights_error)):
            weights_error[n] += w_err_tmp[n]
            bias_error[n] += b_err_tmp[n]
        
        batch_error += np.divide(np.sum(np.multiply(np.divide(np.abs(\
                           output_set[upper_limit + k] - network_output), \
                           output_set[upper_limit + k]), 100.0)), len(network_output))

        batch_error = batch_error / float(batch_size)
        if verbose:
            print batch_error, "% batch train error"
            #Possibly return the value in list rather than print
        
        training_error += batch_error

        for n in range(len(weights_error)):
            weights_error[n] = np.multiply((float(train_factor) / batch_size), weights_error[n])
            bias_error[n] = np.multiply((float(train_factor) / batch_size), bias_error[n])

    network.adjustment(weights_error, bias_error)

    
    training_error = training_error / ((float(upper_limit) / batch_size) + int(bool(leftover_data)))
    return training_error

def online_train(network, input_set, output_set, batch_size, train_factor, verbose=False):
    return batch_train(network, input_set, output_set, 1, train_factor, verbose)

def stochastic_train(network, input_set, output_set, train_size, test_size, max_num_epochs, report_epochs, max_error_val, train_factor, verbose=False):
    pass



#Brain has attributes, network, braintype.

#Depending on brain type brain can have limited resources.

#brain can train (train on a dataset)
#Brain can predict (test a dataset)
#Brain can load from file.
#Brain can save to file.

def main(argv):
    with open(argv[0]) as json_data:
        data_dict = json.load(json_data)
        test_brain = Brain(data_dict)

    #Simple Test 
    in_data = 0.25
    print test_brain.predict(np.array([in_data]))
    print test_brain.learn(test_brain.trainingSet[0])
    print math.sin(in_data)
    print test_brain.predict(np.array([in_data]))

    #Use Pybrain to compare output results
    compare_brain = FeedForwardNetwork()
    inLayer = SigmoidLayer(data_dict["networkProperties"]["sizeInitialLayer"])
    hiddenLayer = SigmoidLayer(data_dict["networkProperties"]["hiddenLayerSizes"][0])
    outLayer = SigmoidLayer(data_dict["networkProperties"]["numberOutputs"])
    compare_brain.addInputModule(inLayer)
    compare_brain.addModule(hiddenLayer)
    compare_brain.addOutputModule(outLayer)
    in_2_hid = FullConnection(inLayer, hiddenLayer)
    hid_2_out = FullConnection(hiddenLayer, outLayer)
    compare_brain.addConnection(in_2_hid)
    compare_brain.addConnection(hid_2_out)
    compare_brain.sortModules()
    


if __name__ == "__main__":
    main(sys.argv[1:])
