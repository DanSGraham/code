#A module to define layer classes
#By DanG

import random
import numpy as np
import functions




class Layer(object):



    def __init__(
        self, weights_shape, bias_shape, 
        activation_fxn, slope_param=1.0, use_bias=True):
        
        self.activation_fxn = functions.log_sigmoid
        self.d_activation_fxn = functions.d_log_sigmoid

        if activation_fxn == "Heaviside":
            self.activation_fxn = functions.heaviside
            self.d_activation_fxn = functions.d_heaviside
        if activation_fxn == "Signum":
            self.activation_fxn = functions.signum
            self.d_activation_fxn = functions.d_signum
        if activation_fxn == "PiecewiseLinear":
            self.activation_fxn = functions.piece_wise_linear
            self.d_activation_fxn = functions.d_piece_wise_linear
        if activation_fxn == "Linear":
            self.activation_fxn = functions.linear
            self.d_activation_fxn = functions.d_linear
        if activation_fxn == "Sigmoid":
            self.activation_fxn = functions.log_sigmoid
            self.d_activation_fxn = functions.d_log_sigmoid
        if activation_fxn == "Tanh":
            self.activation_fxn = functions.tanh
            self.d_activation_fxn = functions.d_tanh
        if activation_fxn == "ArcTan":
            self.activation_fxn = functions.arc_tan
            self.d_activation_fxn = functions.d_arc_tan
        if activation_fxn == "Softsign":
            self.activation_fxn = functions.softsign
            self.d_activation_fxn = functions.d_softsign
        if activation_fxn == "Softplus":
            self.activation_fxn = functions.softplus
            self.d_activation_fxn = functions.d_softplus
        if activation_fxn == "Softmax":
            self.activation_fxn = functions.softmax
            self.d_activation_fxn = functions.d_softmax

        self.weights = np.random.uniform(-1, 1, weights_shape)
        self.use_bias = use_bias
        self.bias = 0.0
        if self.use_bias:
            self.bias = np.random.uniform(-1, 1, bias_shape)
        self.slope_param = slope_param

    def activate(self, input_vector):

        raise NotImplementedError("activate not implemented")

    def correction(self, cost, input_vals):

        raise NotImplementedError("correction not implemented")

    def adjust(self, weights_adjust, bias_adjust):

        self.weights -= weights_adjust
        if self.use_bias:
            self.bias -= bias_adjust



class FFInputLayer(Layer):




    def __init__(
        self, weights, bias, 
        activation_fxn="Linear", slope_param=1.0, use_bias=True):

        super(FFInputLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

    def activate(self, input_vector):

        self.input_vector = input_vector
        self.activation_input = (np.multiply(input_vector, self.weights)
            + self.bias)
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

    def connect_next_layer(self, next_layer):

        self.next_layer = next_layer

    def correction(self, error):

        self.error = np.multiply(
            np.dot(self.next_layer.weights.T, error), 
            self.d_activation_fxn(self.activation_input, self.slope_param))
        self.weights_error = np.multiply(self.error, self.input_vector)
        return self.weights_error, self.error,  None




class FFHiddenLayer(Layer):




    def __init__(
        self, weights, bias, 
        activation_fxn="Sigmoid", slope_param=1.0, use_bias=True):

        super(FFHiddenLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

    def activate(self, input_vector):

        self.input_vector = input_vector
        self.activation_input = np.dot(self.weights, input_vector) + self.bias
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

    #I don't like this but this is what I am thinking for backprop

    def connect_prev_layer(self, prev_layer):

        self.prev_layer = prev_layer

    def connect_next_layer(self, next_layer):

        self.next_layer = next_layer

    def correction(self, error):

        self.error = np.multiply(
            np.dot(self.next_layer.weights.T, error), 
            self.d_activation_fxn(self.activation_input, self.slope_param))

        self.weights_error = np.multiply(self.error, self.input_vector)
        return self.weights_error, self.error, None
        

class FFOutputLayer(Layer):

    def __init__(
        self, weights, bias, 
        activation_fxn="Linear", cost_fxn="Quadratic",  
        slope_param=1.0, use_bias=True):

        super(FFOutputLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

        if cost_fxn == "Quadratic":
            self.cost_fxn = functions.quad_cost
            self.cost_fxn_grad = functions.quad_cost_grad
        if cost_fxn == "CrossEntropy":
            self.cost_fxn = functions.cross_entropy_cost
            self.cost_fxn_grad = functions.cross_entropy_cost_grad
        if cost_fxn == "Exponential":
            #Needs T param
            self.cost_fxn = functions.exponential_cost
            self.cost_fxn_grad = functions.exponential_cost_grad
        if cost_fxn == "HellingerDistance":
            self.cost_fxn = functions.Hellinger_distance
            self.cost_fxn_grad = functions.Hellinger_distance_grad
        if cost_fxn == "KullbackLeiblerDivergence":
            self.cost_fxn = functions.Kullback_Leibler_divergence
            self.cost_fxn_grad = functions.Kullback_Leibler_divergence_grad
        if cost_fxn == "GenKullbackLeiblerDivergence":
            self.cost_fxn = functions.gen_Kullback_Leibler_divergence
            self.cost_fxn_grad = functions.gen_Kullback_Leibler_divergence_grad
        if cost_fxn == "ItakuraSaitoDistance":
            self.cost_fxn = functions.Itakura_Saito_distance
            self.cost_fxn_grad = functions.Itakura_Saito_distance_grad

    def connect_prev_layer(self, prev_layer):

        self.prev_layer = prev_layer

    def activate(self, input_vector):

        self.input_vector = input_vector
        self.activation_input = np.dot(self.weights, input_vector) + self.bias
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

    def correction(self, target):

        self.error = np.multiply(
            self.cost_fxn_grad(self.output, target), 
            self.d_activation_fxn(self.activation_input, self.slope_param))
        self.weights_error = np.multiply(self.error, self.input_vector.T)
        self.total_error = self.cost_fxn(self.output, target)
        return self.weights_error, self.error, self.total_error

class RInputLayer(FFInputLayer):

    def __init__(
        self, weights, bias,
        activation_fxn="Linear", slope_param=1.0, use_bias=True):

        super(RInputLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

        self.internal_weights = np.random.uniform(-1, 1, (self.weights.shape[0], 1))
        self.output = 0.0

    def activate(self, input_vector):
        self.input_vector = input_vector
        self.activation_input = (np.multiply(self.weights, input_vector) 
            + np.multiply(self.internal_weights, self.output) + self.bias)
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

        
    
class RHiddenLayer(FFHiddenLayer):

    def __init__(
        self, weights, bias,
        activation_fxn="Sigmoid", slope_param=1.0, use_bias=True):

        super(RHiddenLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

        self.internal_weights = np.random.uniform(-1, 1, (self.weights.shape[0], 1))
        self.output = 0.0

    def activate(self, input_vector):
        self.input_vector = input_vector
        self.activation_input = (np.dot(self.weights, input_vector) 
            + np.multiply(self.internal_weights, self.output) + self.bias)
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

class ROutputLayer(FFOutputLayer):

    def __init__(
        self, weights, bias,
        activation_fxn="Linear", cost_fxn="Quadratic", 
        slope_param=1.0, use_bias=True):

        super(RInputLayer, self).__init__(
            weights, bias, activation_fxn, cost_fxn, slope_param, use_bias)

        self.internal_weights = np.random.uniform(-1, 1, (self.weights.shape[0], 1))
        self.output = 0.0

    def activate(self, input_vector):
        self.input_vector = input_vector
        self.activation_input = (np.dot(self.weights, input_vector) 
            + np.multiply(self.internal_weights, self.output) + self.bias)
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

