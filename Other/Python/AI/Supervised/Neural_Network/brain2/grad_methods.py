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

def Nesterov_acc(we):
    #This one requires the gradient method. Needs another parameter. Maybe fix somehow?
    pass

def adagrad(weight_error, train_factor, prev_velocity, momentum_factor, smoothing_factor, lookback_limit):
    #Smoothig factor on the order of 10^-8
    pass

def adadelta(weight_error, train_factor, prev_velocity, momentum_factor, smoothing_factor, lookback_limit):
    pass

def RMSprop():
    pass

def adam():
    pass
