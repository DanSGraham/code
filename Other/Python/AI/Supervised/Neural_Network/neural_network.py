#A neural network abstract class and concrete implementations.
# By DanG

import json
import numpy as np
import time

class NeuralNetwork(object):

    def __init__(self, input_file):
        self.activation_function = log_sigmoid 
        self.d_activation_function = d_log_sigmoid
        self.cost_function = quad_cost_grad

        self.optimization = "backpropagation"
        self.use_bias = True
        self.properties = input_file["networkProperties"]
        self.gradient_eta = 1.0
        self.batch_size = 1.0
        if "activationFunction" in self.properties:
            if self.properties["activationFunction"] == "tanh":
                self.activation_function = tan_hyperbolic
                self.d_activation_function = d_tan_hyperbolic

        if "useBias" in self.properties:
            self.use_bias = self.properties["useBias"]

        if "optimizationMethod" in self.properties:
            self.optimization = self.properties["optimizationMethod"]

    def calculate(self, input_data):
        raise NotImplementedError("You have not implemented the calculate method")

    def correction(self):
        raise NotImplementedError("You have not implemented the correction method")

    def export_network(self):
        raise NotImplementedError("You have not implemented the export_network method")


class FNeuralNetwork(NeuralNetwork):

    def __init__(self, input_data):
        super(FNeuralNetwork, self).__init__(input_data)
        self.input_data = input_data
        self.num_inputs = self.properties['numberInputs']

    def calculate(self, input_data):
        pass

    def correction(self):
        pass

    def export_network(self):
        return json.JSONEncoder(self.input_data)

class SingleLayerPerceptron(FNeuralNetwork):

    def __init__(self, input_data):
        super(SingleLayerPerceptron, self).__init__(input_data)
        self.num_neurons = self.properties["numberOutputs"]
        self.network_weights = np.random.uniform(-1, 1, (self.num_neurons, self.num_inputs))
        self.bias_weights = np.random.uniform(-1, 1, (self.num_neurons))
        self.correction_alg = self.gradient_descent
        if not self.use_bias:
            self.bias_weights = np.zeros(self.num_neurons)
        

    def calculate(self, input_stimulus):
        #input_stiumulus is a 1D array in bra form
        self.last_input = input_stimulus
        self.last_output = self.network_weights.dot(input_stimulus) + self.bias_weights
        self.activated_values = self.activation_function(self.last_output)
        return self.activated_values

    def correction(self, true_values):
        if self.optimization == "backpropagation":
           self.error = np.dot(self.cost_function(self.activated_values, true_values), self.d_activation_function(self.last_output + self.bias_weights))
           self.gradient_descent()

    def gradient_descent(self):
        self.newtork_weights = self.network_weights - (self.gradient_eta / self.batch_size) * np.dot(self.error, self.last_input)
        self.bias_weights = self.error

    def export_network(self):
        return json.JSONEncoder(self.input_data)


class MultiLayerPerceptron(FNeuralNetwork):

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
            self.network_weights.append(np.random.uniform(-1, 1, (self.num_inputs, 1)))
            self.network_bias.append(np.random.uniform(-1, 1, (self.num_inputs, 1)))

        #Create Input Layer:
        self.network_weights.append(np.random.uniform(-1, 1, (self.size_init_layer, self.num_inputs)))
        self.network_bias.append(np.random.uniform(-1, 1, (self.size_init_layer, self.num_inputs)))

        temp_input_size = self.size_init_layer
        for i in range(self.num_hidden_layers):
            layer_size = self.hidden_layer_sizes[i]
            self.network_weights.append(np.random.uniform(-1, 1, (layer_size, temp_input_size)))
            self.network_bias.append(np.random.uniform(-1, 1, (layer_size, temp_input_size)))
            temp_inputs = layer_size

        #Create output layer:
        self.network_weights.append(np.random.uniform(-1, 1, (self.num_output_neurons, temp_inputs)))
        self.network_bias.append(np.random.uniform(-1, 1, (self.num_output_neurons, temp_inputs)))

        if not self.use_bias:
            for bias_layer in self.network_bias:
                bias_layer.fill(0.0)

        def calculate(self, input_values):
           #input stimulus is a 1D array in bra form 
            #Need to check this and account for normalization. Also rename input_layers. This will store the output of each layer which is the input of the next.
            self.input_layers = [input_values]
            self.activation_input = []
            self.output_vals = []
            for i in range(len(self.network_weights)):
                self.activation_input.append(self.network_weights[i].dot(self.input_layers[-1])\
                                             + self.network_bias[i])
                self.input_layers.append(self.activation_function(self.activation_input[-1]) 
                
        def correction(self, true_values):
            pass


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

def log_sigmoid(input_stimulus, slope_param=1.0):
    #Returns a value from 0 to 1 and has a variable slope.
    sig_val = 1.0 / (1.0 + (np.exp(-1. * slope_param * input_stimulus)))
    return sig_val
		
def d_log_sigmoid(input_stimulus, bias_vector, slope_param=1.0):
    #Returns the derivative of the log_sigmoid activation function.
    #The derivative is used when determing the error in a neuron.
    sig_derivative = (slope_param * np.exp(slope_param * input_stimulus + bias_vector))\
                      / (np.square(np.exp(bias_vector) + \
                      (np.exp(slope_param * input_stimulus))))
    return sig_derivative
	
def tan_hyperbolic(input_stimulus, slope_param=1.0):
    # Returns a value from -1 to 1. Similar to log_sigmoid but 
    # offers negative values.
    hyp_value = np.tanh(input_stimulus * slope_param)
    return hyp_value
		
def d_tan_hyperbolic(input_stimulus, bias_vector, slope_param=1.0):
    # Returns the derivative of the tan_hyperbolic fxn.
    d_hyp_value = slope_param * (np.sech(bias_vector - input_stimulus * slope_param)) ** 2
    return d_hype_value

##-----------------------------------------------------------------------------

##----------------------------Cost Function Gradients--------------------------

#Many found here: http://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications

def quad_cost_grad(output_vector, truth_vector):
    return (output_vector - truth_vector)

def cross_entropy_cost_grad(output_vector, truth_vector):
    return np.divide((output_vector - truth_vector), ((1. - output_vector) * output_vector))

def exponential_cost_grad(output_vector, truth_vector, t_param=1.0):
    #Not sure if this is right. Need to check.
    exp_val = (1. / t_param) * np.sum((output_vector - truth_vector) ** 2.) 
    cost_val = t_param * np.exp(exp_val)
    coeff_vector = (2./t_param) * (output_vector - truth_vector)
    return coeff_vector * cost_val 

def Hellinger_distance_grad(output_vector, truth_vector):
    #Requires positive values
    return (np.sqrt(output_vector) - np.sqrt(truth_vector)) \
           / (np.sqrt(2) * np.sqrt(output_vector))

def Kullback_Leibler_divergence_grad(output_vector, truth_vector):
    return -1 * np.divide(truth_vector, output_vector)

def gen_Kullback_Leibler_divergence_grad(output_vector, truth_vector):
    return -1 * (np.divide((truth_vector + output_vector), output_vector))

def Itakura_Saito_distance_grad(output_vector, truth_vector):
    return np.divide((output_vector - truth_vector), (output_vector) ** 2.)

##-----------------------------------------------------------------------------

##----------------------------Optimization Algorithms--------------------------

def backpropagation(err_vector, wghts_matrix, deriv_vector, lrn_rate=1.0):
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

    input_data = json.load(inputFile)

    if (input_data["networkClass"] == "Feedforward"):
        if(input_data["networkType"] == "SLPercep"):
            return SingleLayerPerceptron(input_data)
        if(input_data["networkType"] == "MLPercep"):
            return MultiLayerPerceptron(input_data)
