"""This is a neuron: the base component of a neural network. It is meant
to function similar to a biological neuron, accepting inputs and based
on how large the input signal is fire an output signal. The neuron has
3 main components:
1. Weights for incoming stimuli (outputs from connected neurons): These 
	weights are what the neuron uses to set its "fire" threshold. They 
	are adjustable and allow the neuron, in concert with the network, to 
	adapt. 
	
2. Activation function: This is the function that incoming stimulus
	(the sum of all inputs multiplied by weights) are evaluated by. The
	activation funcition converts the incoming stimulus into a standard
	form, for a step funciton 0 or 1, and for a sigmoid function a value
	between 0 and 1 along a sigmoid curve.
	
3. Bias: This allows the neuron to fire even if no stimulus is recieved
	(if all values are 0) this acts essentially like an internal 
	stimulus to the neuron, allowing it to fire on a 0 input, which may
	be useful to the network as a whole. The bias is adjusted like a 
	weight.
	
These things together make up a neuron. They can be specified in a 
matrix or neuron objects. When connected in multiple layers, the neurons
may act like an equation where the weights are the coefficients. In this
way a neural network can approximate many types of equations by 
adjusting weights.

The main resource I used for this project may be found here:
	http://neuralnetworksanddeeplearning.com/chap1.html"""
#By Daniel Graham



import random
import math

	
class Neuron:
	#A class to specify neurons in a neural network. 
	def __init__(self, number_inputs):
		self.bias = 1
		self.output_value = 0 #Output from activation function
		self.input_stimulus = 0  #Sum of inputs multiplied by weights
		self.input_vector = []
		self.downstream_neurons = [] 
		self.activation_function = None 
		self.error = 0 
		self.learn_rate = 1
		self.set_activation_function_sigmoid()
		
		#MAY NEED UNWEIGHTED INPUTS AS WELL. MAKE SURE NOT NECESSARY.
		
		#Activation is initially set to sigmoid because this is the 
		#most common activation function in basic networks.
		
		
		#Create weight values. Between -1 and 1 initially. Weight index 
		#in array corresponds to index of input to weight.
		self.weights = []	
		for i in range(number_inputs):
			self.weights.append(random.uniform(-1, 1))
			
		#May instead have a bias that changes rather than weight.
		#Will do a few tests to determine best scenario.	
		#self.weights.append(random.uniform(-1, 1))
		
	def set_bias(self, new_bias):
		#This method may not be necessary if it can be done with weights
		self.bias = new_bias
		
	def set_error(self, new_error):
		#The error in a neuron is what motivates the adjustment of 
		#weights, each adjustment is meant to reduce neuron self.error. 
		self.error = new_error
	
	def set_activation_function_step(self):
		#Sets the activation function to a step function.
		#This is not really a useful activation function because it 
		#causes drastic swings in the network when a weight changes. 
		#Drastic swings are caused by the binary values of a step fxn.
		
		self.activation_function = step_function
		self.d_activation_function = 0 
		
	def set_activation_function_sigmoid(self, sig_slope_param = 1):
		#Sets activation function as a sigmoid. Can adjust the 
		#parameters of the sigmoid if necessary. This is a useful 
		#activation function because there is a 'soft' change from 0
		#to 1 when compared to the step function, resulting in much more
		#gradual output changes.
		
		self.sig_slope_param = sig_slope_param
		self.activation_function = self.log_sigmoid
		self.d_activation_function = self.d_log_sigmoid
	
	def set_sig_slope_param(self, new_param):
		#The slope parameter determines how 'soft' or gradual the change
		#from 0 to 1 outputs are in the function. A smaller parameter
		#means a smaller slope.
		
		self.sig_slope_param = new_param
			
	def process_input(self, input_array):
		#Processes the input and determines if it will fire. 
		#Returns the value of the activation_function
		#Also stores the value of the output temporarily for use 
		# in self.output.
		
		#Each input is multiplied by its corresponding weight and then
		#all inputs are summed and stored in the neuron memory 
		#(self.input_sum).
		
		weighted_inputs = []
		for i in range(input_array):
			weighted_inputs.append(input_array[i] * self.weights[i])
		
		self.input_stimulus = sum(weighted_inputs) + self.bias
			
		#Then the input stimulus is sent to the activation fxn which 
		#generates the output of the neuron, also stored in the neuron
		#memory (self.output_value).
		
		activation_val = self.activation_function(self.input_stimulus)
		self.output_value = activation_value
		return activation_val
		
	def adjust_weights(self):
		#Adjusts the weights of the inputs
		for i in range(self.weights):
			new_weight = self.weights[i] - (self.learn_rate * \
				(self.input_vector[i] * self.error))
			self.weights[i] = new_weight
			
	def adjust_bias(self):
		#Adjusts the bias of the neuron
		new_bias = self.bias - (self.learn_rate * self.error)
		self.bias = new_bias
		
	def connect_neuron(self, neuron_to_connect):
		#Connects the current neuron to the next layer. The neurons in 
		#self.downstream_neurons receive the output of the self neuron.
		
		self.downstream_neurons.append(neuron_to_connect)
	
	def log_sigmoid(input_stimulus):
		#Returns a value from 0 to 1 and has a variable slope.
		
		sig_val = 	1.0/(1.0 + (math.e ** (-1 * self.sig_slope_param * \
											input_stimulus)))
		return sig_val
		
	def d_log_sigmoid(input_stimulus):
		#Returns the derivative of the log_sigmoid activation function.
		#The derivative is used when determing the error in a neuron.
		
		sig_derivative = (math.e ** input_stimulus) \
							/ ((1 + math.e ** input_stimulus) ** 2)
		
		return sig_derivative
		
	def tan_hyperbolic(input_stimulus):
		#Returns a value from -1 to 1. Similar to log_sigmoid but 
		#offers negative values.
		hyp_value = math.tanh(input_stimulus)
		return hyp_value
		
	def soft_max(input_stimulus):
		#SoftMaxFunction is slightly different from the others.
		#It requires an output neuron for each possible output value
		#(outputs are not binary, 1 or 0, they take on multiple values)
		#The function divides the sum of the inputs and weights at 
		#each neuron and divides by the sum of all neurons. Thus the
		#probability of the neuron's output being correct is given. The
		#output neurons are numbered to correspond to the poss. outputs.
		#Soft max must have access to all other neurons in the layer.
		pass
		
		
	def step_function(input_stimulus):
		#Returns either -1 or 1 no values between. Not very useful for
		#neurons.
		if (input_stimulus >= 0):
			return 1
		else:
			return 0
			
