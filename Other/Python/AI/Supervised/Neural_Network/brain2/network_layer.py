#A module to define layer classes
#By DanG

import random
import numpy as np
import functions




class Layer(object):



    def __init__(
        self, weights_shape, bias_shape, activation_fxn, 
        grad_method="Standard", 
        train_factor=1.0, momentum=0.9, smoothing=(10**(-8)), 
        delta_factor=0.9, slope_param=1.0, use_bias=True):

        self.tFactor = train_factor
        
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

        if grad_method == "Standard":
            self.gradient_method = standard
        if grad_method == "Momentum":
            self.gradient_method = momentum
            self.momentum = momentum
        if grad_method == "Nesterov":
            self.gradient_method = Nesterov_acc
            self.momentum = momentum
        if grad_method == "Adagrad":
            self.gradient_method = adagrad
            self.smoothing = smoothing
        if grad_method == "Adadelta":
            self.gradient_method = adadelta
            self.delta_factor = delta_factor
        if grad_method == "RMSprop":
            self.gradient_method = RMSprop
            self.delta_factor = delta_factor
        if grad_method == "Adam":
            self.gradient_method = adam
            self.momentum = momentum
        if grad_method == "gradientNoise":
            self.gradient_method = gradient_noise
            self.momentum = momentum


        self.weights = np.random.uniform(-1, 1, weights_shape)
        self.use_bias = use_bias
        self.bias = 0.0
        if self.use_bias:
            self.bias = np.random.uniform(-1, 1, bias_shape)
        self.slope_param = slope_param
        self.error = np.zeros(self.weights.shape[0], 1))

    def activate(self, input_vector):

        raise NotImplementedError("activate not implemented")

    def connect_next_layer(self, next_layer):

        self.next_layer = next_layer

    def connect_prev_layer(self, prev_layer):

        self.prev_layer = prev_layer

    def grad_correction(self, cost, input_vals):

        raise NotImplementedError("correction not implemented")

    def adjust(self, weights_adjust, bias_adjust):

        self.weights -= weights_adjust
        if self.use_bias:
            self.bias -= bias_adjust



class FFLayer(Layer):

    


    def __init__(
        self, weights_shape, bias_shape, activation_fxn, 
        grad_method="Standard", 
        train_factor=1.0, momentum=0.9, smoothing=(10**(-8)), 
        delta_factor=0.9, slope_param=1.0, use_bias=True):

    super(FFLayer, self).__init__(weights_shape, bias_shape, activation_fxn,
        grad_method, train_factor, momentum, smoothing, 
        delta_factor, slope_param, use_bias):

    
    self.weights_error = np.zeros((self.weights.shape))

    def adjust(self, batch_size):

        adj_train_factor = float(self.tFactor) / batch_size
        temp_w_err = self.grad_method(
            self.weights_error, adj_train_factor,
            self.pVelocity, self.momentum, self.smoothing)

        self.pVelocity = temp_w_err

        temp_bias_err = np.multiply(adj_train_factor, self.error)

        self.weights_error = np.zeros((self.weights.shape))
        self.error = np.zeros(self.weights.shape[0], 1))

        self.weights -= temp_w_err
        if use_bias:
            self.bias -= temp_bias_err

        return True
    
        

class FFInputLayer(FFLayer):




    def __init__(
        self, weights, bias, 
        activation_fxn="Linear", grad_method="Standard", 
        train_factor=1.0, momentum=0.9, smoothing=(10**(-8)), 
        delta_factor=0.9, slope_param=1.0, use_bias=True):

        super(FFInputLayer, self).__init__(
            weights, bias, activation_fxn, grad_method, 
            train_factor, momentum, smoothing, 
            delta_factor, slope_param, use_bias):

    def activate(self, input_vector):

        self.input_vector = input_vector
        self.activation_input = (np.multiply(input_vector, self.weights)
            + self.bias)
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

    def grad_correction(self, error):

        temp_err = np.multiply(
            np.dot(self.next_layer.weights.T, error), 
            self.d_activation_fxn(self.activation_input, self.slope_param))
        self.weights_error += np.multiply(self.error, self.input_vector)
        self.error += temp_err
        return temp_err




class FFHiddenLayer(FFLayer):




    def __init__(
        self, weights, bias, 
        activation_fxn="Sigmoid", grad_method="Standard", 
        train_factor=1.0, momentum=0.9, smoothing=(10**(-8)), 
        delta_factor=0.9, slope_param=1.0, use_bias=True):

        super(FFHiddenLayer, self).__init__(
            weights, bias, activation_fxn, grad_method, 
            train_factor, momentum, smoothing, 
            delta_factor, slope_param, use_bias):

    def activate(self, input_vector):

        self.input_vector = input_vector
        self.activation_input = np.dot(self.weights, input_vector) + self.bias
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

    def grad_correction(self, error):

        temp_err = np.multiply(
            np.dot(self.next_layer.weights.T, error), 
            self.d_activation_fxn(self.activation_input, self.slope_param))

        self.weights_error += np.multiply(self.error, self.input_vector)
        self.error += temp_err
        return temp_err
        

class FFOutputLayer(FFLayer):

    def __init__(
        self, weights, bias, 
        activation_fxn="Linear", grad_method="Standard",
        cost_fxn="Quadratic"
        train_factor=1.0, momentum=0.9, smoothing=(10**(-8)), 
        delta_factor=0.9, slope_param=1.0, use_bias=True):

        super(FFOutputLayer, self).__init__(
            weights, bias, activation_fxn, grad_method, 
            train_factor, momentum, smoothing, 
            delta_factor, slope_param, use_bias):

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

    def activate(self, input_vector):

        self.input_vector = input_vector
        self.activation_input = np.dot(self.weights, input_vector) + self.bias
        self.output = self.activation_fxn(
            self.activation_input, self.slope_param)
        return self.output

    def grad_correction(self, target):

        temp_err = np.multiply(
            self.cost_fxn_grad(self.output, target), 
            self.d_activation_fxn(self.activation_input, self.slope_param))
        self.weights_error += np.multiply(self.error, self.input_vector.T)
        self.error += temp_err
        self.total_error = self.cost_fxn(self.output, target)
        return temp_err, self.total_error




class RInputLayer(FFInputLayer):

    def __init__(
        self, weights, bias,
        activation_fxn="Linear", slope_param=1.0, 
        use_bias=True, backprop_trunc=float("inf")):

        super(RInputLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

        self.internal_weights = np.random.uniform(
             -1, 1, (self.weights.shape[0], 1))
        self.output = [np.array([0.0])]
        self.input_vector = []
        self.activation_input = []
        self.backprop_trunc = backprop_trunc
        

    def activate(self, input_vector):
        self.input_vector.append(input_vector)
        self.activation_input.append(np.multiply(self.weights, input_vector) 
            + np.multiply(self.internal_weights, self.output[-1]) + self.bias)
        self.output.append(self.activation_fxn(
            self.activation_input[-1], self.slope_param))
        return self.output[-1]

    def refresh_memory(self):
        self.output = [np.array([0.0])]
        self.input_vector = []
        self.activation_input = []

    def correction(self, error):

        #BPPTT
        #Guided by: peterroelants.github.io/posts/rnn_implementation_part01/
        self.weights_error = 0.0
        self.internal_weights_error = 0.0
        self.error = np.multiply(
            np.dot(self.next_layer.weights.T, error),
            self.d_activation_fxn(self.activation_input[-1], self.slope_param))
        temp_error = self.error
        for k in range(len(self.input_vector), 0, -1):
            self.weights_error += np.multiply(temp_error, self.input_vector[k-1])
            self.internal_weights_error += np.multiply(
                temp_error, self.output[k-1])
            temp_error = np.multiply(temp_error, self.internal_weights)

        return (self.weights_error, self.internal_weights_error, 
                self.error, None)

    def adjust(self, adjust_weights, adjust_internal_weights, adjust_bias):
        self.weights = np.subtract(self.weights, adjust_weights)
        self.internal_weights = np.subtract(
            self.internal_weights, adjust_internal_weights)
        self.bias = np.subtract(self.bias, adjust_bias)
        return True


    
class RHiddenLayer(FFHiddenLayer):

    def __init__(
        self, weights, bias,
        activation_fxn="Sigmoid", slope_param=1.0, 
        use_bias=True, backprop_trunc=float("inf")):

        super(RHiddenLayer, self).__init__(
            weights, bias, activation_fxn, slope_param, use_bias)

        self.internal_weights = np.random.uniform(
             -1, 1, (self.weights.shape[0], 1))
        self.output = [np.array([0.0])]
        self.input_vector = []
        self.activation_input = []
        self.backprop_trunc = backprop_trunc
        

    def activate(self, input_vector):
        self.input_vector.append(input_vector)
        self.activation_input.append(np.dot(self.weights, input_vector) 
            + np.multiply(self.internal_weights, self.output[-1]) + self.bias)
        self.output.append(self.activation_fxn(
            self.activation_input[-1], self.slope_param))
        return self.output[-1]

    def refresh_memory(self):
        self.output = [np.array([0.0])]
        self.input_vector = []
        self.activation_input = []

    def correction(self, error):

        #BPPTT
        #Guided by: peterroelants.github.io/posts/rnn_implementation_part01/
        self.weights_error = 0.0
        self.internal_weights_error = 0.0
        self.error = np.multiply(
            np.dot(self.next_layer.weights.T, error),
            self.d_activation_fxn(self.activation_input[-1], self.slope_param))
        temp_error = self.error
        for k in range(len(self.input_vector), 0, -1):
            self.weights_error += np.multiply(temp_error, self.input_vector[k-1])
            self.internal_weights_error += np.multiply(
                temp_error, self.output[k-1])
            temp_error = np.multiply(temp_error, self.internal_weights)

        return (self.weights_error, self.internal_weights_error, 
                self.error, None)

    def adjust(self, adjust_weights, adjust_internal_weights, adjust_bias):
        self.weights = np.subtract(self.weights, adjust_weights)
        self.internal_weights = np.subtract(
            self.internal_weights, adjust_internal_weights)
        self.bias = np.subtract(self.bias, adjust_bias)
        return True

class ROutputLayer(FFOutputLayer):

    def __init__(
        self, weights, bias,
        activation_fxn="Linear", cost_fxn="Quadratic",
        slope_param=1.0, use_bias=True, backprop_trunc=float("inf")):

        super(ROutputLayer, self).__init__(
            weights, bias, activation_fxn, cost_fxn, slope_param, use_bias)

        self.internal_weights = np.random.uniform(
             -1, 1, (self.weights.shape[0], 1))
        self.output = [np.array([0.0])]
        self.input_vector = []
        self.activation_input = []
        self.backprop_trunc = backprop_trunc
        

    def activate(self, input_vector):
        self.input_vector.append(input_vector)
        self.activation_input.append(np.dot(self.weights, input_vector) 
            + np.multiply(self.internal_weights, self.output[-1]) + self.bias)
        self.output.append(self.activation_fxn(
            self.activation_input[-1], self.slope_param))
        return self.output[-1]

    def refresh_memory(self):
        self.output = [np.array([0.0])]
        self.input_vector = []
        self.activation_input = []

    def correction(self, target):

        self.weights_error = 0.0
        self.internal_weights_error = 0.0
        self.error = np.multiply(
            self.cost_fxn_grad(self.output[-1], target), 
            self.d_activation_fxn(self.activation_input[-1], self.slope_param))
        temp_error = self.error
        #Could be incorrect. Should check
        for k in range(len(self.input_vector), 0, -1):
            self.weights_error += np.multiply(temp_error, self.input_vector[k-1].T)
            self.internal_weights_error += np.multiply(
                temp_error, self.output[k-1].T)
            temp_error = np.multiply(temp_error, self.internal_weights)
        self.total_error = self.cost_fxn(self.output[-1], target)
        return (self.weights_error, self.internal_weights_error, 
            self.error, self.total_error)

    def adjust(self, adjust_weights, adjust_internal_weights, adjust_bias):
        self.weights = np.subtract(self.weights, adjust_weights)
        self.internal_weights = np.subtract(
            self.internal_weights, adjust_internal_weights)
        self.bias = np.subtract(self.bias, adjust_bias)
        return True

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

