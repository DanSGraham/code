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

        if activation_fxn == "Linear":
            self.activation_fxn = functions.linear
            self.d_activation_fxn = functions.d_linear
        if activation_fxn == "Sigmoid":
            self.activation_fxn = functions.log_sigmoid
            self.d_activation_fxn = functions.d_log_sigmoid
        if activation_fxn == "Tanh":
            self.activation_fxn = functions.tan_hyperbolic
            self.d_activation_fxn = functions.d_tan_hyperbolicA

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



class InputLayer(Layer):




    def __init__(
        self, weights, bias, 
        activation_fxn="Linear", slope_param=1.0, use_bias=True):

        super(InputLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

    def activate(self, input_vector):
        self.input_vector = input_vector
        self.activation_input = (np.multiply(input_vector, self.weights)
            + self.bias)
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

    def next_layer(self, next_layer):
        self.next_layer = next_layer

    def correction(self, error):

        self.error = np.multiply(
            np.dot(self.next_layer.weights.T, error), 
            self.d_activation_fxn(self.activation_input, self.slope_param))
        self.weights_error = np.multiply(self.error, self.input_vector)
        return self.weights_error, self.error,  None




class HiddenLayer(Layer):




    def __init__(
        self, weights, bias, 
        activation_fxn="Sigmoid", slope_param=1.0, use_bias=True):

        super(HiddenLayer, self).__init__(
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
        

class OutputLayer(Layer):

    def __init__(
        self, weights, bias, 
        activation_fxn="Linear", cost_fxn="Quadratic",  
        slope_param=1.0, use_bias=True):

        super(OutputLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

        if cost_fxn == "Quadratic":
            self.cost_fxn = functions.quad_cost
            self.cost_fxn_grad = functions.quad_cost_grad
        if cost_fxn == "CrossEntropy":
            self.cost_fxn = functions.cross_entropy_cost
            self.cost_fxn_grad = functions.cross_entropy_cost_grad
        if cost_fxn == "":
            pass

    def connect_prev_layer(self, prev_layer):
        self.prev_layer = prev_layer

    def activate(self, input_vector):

        self.input_vector = input_vector
        self.activation_input = np.dot(self.weights, input_vector) + self.bias
        self.output = self.activation_fxn(
            self.slope_param, self.activation_input)
        return self.output

    def correction(self, target):
        self.error = np.multiply(
            self.cost_fxn_grad(self.output, target), 
            self.d_activation_fxn(self.activation_input, self.slope_param))
        self.weights_error = np.multiply(self.error, self.input_vector.T)
        self.total_error = self.cost_fxn(self.output, target)
        return self.weights_error, self.error, self.total_error
