import random
import math

#TO solve the problem of output weighting have a special output neuron with only one input use to determine weight of final output if needed. May find that such a neuron is not needed.


	
class Neuron:
	#A class to specify neurons in a neural network. 
	def __init__(self, number_inputs):
		self.bias = 1
		self.output_value = 0
		self.input_sum = 0
		self.downstream_neurons = []
		self.activation_function = None
		self.error = 0
		self.set_activation_function_sigmoid()
		
		#create weight values. Between -1 and 1 initially. Weights match
		#indeces of inputs.
		self.weights = []	
		for i in range(number_inputs):
			self.weights.append(random.uniform(-1, 1))
			
		
		#add weight for bias. Always at the end of the array. 
		#May instead have a bias that changes rather than weight.
		#Will do a few tests to determine best scenario.	
		#self.weights.append(random.uniform(-1, 1))
		
	def set_bias(self, new_bias):
		#This method may not be necessary if it can be done with weights
		self.bias = new_bias
		
	def set_error(self, new_error):
		self.error = new_error
	
	def set_activation_function_step(self):
		#Sets the activation function to a step function
		pass
		
	def set_activation_function_sigmoid(self, sig_slope_param = 1):
		#Sets activation function as a sigmoid. Possibly adjust the parameters of the sigmoid if necessary
		self.sig_slope_param = sig_slope_param
		self.activation_function = self.log_sigmoid
		self.d_activation_function = self.d_log_sigmoid
	
	def set_sig_slope_param(self, new_param):
		self.sig_slope_param = new_param
			
	def process_input(self, input_array):
		#Processes the input and determines if it will fire. 
		#Returns the value of the activation_function
		#Also stores the value of the output temporarily for use 
		# in self.output.
		sum_inputs = sum(input_array)
		self.input_sum = sum_inputs
		activation_val = self.activation_function(sum_inputs)
		self.output_value = activation_value
		return activation_val
		
	def adjust_weights(self, weight_adjust):
		#Adjusts the weights of the inputs
		pass
		
	def connect_neuron(self, neuron_to_connect):
		self.downstream_neurons.append(neuron_to_connect)
	
	def log_sigmoid(sum_inputs):
		#returns a value from 0 to 1
		sig_val = 	1.0/(1.0 + (math.e ** (-1 * self.sig_slope_param * sum_inputs)))
		return sig_val
		
	def d_log_sigmoid(sum_inputs):
		#Returns the derivative of the log_sigmoid activation function.
		
		sig_derivative = (math.e ** sum_inputs) \
		/ ((1 + math.e ** sum_inputs) ** 2)
		
		return sig_derivative
		
	def tan_hyperbolic(sum_inputs):
		#returns a value from -1 to 1
		hyp_value = math.tanh(sum_inputs)
		return hyp_value
		
	def soft_max(sumOfInputs):
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
		#Soft max must have access to all other neurons in the layer.
		pass
		
		
	def step_function(sum_inputs):
		#returns either -1 or 1
		if (sum_inputs >= 0):
			return 1
		else:
			return 0
			
