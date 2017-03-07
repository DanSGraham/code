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

        self.cost_function = quad_cost_grad
        self.optimization = "backpropagation"
        self.use_bias = True
        self.activation_fxns = input_dict["networkProperties"][
            "activationFunctions"]

        self.properties = input_dict["networkProperties"]
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
        self.network = []

        input_layer = nl.InputLayer((self.num_inputs, 1), (self.num_inputs, 1))
        self.network.append(input_layer)

        temp_inputs = self.num_inputs
        for i in range(self.num_hidden_layers):
            layer_size = self.hidden_layer_sizes[i]
            hidden_layer = nl.HiddenLayer((layer_size, temp_inputs), 
                                       (layer_size, 1))

            self.network.append(hidden_layer)
            temp_inputs = layer_size

        #Create output layer:
        output_layer = nl.OutputLayer((self.num_output_neurons, temp_inputs), 
                                   (self.num_output_neurons, 1))

        self.network.append(output_layer)

        #Establish the connections
        for i in range(len(self.network)-2, -1, -1):
            self.network[i].next_layer(self.network[i + 1])

    def calculate(self, input_values):

        #input stimulus is a 1D array in bra form 
        self.data_layers = [input_values]
        for layer in self.network:
            data_output = layer.activate(self.data_layers[-1])
            self.data_layers.append(data_output)
        return self.data_layers[-1] 

    def correction(self, target_values):
        
        #Generate the error matrices to make adjustments.
        #Iterate backwards through layers calculating error.
        self.error_list = []    #This list must be flipped around at the end.
        self.weights_error = [] #This must also be flipped
        #OutputError first
        w_err, err, total_err = self.network[-1].correction(target_values)
        self.error_list.append(err)
        self.weights_error.append(w_err)
        for i in range((len(self.network) - 2), -1, -1):
            w_err, err, t_e = self.network[i].correction(self.error_list[-1])
            self.error_list.append(err)
            self.weights_error.append(w_err)

        self.error_list = list(reversed(self.error_list))
        self.weights_error = list(reversed(self.weights_error))
        return (self.weights_error, self.error_list,  total_err)

    def adjustment(self, weights_adjust, bias_adjust):

        #Adjust the weights and biases to correct network.
        for i in range(len(self.network)):
            self.network[i].adjust(weights_adjust[i], bias_adjust[i])




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

def distance2(vector1, vector2):
    """Return the square distance between two vectors"""
    return np.sum(np.square(np.subtract(vector2, vector1)))

def create_network(inputFile):


    input_data = inputFile

    if (input_data["networkClass"] == "Feedforward"):
        if(input_data["networkType"] == "SLPercep"):
            return SingleLayerPerceptron(input_data)
        if(input_data["networkType"] == "MLPercep"):
            return MultiLayerPerceptron(input_data)

