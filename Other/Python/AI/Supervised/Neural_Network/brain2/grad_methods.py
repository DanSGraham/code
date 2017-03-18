#A module to contain gradient methods
#By DanG

import numpy as np

##--------------------------Gradient Descent Improvements----------------------
#Found here: http://sebastianruder.com/optimizing-gradient-descent/ 
def standard(weight_error, train_factor, prev_velocity=1, momentum_factor=1, smoothing_factor=1):
    return np.multiply(train_factor, weight_error)

def momentum(weight_error, train_factor, prev_velocity, momentum_factor, smoothing_factor=1):

        return (np.multiply(momentum_factor, prev_velocity)
            + np.multiply(train_factor, weight_error))

def Rprop():
    pass

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
    pass
