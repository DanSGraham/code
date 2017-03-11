"""Neural Network obect class specification

"""
#A neural network abstract class and concrete implementations.
# By DanG

#TODO:
#Allow each layer of FF to have a different activation fxn 
#Use Abstract Base Classes.
#Write DocStrings
#Code other Network Types
#Implement network save funcitonality

import json
import numpy as np
import time
import network_layer as nl

class NeuralNetwork(object):



    def __init__(self, input_dict):

        self.optimization = "backpropagation"
        self.use_bias = True
        self.activation_fxns = input_dict["networkProperties"][
            "activationFunctions"]

        self.properties = input_dict["networkProperties"]
        if "slopeParameter" in self.properties:
            self.slope_param = self.properties["slopeParameter"]

        if "useBias" in self.properties:
            self.use_bias = self.properties["useBias"]

        if "optimizationMethod" in self.properties:
            self.optimization = self.properties["optimizationMethod"]

    def calculate(self, input_data):

        raise NotImplementedError(
            "You have not implemented the calculate method")

    def correction(self):

        raise NotImplementedError(
            "You have not implemented the correction method")

    def adjustment(self):

        raise NotImplementedError(
            "You have not implemented the adjustment method")

    def export_network(self):

        raise NotImplementedError(
            "You have not implemented the export_network method")


class FFNeuralNetwork(NeuralNetwork):



    def __init__(self, input_dict):

        super(FFNeuralNetwork, self).__init__(input_dict)
        self.input_data = input_dict
        self.num_inputs = self.properties['numberInputs']
        self.num_outputs = self.properties["numberOutputs"]

    def calculate(self, input_data):

        pass

    def correction(self):

        pass

    def adjustment(self):

        pass

    def export_network(self):

        return json.JSONEncoder(self.input_data)


class SingleLayerPerceptron(FFNeuralNetwork):



    def __init__(self, input_dict):

        super(SingleLayerPerceptron, self).__init__(input_dict)
        self.num_neurons = self.num_outputs
        self.network = []
        self.network.append(HiddenLayer(
            (self.num_neurons, self.num_inputs), (self.num_neurons, 1)))

    def calculate(self, input_stimulus):

        #input_stiumulus is a 1D array in bra form
        self.data_layers = [input_stimulus]
        activation_input = (
            np.multiply(self.slope_param, 
            self.network_weights.dot(input_stimulus))
            + self.network_bias
        )
        self.data_layers.append(self.network[0].activate(activation_input))
        return self.activated_values

    def correction(self, target_values):

        deriv_act_fun = self.d_activation_function(
            self.activation_input[-1], self.slope_param)
        self.error = np.multiply(self.cost_function(self.data_layers[-1], 
            target_values), deriv_act_fun)
        self.weights_error = np.multiply(self.error.T, self.data_layers[0])
        square_sum_error = np.divide(
            np.sum(np.square(self.data_layers[-1] - target_values)), 
            len(target_values))
        return (self.weights_error, self.error, square_sum_error)

    def adjustment(self, weights_adjust, bias_adjust):

        self.network_weights = self.network_weights - weights_adjust
        if self.use_bias:
            self.bias_weights = self.bias_weights - bias_adjust

    def export_network(self):
        
        return json.JSONEncoder(self.input_data)


class MultiLayerPerceptron(FFNeuralNetwork):



    def __init__(self, input_data):

        super(MultiLayerPerceptron, self).__init__(input_data)
        self.num_hidden_layers = self.properties["numberHiddenLayers"]
        self.hidden_layer_sizes = self.properties["hiddenLayerSizes"]
        self.num_output_neurons = self.properties["numberOutputs"]
        self.network_layers = []

        input_layer = nl.InputLayer((self.num_inputs, 1), (self.num_inputs, 1))
        self.network_layers.append(input_layer)

        temp_inputs = self.num_inputs
        for i in range(self.num_hidden_layers):
            layer_size = self.hidden_layer_sizes[i]
            hidden_layer = nl.HiddenLayer((layer_size, temp_inputs), 
                                       (layer_size, 1))

            self.network_layers.append(hidden_layer)
            temp_inputs = layer_size

        #Create output layer:
        output_layer = nl.OutputLayer((self.num_output_neurons, temp_inputs), 
                                      (self.num_output_neurons, 1), 
                                      activation_fxn=self.activation_fxns[-1])

        self.network_layers.append(output_layer)

        #Establish the connections
        for i in range(len(self.network_layers)-2, -1, -1):
            self.network_layers[i].connect_next_layer(self.network_layers[i + 1])

        for j in range(1, len(self.network_layers)):
            self.network_layers[j].connect_prev_layer(self.network_layers[j - 1])

    def calculate(self, input_values):

        #input stimulus is a 1D array in bra form 
        self.data_layers = [input_values]
        for layer in self.network_layers:
            data_output = layer.activate(self.data_layers[-1])
            self.data_layers.append(data_output)
        return self.data_layers[-1] 

    def correction(self, target_values):
        
        #Generate the error matrices to make adjustments.
        #Iterate backwards through layers calculating error.
        self.error_list = []    #This list must be flipped around at the end.
        self.weights_error = [] #This must also be flipped
        #OutputError first
        w_err, err, total_err = self.network_layers[-1].correction(target_values)
        self.error_list.append(err)
        self.weights_error.append(w_err)
        for i in range((len(self.network_layers) - 2), -1, -1):
            w_err, err, t_e = self.network_layers[i].correction(self.error_list[-1])
            self.error_list.append(err)
            self.weights_error.append(w_err)

        self.error_list = list(reversed(self.error_list))
        self.weights_error = list(reversed(self.weights_error))
        return (self.weights_error, self.error_list,  total_err)

    def adjustment(self, weights_adjust, bias_adjust):

        #Adjust the weights and biases to correct network.
        for i in range(len(self.network_layers)):
            self.network_layers[i].adjust(weights_adjust[i], bias_adjust[i])




class RNeuralNetwork(NeuralNetwork):



    def __init__(self, input_data):
        super(RFNeuralNetwork, self).__init__(input_dict)
        self.input_data = input_dict
        self.input_size = self.properties['inputSize']
        self.output_size = self.properties["outputSize"]


class RecurrantMultiLLayerPerceptron(RNeuralNetwork):



    def __init__(self, input_data):

        super(RecurrantMultiLayerPerceptron, self).__init__(input_data)
        self.num_hidden_layers = self.properties["numberHiddenLayers"]
        self.hidden_layer_sizes = self.properties["hiddenLayerSizes"]
        self.num_output_neurons = self.properties["numberOutputs"]
        self.network_layers = []

        input_layer = nl.InputLayer((self.num_inputs, 1), (self.num_inputs, 1))
        self.network_layers.append(input_layer)

        temp_inputs = self.num_inputs
        for i in range(self.num_hidden_layers):
            layer_size = self.hidden_layer_sizes[i]
            hidden_layer = nl.HiddenLayer((layer_size, temp_inputs), 
                                       (layer_size, 1))

            self.network_layers.append(hidden_layer)
            temp_inputs = layer_size

        #Create output layer:
        output_layer = nl.OutputLayer((self.num_output_neurons, temp_inputs), 
                                      (self.num_output_neurons, 1), 
                                      activation_fxn=self.activation_fxns[-1])

        self.network_layers.append(output_layer)

        #Establish the connections
        for i in range(len(self.network_layers)-2, -1, -1):
            self.network_layers[i].connect_next_layer(self.network_layers[i + 1])

        for j in range(1, len(self.network_layers)):
            self.network_layers[j].connect_prev_layer(self.network_layers[j - 1])

    def calculate(self, input_values):

        #input stimulus is a 1D array in bra form 
        self.data_layers = [input_values]
        for layer in self.network_layers:
            data_output = layer.activate(self.data_layers[-1])
            self.data_layers.append(data_output)
        return self.data_layers[-1] 

    def correction(self, target_values):
        
        #Generate the error matrices to make adjustments.
        #Iterate backwards through layers calculating error.
        self.error_list = []    #This list must be flipped around at the end.
        self.weights_error = [] #This must also be flipped
        #OutputError first
        w_err, err, total_err = self.network_layers[-1].correction(target_values)
        self.error_list.append(err)
        self.weights_error.append(w_err)
        for i in range((len(self.network_layers) - 2), -1, -1):
            w_err, err, t_e = self.network_layers[i].correction(self.error_list[-1])
            self.error_list.append(err)
            self.weights_error.append(w_err)

        self.error_list = list(reversed(self.error_list))
        self.weights_error = list(reversed(self.weights_error))
        return (self.weights_error, self.error_list,  total_err)

    def adjustment(self, weights_adjust, bias_adjust):

        #Adjust the weights and biases to correct network.
        for i in range(len(self.network_layers)):
            self.network_layers[i].adjust(weights_adjust[i], bias_adjust[i])




class HopfieldNetwork(RNeuralNetwork):



    pass



class BoltzmannMachine(RNeuralNetwork):



    pass



class LongShortTermMemory(RNeuralNetwork):



    pass



class StochasticNetwork(RNeuralNetwork):



    pass


def backpropagation_intime():
    pass

def genetic_algorithm():
    pass

def continuous_genetic_algorithm():
    pass

def Tabu_search():
    pass

def simulated_annealing():
    pass

def particle_swarm_optimization():
    pass

def wavelet_transforms():
    pass

def some_kind_of_hybrid():
    pass



def create_network(inputFile):


    input_data = inputFile

    if (input_data["networkClass"] == "Feedforward"):
        if(input_data["networkType"] == "SLPercep"):
            return SingleLayerPerceptron(input_data)
        if(input_data["networkType"] == "MLPercep"):
            return MultiLayerPerceptron(input_data)

