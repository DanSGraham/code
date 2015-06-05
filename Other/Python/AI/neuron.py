import random

#TO solve the problem of output weighting have a special output neuron with only one input use to determine weight of final output if needed. May find that such a neuron is not needed.

class Neuron:
	#A class to specify neurons in a neural network. 
	def __init__(self, numberOfInputs):
		#NEED Weights of all inputs. Will the output or input node store weights? (thinking output)
		#Need activation function (sigmoid function or step)
		#NEed Bias!
		self.bias = 1
		self.downStreamNeurons = []
		
		#create weight values. Between -1 and 1 initially. Weights match
		#indeces of inputs.
		self.weights = []	
		for i in range(numberOfInputs):
			self.weights.append(random.uniform(-1, 1))
			
		
		#add weight for bias. Always at the end of the array.	
		self.weights.append(random.uniform(-1, 1))
	
	def processInput(self, inputArray):
		#Processes the input and determines if it will fire.
		
	def adjustWeights(self, weightAdjust):
		#Adjusts the weights of the inputs
		
	def connectNeuron(self, neuronToConnect):
		self.downStreamNeurons.append(neuronToConnect)
		
	
