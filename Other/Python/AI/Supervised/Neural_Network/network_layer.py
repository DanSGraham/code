#A module to define layer classes
#By DanG

import functions




class Layer(object):



    def __init__(self, weights, bias, activation_fxn, slope_param=0.01):
        
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

        self.weights = weights
        self.bias = bias
        self.slope_param = slope_param

    def activate(self, input_vector):
        self.activation_input = input_vector
        return self.activation_fxn(input_vector) 

    def correction(self, cost, input_vals):

        return np.multiply(cost, self.d_activation_fxn)

    def adjust(self, weights_corr, bias_corr):

        raise NotImplementedError("adjust not implemented")

