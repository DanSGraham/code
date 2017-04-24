#A program to calculate the Monte Carlo Integration
#By DanG 
import random
import math
import numpy
import matplotlib.pyplot as plt

samples = 10000

#Calculate the Integral
def fxn(x):
    return (1./(1. + x**2.))


def fxn_2(x):
    return (1./(1. + x**2.)) ** 2.

def transform_x(a, val):
    return -(math.log(1 - (1 - math.exp(-a)) * val))/a

def new_px(a, val):
    return (a * math.exp(-a * val)) / (1 - math.exp(-a))

def MCI_Uniform(numSamples):
    input_list = []
    fxList = []
    fx_2List = []
    for i in range(numSamples):
        randVal = random.random()
        input_list.append(randVal)
        fxList.append(fxn(randVal))
        fx_2List.append(fxn_2(randVal))

    return (input_list, fxList, fx_2List)
    #plt.scatter(range(len(fxList)), fxList, s=10)    
    #plt.ylabel("Integral Value")
    #plt.xlabel("x index")
    #plt.title("Integral of Fxn")
    #plt.show()


aVal = 0.7

def MCI_Improved(numSamples):
    input_list = []
    fxList = []
    fx_2List = []
    for i in range(numSamples):
        randNum = (1- math.exp(-aVal * random.random()))/ ( 1- math.exp(-aVal))
        randVal = transform_x(aVal, randNum)
        otherVal = new_px(aVal, randVal)
        input_list.append(otherVal)
        fxList.append(((fxn(randVal))/otherVal))
        fx_2List.append(((fxn_2(randVal))/otherVal))

    return (input_list, fxList, fx_2List)

    #plt.scatter(range(len(fxList)), fxList, s=10)    
    #plt.ylabel("Integral Value")
    #plt.xlabel("x index")
    #plt.title("Integral of Fxn")
    #plt.show()

def main():

    uni_input, uni_fx, uni_fx2 = MCI_Uniform(samples)
    imp_input, imp_fx, imp_fx2 = MCI_Improved(samples)

   # print numpy.mean(imp_fx)
   # print numpy.mean(imp_fx2)
   # print numpy.mean(imp_fx2) - numpy.mean(imp_fx) ** 2.

    plt.scatter(range(len(uni_fx)), [x * 4 for x in uni_fx], s=10)
    plt.scatter(range(len(imp_fx)), [x * 4 for x in imp_fx], s=10)
    plt.show()

main()

