#A module to house the various functions used by the NN
#By DanG

import numpy as np
import math

##--------------------------Activation Functions-------------------------------

def heaviside(input_stimulus, slope_param=1.0):

    return np.piecewise(input_stimulus, 
        [input_stimulus < 0, input_stimulus == 0, input_stimulus > 0],
        [0., 0.5, 1.])

def d_heaviside(input_stimulus, slope_param=1.0):

    return 0.0

def signum(input_stimulus, slope_param=1.0):

    return np.piecewise(input_stimulus, 
        [input_stimulus < 0, input_stimulus == 0, input_stimulus > 0],
        [-1., 0., 1.])

def d_signum(input_stimulus, slope_param=1.0):

    return 0.0

def piece_wise_linear(input_stimulus, slope_param):

    return np.piecewise(input_stimulus, 
        [input_stimulus <= -.5, input_stimulus > -.5, 
         input_stimulus < 0.5,  input_stimulus >= 0.5],
        [0, slope_param * nput_stimulus + 0.5, 
         slope_param * input_stimulus + 05, 1.])

def d_piece_wise_linear(input_stimulus, slope_param=1.0):

    return np.piecewise(input_stimulus, 
        [input_stimulus <= -.5, input_stimulus > -.5, 
         input_stimulus < 0.5,  input_stimulus >= 0.5],
        [0, slope_param, slope_param, 0])

def linear(input_stimulus, slope_param=1.0):

    return np.multiply(slope_param, input_stimulus)

def d_linear(input_stimulus, slope_param=1.0):

    out_array = np.copy(input_stimulus)
    out_array.fill(slope_param)
    return out_array

def log_sigmoid(input_stimulus, slope_param=1.0):

    #Returns a value from 0 to 1 and has a variable slope.
    sig_val = np.divide(1.0, (1.0 + (np.exp(
                  np.multiply(-1., 
                  np.multiply(slope_param, input_stimulus))))))
    return sig_val
		
def d_log_sigmoid(input_stimulus, slope_param=1.0):

    #Returns the derivative of the log_sigmoid activation function.
    #The derivative is used when determing the error in a neuron.
    sig_derivative = np.divide(slope_param, 
                         np.multiply(2.0, np.cosh(input_stimulus)) + 2)
    return sig_derivative
	
def tanh(input_stimulus, slope_param=1.0):

    # Returns a value from -1 to 1. Similar to log_sigmoid but 
    # offers negative values.
    hyp_value = np.tanh(np.multiply(slope_param, input_stimulus))
    return hyp_value
		
def d_tanh(input_stimulus, slope_param=1.0):

    # Returns the derivative of the tan_hyperbolic fxn.
    d_hyp_value = slope_param * np.square((np.sech(input_stimulus)))
    return d_hype_value

#Incorporate slope_param
def arc_tan(input_stimulus, slope_param=1.0):

    return np.arctan(input_stimulus)

def d_arc_tan(input_stimulus, slope_param=1.0):

    return np.divide(1., (np.square(input_stimulus) + 1))

def softsign(input_stimulus, slope_param=1.0):

    input_stimulus = np.multiply(input_stimulus, slope_param)
    return np.divide(input_stimulus, (1 + np.absolute(input_stimulus)))

def d_softsign(input_stimulus, slope_param=1.0):

    input_stimulus = np.multiply(input_stimulus, slope_param)
    return np.divide(slope_param, np.square(input_stimulus + 1))

def softplus(input_stimulus, slope_param=1.0):

    input_stimulus = np.multiply(input_stimulus, slope_param)
    return np.log(1 + np.exp(input_stimulus))

def d_softplus(input_stimulus, slope_param=1.0):

    input_stimulus = np.multiply(input_stimulus, slope_param)
    top = np.multiply(slope_param, np.exp(input_stimulus))
    bottom = np.exp(input_stimulus) + 1
    return np.divide(top, bottom)

def softmax(input_stimulus, slope_param=1.0):

    input_stimulus = np.multiply(input_stimulus, slope_param)
    e_x = np.exp(input_stimulus)
    return np.divide(e_x, np.sum(e_x, axis=0))

def d_softmax(input_stimulus, slope_param=1.0):

    value = softmax(input_stimulus, slope_param)
    SM = value.reshape((-1,1))
    return np.diag(value) - np.dot(SM, SM.T)

##----------------------------Cost Function Gradients--------------------------

#Many found here: http://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications

def quad_cost(output_vector, target_vector):

    return np.multiply(0.5, np.sum(np.square((output_vector - target_vector))))

def quad_cost_grad(output_vector, target_vector):

    return (output_vector - target_vector)

def cross_entropy_cost(output_vector, target_vector):

    return -(np.sum(
        (np.multiply(target_vector, np.log(output_vector)) 
        + np.multiply((1 - target_vector), np.log(1 - output_vector)))))

def cross_entropy_cost_grad(output_vector, target_vector):

    return np.divide((output_vector - target_vector), 
                     ((1. - output_vector) * output_vector))

#The exponential cost fxns not done.
def exponential_cost(output_vector, target_vector, t_param=1.0):

    pass


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

def Kullback_Leibler_divergence(output_vector, target_vector):

    return np.multiply(target_vector, 
        np.log(np.divide(target_vector, output_vector)))

def Kullback_Leibler_divergence_grad(output_vector, target_vector):

    return -1 * np.divide(target_vector, output_vector)

def gen_Kullback_Leibler_divergence(output_vector, target_vector):
    pass

def gen_Kullback_Leibler_divergence_grad(output_vector, target_vector):

    return -1 * (np.divide((target_vector + output_vector), output_vector))

def Itakura_Saito_distance_grad(output_vector, target_vector):

    return np.divide((output_vector - target_vector), (output_vector) ** 2.)

##-----------------------------------------------------------------------------
