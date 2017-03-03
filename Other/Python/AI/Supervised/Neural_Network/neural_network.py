#A neural network abstract class and concrete implementations.
# By DanG

#TODO:
#Use Abstract Base Classes.
#Write DocStrings
#Clean up code
#Optimize MLPercpetron
#Code other Network Types
#Implement network save funcitonality

import json
import numpy as np
import time


class NeuralNetwork(object):



    def __init__(self, input_dict):

        self.activation_function = log_sigmoid 
        self.d_activation_function = d_log_sigmoid
        self.slope_param = 1.0
        self.cost_function = quad_cost_grad
        self.optimization = "backpropagation"
        self.use_bias = True

        self.properties = input_file["networkProperties"]
        if "activationFunction" in self.properties:
            if self.properties["activationFunction"] == "tanh":
                self.activation_function = tan_hyperbolic
                self.d_activation_function = d_tan_hyperbolic
        if "slopeParameter" in self.properties:
            self.slope_param = self.properties["slopeParameter"]

        if "useBias" in self.properties:
            self.use_bias = self.properties["useBias"]

        if "costFunction" in self.properties:
            cFun = self.properties["costFunction"]
            if cFun == "Quadratic":
                self.cost_function = quad_cost_grad
            if cFun == "CrossEntropy":
                self.cost_function = cross_entropy_cost_grad
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
        self.network_weights = np.random.uniform(-1, 1, 
            (self.num_neurons, self.num_inputs))
        self.bias_weights = np.random.uniform(-1, 1, 
            (self.num_neurons))

    def calculate(self, input_stimulus):

        #input_stiumulus is a 1D array in bra form
        self.data_layers = [input_stimulus]
        self.activation_input = [
            np.multiply(self.slope_param, 
            self.network_weights.dot(input_stimulus))
            + self.bias_weights
        ]
        self.data_layers.append(self.activation_function(self.last_output))
        return self.activated_values

    def correction(self, target_values):

        deriv_act_fun = self.d_activation_function(
            self.activation_input[-1], self.slope_param)
        self.error = np.multiply(self.cost_function(self.data_layers[-1], 
            target_values), deriv_act_fun)
        return self.error

    def adjustment(self, weights_adjust, bias_adjust):

        self.network_weights = self.network_weights - weights_adjust
        self.bias_weights = self.bias_weights - bias_adjust

    def export_network(self):
        
        return json.JSONEncoder(self.input_data)


class MultiLayerPerceptron(FFNeuralNetwork):



    def __init__(self, input_data):

        super(MultiLayerPerceptron, self).__init__(input_data)
        self.size_init_layer = self.properties["sizeInitialLayer"]
        self.num_hidden_layers = self.properties["numberHiddenLayers"]
        self.hidden_layer_sizes = self.properties["hiddenLayerSizes"]
        self.num_output_neurons = self.properties["numberOutputs"]
        self.normalize_input = self.properties["normalizeInputs"]
        self.network_weights = []
        self.network_bias = []

        if self.normalize_input:
            self.network_weights.append(
                np.random.uniform(-1, 1, (self.num_inputs)))
            self.network_bias.append(
                np.random.uniform(-1, 1, (self.num_inputs)))

        #Create Input Layer:
        self.network_weights.append(
            np.random.uniform(-1, 1, (self.size_init_layer, self.num_inputs)))
        self.network_bias.append(
            np.random.uniform(-1, 1, (self.size_init_layer)))

        temp_inputs = self.size_init_layer
        for i in range(self.num_hidden_layers):
            layer_size = self.hidden_layer_sizes[i]
            self.network_weights.append(
                np.random.uniform(-1, 1, (layer_size, temp_inputs)))
            self.network_bias.append(
                np.random.uniform(-1, 1, (layer_size)))
            temp_inputs = layer_size

        #Create output layer:
        self.network_weights.append(
            np.random.uniform(-1, 1, (self.num_output_neurons, temp_inputs)))
        self.network_bias.append(
            np.random.uniform(-1, 1, (self.num_output_neurons)))

        if not self.use_bias:
            for bias_layer in self.network_bias:
                bias_layer.fill(0.0)

    def calculate(self, input_values):

        #input stimulus is a 1D array in bra form 
        self.data_layers = [input_values]
        self.activation_input = []

        iter_val = range(len(self.network_weights))
        if self.normalize_input:
            self.activation_input.append(
                np.multiply(self.slope_param, np.multiply(self.data_layers[-1],
                self.network_weights[0]) + self.network_bias[0]))
            self.data_layers.append(
                self.activation_function(self.activation_input[-1]))
            iter_val = range(1,len(self.network_weights)) 

        for i in iter_val:
            self.activation_input.append(
                np.multiply(self.slope_param, 
                np.dot(self.network_weights[i], self.data_layers[-1])
                + self.network_bias[i]))
            self.data_layers.append(
                self.activation_function(self.activation_input[-1]))
        
        return self.data_layers[-1] 

    def correction(self, target_values):
        
        #Generate the error matrices to make adjustments.
        #Iterate backwards through layers calculating error.
        self.error_list = []    #This list must be flipped around at the end.
        self.weights_error = [] #This must also be flipped
        #OutputError first
        self.error_list.append(
            np.multiply(
                self.cost_function(self.data_layers[-1], target_values),
                self.d_activation_function(
                    self.activation_input[-1], self.slope_param)))
        
       #Need to calculate the weight error outside in the train function 
        self.weights_error.append(
            np.multiply(np.array([self.error_list[-1]]).T, 
            np.array([self.data_layers[-2]])))

        for i in range((len(self.network_weights)-2), -1, -1):
            self.error_list.append(
                np.multiply(np.dot(self.network_weights[i + 1].T, 
                self.error_list[-1]), 
                self.d_activation_function(self.activation_input[i], 
                self.slope_param)))
            self.weights_error.append(
                np.multiply(np.array([self.error_list[-1]]).T, 
                np.array([self.data_layers[i]])))

        #Multiply by the correct adjustment and return
        self.error_list = list(reversed(self.error_list))
        self.weights_error = list(reversed(self.weights_error))    #Weights error calculated outside in train function
        square_sum_error = np.divide(
            np.sum(np.square(self.data_layers[-1] - target_values)), 
            len(target_values))
        return (self.error_list, square_sum_error)        

    def adjustment(self, weights_adjust, bias_adjust):

        #Adjust the weights and biases to correct network.
        for i in range(len(self.network_weights)):
            self.network_weights[i] = np.subtract(self.network_weights[i], 
                weights_adjust[i])
            self.network_bias[i] = np.subtract(self.network_bias[i], 
                bias_adjust[i])


class RNeuralNetwork(NeuralNetwork):



    def __init__(self, input_data):

        pass



class HopfieldNetwork(RNeuralNetwork):



    pass



class BoltzmannMachine(RNeuralNetwork):



    pass



class LongShortTermMemory(RNeuralNetwork):



    pass



class StochasticNetwork(RNeuralNetwork):



    pass

##--------------------------Activation Functions-------------------------------

def linear(input_stimulus):

    return input_stimulus

def d_linear(input_stimulus, slope_param=1.0):

    return slope_param

def log_sigmoid(input_stimulus):

    #Returns a value from 0 to 1 and has a variable slope.
    sig_val = np.divide(1.0, (1.0 + (np.exp(
                  np.multiply(-1., input_stimulus)))))
    return sig_val
		
def d_log_sigmoid(input_stimulus, slope_param=1.0):

    #Returns the derivative of the log_sigmoid activation function.
    #The derivative is used when determing the error in a neuron.
    sig_derivative = np.divide(slope_param, 
                         np.multiply(2.0, np.cosh(input_stimulus)) + 2)
    return sig_derivative
	
def tan_hyperbolic(input_stimulus):

    # Returns a value from -1 to 1. Similar to log_sigmoid but 
    # offers negative values.
    hyp_value = np.tanh(input_stimulus)
    return hyp_value
		
def d_tan_hyperbolic(input_stimulus, slope_param=1.0):

    # Returns the derivative of the tan_hyperbolic fxn.
    d_hyp_value = slope_param * np.square((np.sech(input_stimulus)))
    return d_hype_value

##----------------------------Cost Function Gradients--------------------------

#Many found here: http://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications

def quad_cost_grad(output_vector, target_vector):

    return (output_vector - target_vector)

def cross_entropy_cost_grad(output_vector, target_vector):

    return np.divide((output_vector - target_vector), 
                     ((1. - output_vector) * output_vector))

def exponential_cost_grad(output_vector, target_vector, t_param=1.0):

    #Not sure if this is right. Need to check.
    exp_val = (1. / t_param) * np.sum((output_vector - target_vector) ** 2.)
    cost_val = t_param * np.exp(exp_val)
    coeff_vector = (2./t_param) * (output_vector - target_vector)
    return coeff_vector * cost_val 

def Hellinger_distance_grad(output_vector, target_vector):

    #Requires positive values
    return (np.sqrt(output_vector) - np.sqrt(target_vector)) \
           / (np.sqrt(2) * np.sqrt(output_vector))

def Kullback_Leibler_divergence_grad(output_vector, target_vector):

    return -1 * np.divide(target_vector, output_vector)

def gen_Kullback_Leibler_divergence_grad(output_vector, target_vector):

    return -1 * (np.divide((target_vector + output_vector), output_vector))

def Itakura_Saito_distance_grad(output_vector, target_vector):

    return np.divide((output_vector - target_vector), (output_vector) ** 2.)

##----------------------------Optimization Algorithms--------------------------

def backpropagation():
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

##-----------------------------------------------------------------------------


def create_network(inputFile):


    input_data = inputFile

    if (input_data["networkClass"] == "Feedforward"):
        if(input_data["networkType"] == "SLPercep"):
            return SingleLayerPerceptron(input_data)
        if(input_data["networkType"] == "MLPercep"):
            return MultiLayerPerceptron(input_data)

