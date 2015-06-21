import random
import math

#TO solve the problem of output weighting have a special output neuron with only one input use to determine weight of final output if needed. May find that such a neuron is not needed.


	
class Neuron:
	#A class to specify neurons in a neural network. 
	def __init__(self, numberOfInputs):
		#NEED Weights of all inputs. Will the output or input node store weights? (thinking output)
		#Need activation function (sigmoid function or step)
		#NEed Bias!
		self.bias = 1
		self.downStreamNeurons = []
		self.sigSlopeParam = 1
		self.activationFunction = self.LogSigmoid
		
		#create weight values. Between -1 and 1 initially. Weights match
		#indeces of inputs.
		self.weights = []	
		for i in range(numberOfInputs):
			self.weights.append(random.uniform(-1, 1))
			
		
		#add weight for bias. Always at the end of the array.	
		self.weights.append(random.uniform(-1, 1))
		
		#Possibly don't need weight for bias. Some examples have direct 
		#Change of bias.
	
	def setActivateFunctionStep(self):
		#Sets the activation function to a step function
		pass
		
	def setActivationFunctionSigmoid(self):
		#Sets activation function as a sigmoid. Possibly adjust the parameters of the sigmoid if necessary
		self.sigSlopeParam = 1
	
	def setSigSlopeParam(self, newParam):
		self.sigSlopeParam = newParam
			
	def processInput(self, inputArray):
		#Processes the input and determines if it will fire.
		pass
		
	def adjustWeights(self, weightAdjust):
		#Adjusts the weights of the inputs
		pass
		
	def connectNeuron(self, neuronToConnect):
		self.downStreamNeurons.append(neuronToConnect)
	
	def LogSigmoid(sumOfInputs):
		#returns a value from 0 to 1
		sigValue = 	1.0/(1.0 + (math.e ** (-1 * self.sigSlopeParam * sumOfInputs)))
		return sigValue
		
	def TanHyperbolic(sumOfInputs):
		#returns a value from -1 to 1
		hypValue = math.tanh(sumOfInputs)
		return hypValue
		
	def SoftMaxFunction(sumOfInputs):
		#Need to look up the softMaxFunction
		#Starting to get it. Involves a probability of outputs. 
		#Need more research. Lack fundamental understanding.
		
		
		#SoftMaxFunction is slightly different from the others.
		#It requires an output neuron for each possible output value
		#(outputs are not binary, 1 or 0, they take on multiple values)
		#The function divides the sum of the inputs and weights at 
		#each neuron and divides by the sum of all neurons. Thus the
		#probability of the neuron's output being correct is given. The
		#output neurons are numbered to correspond to the poss. outputs.
		pass
		
		
	def StepFunction(sumOfInputs):
		#returns either -1 or 1
		if (sumOfInputs >= 0):
			return 1
		else:
			return 0
	
		
	
