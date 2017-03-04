#A Neural Network Implemented in Python
#By DanG

import json
import math
import random
import sys
import time
import numpy as np
#from pybrain.structure import FeedForwardNetwork, SigmoidLayer, FullConnection
import neural_network


#TODO: 
#Docstring
#Currently going with a 70/30 train to test method.
#Do ROC analysis for error
#Add debug/evaluation methods to test effectiveness of different methods
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
        if self.maxEpochs != None:
            return self.training_method(
                self.network, input_vals, output_vals, 
                self.maxEpochs, self.bSize, self.tFactor
            )
        else:
            return self.training_method(
                self.network, input_vals, output_vals, 
                self.bSize, self.tFactor
            )

    def predict(self, inputSet):

        """Predicts an output based on the trained values"""
        return self.network.calculate(inputSet)

    def evolve(self):

        """Grows new neurons and links. Trims trivial neurons and links"""

##----------------------Training Methods---------------------------------------

def batch_train(network, input_set, output_set, batch_size, train_factor):

    leftover_data = len(input_set) % batch_size
    upper_limit = len(input_set) - leftover_data

    for i in range(0, upper_limit, batch_size):
        weights_error = []
        bias_error = []

        for n in range(len(network.network_weights)):
            weights_error.append(np.zeros(network.network_weights[n].shape))
            bias_error.append(np.zeros(network.network_bias[n].shape))

        for j in range(batch_size):
            network_output = network.calculate(input_set[i + j])
            w_err_tmp, b_err_tmp, MSE = network.correction(output_set[i + j])

            for n in range(len(weights_error)):
                weights_error[n] += w_err_tmp[n]
                bias_error[n] += b_err_tmp[n]

        for n in range(len(weights_error)):
            weights_error[n] = np.multiply(
                (float(train_factor) / batch_size), weights_error[n])
            bias_error[n] = np.multiply(
                (float(train_factor) / batch_size), bias_error[n])
        network.adjustment(weights_error, bias_error)
     
    weights_error = []
    bias_error = []
    for n in range(len(network.network_weights)):
        weights_error.append(np.zeros(network.network_weights[n].shape))
        bias_error.append(np.zeros(network.network_bias[n].shape))

    for k in range(leftover_data):
        network_output = network.calculate(input_set[upper_limit + k])
        w_err_tmp, b_err_tmp, MSE = network.correction(
                                        output_set[upper_limit + k])
        for n in range(len(weights_error)):
            weights_error[n] += w_err_tmp[n]
            bias_error[n] += b_err_tmp[n]
        
        for n in range(len(weights_error)):
            weights_error[n] = np.multiply(
                (float(train_factor) / batch_size), weights_error[n])
            bias_error[n] = np.multiply(
                (float(train_factor) / batch_size), bias_error[n])

    network.adjustment(weights_error, bias_error)
    return True

def online_train(network, input_set, output_set, batch_size, train_factor):

    return batch_train(network, input_set, output_set, 1, train_factor)

def single_epoch(
        network, input_matrix, output_matrix, 
        minibatch_size, train_factor, train_to_test_ratio=0.7):

    #Trains a single epoch.
    in_copy = []
    out_copy = []
    index_list = range(len(input_matrix))
    random.shuffle(index_list)
    for i in range(int(len(input_matrix) * train_to_test_ratio)):
        in_copy.append(np.copy(input_matrix[index_list[i]]))
        out_copy.append(np.copy(output_matrix[index_list[i]]))
    batch_train(network, in_copy, out_copy, minibatch_size, train_factor)
    #Determine error in test set. 
    tot_SSE = 0.0
    for j in range(
            int(len(input_matrix) * train_to_test_ratio), len(input_matrix)):
        network.calculate(input_matrix[index_list[j]])
        w_err, err_val, MSE = network.correction(output_matrix[index_list[j]])
        tot_SSE += MSE

    return tot_SSE
    
def stochastic_train(
        network, input_set, output_set, 
        max_num_epochs, batch_size, train_factor):
   
    SSE_list = []
    for i in range(max_num_epochs):
        SSE_list.append(single_epoch(
            network, input_set, output_set, batch_size, train_factor))
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
        test_brain = Brain(data_dict)

    #Simple Test 
    in_data = 0.25
    print test_brain.predict(np.array([in_data]))
    print test_brain.learn(test_brain.trainingSet[0])
    print math.sin(in_data)
    print test_brain.predict(np.array([in_data]))

    #Use Pybrain to compare output results
#    compare_brain = FeedForwardNetwork()
#    inLayer = SigmoidLayer(data_dict["networkProperties"]["sizeInitialLayer"])
#    hiddenLayer = SigmoidLayer(data_dict["networkProperties"][
#        "hiddenLayerSizes"][0])
#    outLayer = SigmoidLayer(data_dict["networkProperties"]["numberOutputs"])
#    compare_brain.addInputModule(inLayer)
#    compare_brain.addModule(hiddenLayer)
#    compare_brain.addOutputModule(outLayer)
#    in_2_hid = FullConnection(inLayer, hiddenLayer)
#    hid_2_out = FullConnection(hiddenLayer, outLayer)
#    compare_brain.addConnection(in_2_hid)
#    compare_brain.addConnection(hid_2_out)
#    compare_brain.sortModules()

if __name__ == "__main__":
    main(sys.argv[1:])

