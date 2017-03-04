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


            self.gradient_method = standard
            self.momentum = 0.9
            self.smoothing = 10 ** (-8)
            self.pVelocity = []
            self.prev_error_mat = []
            self.delta_factor = 0.9
            self.average_error = []
            for layer in self.network.network_weights:
                self.pVelocity.append(np.zeros(layer.shape))

            if "gradientMethod" in networkInputFile["trainingProperties"]:
                train_prop = networkInputFile["trainingProperties"]
                if train_prop["gradientMethod"] == "Standard":
                    self.gradient_method = standard

       
                if train_prop["gradientMethod"] == "Momentum":
                    self.gradient_method = momentum
                    self.momentum = train_prop["momentumFactor"]

                if train_prop["gradientMethod"] == "Nesterov":
                    self.gradient_method = Nesterov_acc
                    self.momentum = train_prop["momentumFactor"]

                if train_prop["gradientMethod"] == "Adagrad":
                    self.gradient_method = adagrad
                    self.smoothing = train_prop["smoothingFactor"]

                if train_prop["gradientMethod"] == "Adadelta":
                    self.gradient_method = adadelta
                    self.delta_factor = train_prop["deltaFactor"]

                if train_prop["gradientMethod"] == "RMSprop":
                    self.gradient_method = RMSprop
                    self.delta_factor = train_prop["deltaFactor"]

                if train_prop["gradientMethod"] == "Adam":
                    self.gradient_method = adam
                    self.momentum = train_prop["momentumFactor"]
                if train_prop["gradientMethod"] == "gradientNoise":
                    self.gradient_method = gradient_noise
                    self.momentum = train_prop["momentumFactor"]

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
                self.bSize, self.tFactor, self.maxEpochs
            )

    def predict(self, inputSet):

        """Predicts an output based on the trained values"""
        return self.network.calculate(inputSet)

    def evolve(self):

        """Grows new neurons and links. Trims trivial neurons and links"""

##----------------------Training Methods---------------------------------------

def batch_train(brain, input_set, output_set, batch_size, train_factor, epochs=1):

    network = brain.network
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

        weights_error = brain.gradient_method(
            weights_error, (float(brain.tFactor)/batch_size), 
            brain.pVelocity, brain.momentum, brain.smoothing)

        brain.pVelocity = weights_error

        for n in range(len(weights_error)):
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
        
        weights_error = brain.gradient_method(
            weights_error, (float(brain.tFactor)/batch_size), 
            brain.pVelocity, brain.momentum, brain.smoothing)

        brain.pVelocity = weights_error

        for n in range(len(weights_error)):
            bias_error[n] = np.multiply(
                (float(train_factor) / batch_size), bias_error[n])

    network.adjustment(weights_error, bias_error)
    return True

def online_train(brain, input_set, output_set, batch_size, train_factor, epochs=1):

    return batch_train(brain, input_set, output_set, 1, train_factor, epochs)

def single_epoch(
        brain, input_matrix, output_matrix, 
        minibatch_size, train_factor, train_to_test_ratio=0.7):

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
        w_err, err_val, MSE = network.correction(output_matrix[index_list[j]])
        tot_SSE += MSE

    return tot_SSE
    
def stochastic_train(
        brain, input_set, output_set, 
        batch_size, train_factor, max_epochs):

    network = brain.network 
    SSE_list = []
    for i in range(max_epochs):
        SSE_list.append(single_epoch(
            brain, input_set, output_set, batch_size, train_factor))
    return SSE_list


##--------------------------Gradient Descent Improvements----------------------
#Found here: http://sebastianruder.com/optimizing-gradient-descent/ 
def standard(weight_error, train_factor, prev_velocity=1, momentum_factor=1, smoothing_factor=1):
    corr_err = [] 
    for weight in weight_error:
        corr_err.append(np.multiply(train_factor, weight))
    return corr_err

def momentum(weight_error, train_factor, prev_velocity, momentum_factor, smoothing_factor=1):

    corr_err = []
    for i in range(len(weight_error)):
        corr_err.append(np.multiply(momentum_factor, prev_velocity[i])
            + np.multiply(train_factor, weight_error[i]))
    return corr_err

def Nesterov_acc():
    pass

def adagrad(weight_error, train_factor, smoothing_factor):
    #Smoothig factor on the order of 10^-8
    pass

def adadelta(weight_error, train_factor, prev_velocity, momentum_factor, smoothing_factor):
    pass

def RMSprop():
    pass

def adam():
    pass

def gradient_noise():
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

