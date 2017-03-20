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

        self.use_bias = True

        self.properties = input_dict["networkProperties"]
        if "slopeParameter" in self.properties:
            self.slope_param = self.properties["slopeParameter"]

        if "useBias" in self.properties:
            self.use_bias = self.properties["useBias"]


        self.train_properties = input_dict["trainingProperties"]


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
        self.input_size = self.properties['inputSize']
        self.output_size = self.properties["outputSize"]

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
        self.num_neurons = self.output_size
        self.network = []
        self.network.append(HiddenLayer(
            (self.num_neurons, self.input_size), (self.num_neurons, 1)))

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
        self.num_output_neurons = self.properties["outputSize"]
        self.network_layers = []
        self.slope_param = 1.0

        #Training Info
        self.train_factor = 1.0
        self.momentum = 0.9
        self.smoothing = 10 ** (-8)
        self.delta_factor = 0.9

        if "trainingFactor" in self.train_properties:
            self.train_factor = self.train_properties["trainingFactor"]
        if "gradientMethod" in self.train_properties:
            self.gradient_method = self.train_properties["gradientMethod"]

        if "momentumFactor" in self.train_properties:
            self.momentum = self.train_properties["momentumFactor"]
        
         
        input_activation = "Linear"
        if "activationFunction" in self.properties["inputLayer"]:
            input_activation = self.properties["inputLayer"]["activationFunction"]

        input_layer = nl.FFInputLayer((self.input_size, 1), (self.input_size, 1), input_activation, self.gradient_method, self.train_factor, self.momentum, self.smoothing, self.delta_factor, self.slope_param, self.use_bias)
        self.network_layers.append(input_layer)

        temp_inputs = self.input_size

        #HiddenLayer Info
        if "activationFunctions" in self.properties["hiddenLayers"]:
            hidden_activation = self.properties["hiddenLayers"]["activationFunctions"]
        else:
            hidden_activation = "Sigmoid"
            
        for i in range(self.num_hidden_layers):
            layer_size = self.hidden_layer_sizes[i]
            if type(hidden_activation) == list:
                hidden_activation_unit = hidden_activation[i]
            else:
                hidden_activation_unit = hidden_activation
            hidden_layer = nl.FFHiddenLayer((layer_size, temp_inputs), 
                                       (layer_size, 1), hidden_activation_unit, self.gradient_method, self.train_factor, self.momentum, self.smoothing, self.delta_factor, self.slope_param, self.use_bias)

            self.network_layers.append(hidden_layer)
            temp_inputs = layer_size

        #Create output layer:
        output_activation = "Linear"
        cost_fxn = "Quadratic"
        if "activationFunction" in self.properties["outputLayer"]:
            output_activation = self.properties["outputLayer"]["activationFunction"]

        if "costFunction" in self.properties["outputLayer"]:
            cost_fxn = self.properties["outputLayer"]["costFunction"]

        output_layer = nl.FFOutputLayer((self.num_output_neurons, temp_inputs), 
                                      (self.num_output_neurons, 1), output_activation, self.gradient_method, cost_fxn, self.train_factor, self.momentum, self.smoothing, self.delta_factor, self.slope_param, self.use_bias)

        self.network_layers.append(output_layer)


    def calculate(self, input_values):

        self.data_layers = [np.array([input_values]).T]

        for layer in self.network_layers:
            data_output = layer.activate(self.data_layers[-1])
            self.data_layers.append(data_output)

        return self.data_layers[-1] 

    def correction(self, target_values):
        
        #Generate the error matrices to make adjustments.
        #Iterate backwards through layers calculating error.
        #OutputError first

        target_values = np.array([target_values]).T
        err, total_err = self.network_layers[-1].grad_correction(target_values)
        for i in range((len(self.network_layers) - 2), -1, -1):
            err, t_e = self.network_layers[i].grad_correction(
                np.dot(self.network_layers[i + 1].weights.T, err))

        return total_err

    def adjustment(self, batch_size):

        #Adjust the weights and biases to correct network.
        for i in range(len(self.network_layers)):
            self.network_layers[i].adjust(batch_size)




class RNeuralNetwork(NeuralNetwork):



    def __init__(self, input_data):
        super(RNeuralNetwork, self).__init__(input_data)
        self.input_data = input_data
        self.input_size = self.properties['inputSize']
        self.output_size = self.properties["outputSize"]


class RecurrantMultiLayerPerceptron(RNeuralNetwork):



    def __init__(self, input_data):

        super(RecurrantMultiLayerPerceptron, self).__init__(input_data)
        self.num_hidden_layers = self.properties["numberHiddenLayers"]
        self.hidden_layer_sizes = self.properties["hiddenLayerSizes"]
        self.num_output_neurons = self.properties["outputSize"]
        self.network_layers = []
        self.slope_param = 1.0

        #Training Info
        self.train_factor = 1.0
        self.momentum = 0.9
        self.smoothing = 10 ** (-8)
        self.delta_factor = 0.9
        backprop_trunc = float("inf")
        
        
        if "trainingFactor" in self.train_properties:
            self.train_factor = self.train_properties["trainingFactor"]
        if "gradientMethod" in self.train_properties:
            self.gradient_method = self.train_properties["gradientMethod"]

        if "momentumFactor" in self.train_properties:
            self.momentum = self.train_properties["momentumFactor"]
        
         
        input_activation = "Linear"
        if "activationFunction" in self.properties["inputLayer"]:
            input_activation = self.properties["inputLayer"]["activationFunction"]

        input_layer = nl.RInputLayer((self.input_size, 1), 
            (self.input_size, 1), input_activation, self.gradient_method, 
            self.train_factor, self.momentum, self.smoothing, 
            self.delta_factor, self.slope_param, self.use_bias, backprop_trunc)

        self.network_layers.append(input_layer)

        temp_inputs = self.input_size

        #HiddenLayer Info
        if "activationFunctions" in self.properties["hiddenLayers"]:
            hidden_activation = self.properties["hiddenLayers"]["activationFunctions"]
        else:
            hidden_activation = "Sigmoid"
            
        for i in range(self.num_hidden_layers):
            layer_size = self.hidden_layer_sizes[i]
            if type(hidden_activation) == list:
                hidden_activation_unit = hidden_activation[i]
            else:
                hidden_activation_unit = hidden_activation
            hidden_layer = nl.RHiddenLayer((layer_size, temp_inputs), 
                (layer_size, 1), hidden_activation_unit, self.gradient_method,
                self.train_factor, self.momentum, self.smoothing, 
                self.delta_factor, self.slope_param, self.use_bias, 
                backprop_trunc)

            self.network_layers.append(hidden_layer)
            temp_inputs = layer_size

        #Create output layer:
        output_activation = "Linear"
        cost_fxn = "Quadratic"
        if "activationFunction" in self.properties["outputLayer"]:
            output_activation = self.properties["outputLayer"]["activationFunction"]

        if "costFunction" in self.properties["outputLayer"]:
            cost_fxn = self.properties["outputLayer"]["costFunction"]

        output_layer = nl.ROutputLayer((self.num_output_neurons, temp_inputs), 
            (self.num_output_neurons, 1), output_activation,
            self.gradient_method, cost_fxn, self.train_factor, self.momentum, 
            self.smoothing, self.delta_factor, self.slope_param, self.use_bias,
            backprop_trunc)

        self.network_layers.append(output_layer)

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
        #OutputError first
        err, total_err = (
            self.network_layers[-1].grad_correction(target_values))

        for i in range((len(self.network_layers) - 2), -1, -1):
            err, t_e = (self.network_layers[i].grad_correction(
                np.dot(self.network_layers[i + 1].weights.T, err)))

        self.reset_memory()
        return total_err

    def reset_memory(self):
        for layer in self.network_layers:
            layer.refresh_memory()

    def adjustment(self, batch_size):

        #Adjust the weights and biases to correct network.
        for i in range(len(self.network_layers)):
            self.network_layers[i].adjust(batch_size)




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
    if (input_data["networkClass"] == "Recurrant"):
        if(input_data["networkType"] == "RMLPercep"):
            return RecurrantMultiLayerPerceptron(input_data)

