#A module to house the various functions used by the NN
#By DanG

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

##-----------------------------------------------------------------------------

def distance2(vector1, vector2):
    """Return the square distance between two vectors"""
    return np.sum(np.square(np.subtract(vector2, vector1)))
