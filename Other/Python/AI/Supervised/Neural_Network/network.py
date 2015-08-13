"""This is a neural network: the organizational structure on which 
neurons are arrayed. The network not only stores the order of the 
neurons, but it is also responsible for calculating the cost and errors
associated with the whole network, and report those errors back to 
individual neurons for weight adjustments. The neurons can be organized
in any fashion in a network, but the most fundamental kind of network is
a feed forward network. This kind of network has 3 basic 'layers' of
neurons (In one layer of neurons the neurons of that layer are not 
connected to each other in anyway, but all connect to the neurons in the
adjacent forward layer):

1. Input layer: The input layer is where the inputs for the neural 
	network are received. This layer takes raw data from your data set 
	and sends it to the next layer.
	
2. Hidden layer: The hidden layer (or layers) are those that are not 
	input layers, but are not output layers either (output layers will
	be explained shortly). Hidden layers allow further processing and
	adjustments to be made to the data before it is sent to the output 
	layer. The more complex the hidden layers, the more complex of an
	equation the system can model.
	
3. Output layer: This is the layer that returns a value. Each neuron in
	this layer corresponds to a binary type value. If you want to
	predict true or false (binary possibility) given any inputs, you
	can use 1 output neuron, because the neuron can output 2 possible 
	values effectively. If you want to predict a number between 1 and 10
	you would need 10 output neurons and assign each a number in the 
	desired range. Then you can determine which is the output by the 
	largest output value.

Neurons in a network have the capacity to model incredibly complex 
equations, and usually the more neurons in hidden layers, the more 
complex the model can become. The trade off, as usual, is time and 
occasional overfitting. The network allows neurons to communicate with
each other and send errors through the network, allowing the whole 
network to improve over time.

The main resource I used for this project may be found here:
	http://neuralnetworksanddeeplearning.com/chap1.html"""
#By Daniel Graham

#TODO: 
#		1. Add matrix functionality to speed up considerably. 
#         1a. Write error reporting and add save/load feature.
#		  1b. Does the test set remain isolated from train set for stochastic? Also add exception raise if number of expected inputs incorrect.
#		2. Add recurrent feature.
#		4. Add fuzzy logic
#		5. Other kinds of NN

from neuron import *
import math
import random
import time
import datetime
import numpy as np


class Network:
	# A class to specify a network of neurons
	def __init__(self, num_input_vals, num_poss_out, num_neurons_array,\
					act_fxn = "sig", cost_fxn = "quad"):
		"""Inputs:
			num_input_vals: The number values the network will accept
			num_poss_out: The number of possible output values
			num_neurons_array: an array where each layer of the network
								has the number of neurons specified.
								for example: [3, 4, 4, 2]. This network
								has 3 input neurons, two hidden layers
								with 4 neurons each, and 2 output layer
								neurons. This network should also have 
								the same value for num_poss_out as for
								the number of neurons in the output 
								layer.
		    act_fxn: The activation function of individual neurons
		    cost_fxn: The selected cost function."""
								
		
		
		# Activation is initially set to sigmoid because it is the 
		# most common activation function in basic networks.	
		self.activation_function = None
		if act_fxn == "sig": 
			self.set_activation_function_sigmoid()
		elif act_fxn == "tan":
			self.set_activation_function_tan_hyperbolic()
		else:
			raise NameError("""Your activation function parameter is 
								missing or wrong""")
		
		
		# Set cost function.
		if cost_fxn == "quad":
			self.set_quadratic_cost_function()
		
		# weights_array stores the entire network weights as np.arrays.
		self.weights_array = []
		
		# bias_array stores the entire network bias
		self.bias_array = []
		
		# inputs_array stores the input values for each layer of the 
		# network and is pop. in evaluate_network.
		self.inputs_array = []

		# weight_cost stores the derivative of the cost with respect
		# to weight for the network. Populated in add_cost.
		self.weight_cost = []
		
		# bias_cost stores the derivative of the cost with respect to 
		# bias for the network. Pop in add_cost.
		self.bias_cost = []		
		
		# learn_rate is a user adjustable parameter. It should be tuned
		# for a specific dataset to optimize learning.
		self.learn_rate = 1.0
		
		# weights_array is built. Each layer starts as a random number
		# between -1 and 1 with the 0 axis corresponding to individual
		# neurons, and the 1 axis the weights associated with each 
		# neuron. Each neuron has a number of weights equal to the 
		# number of neurons in an upstream layer.
		for i in range(len(num_neurons_array)):
			
			# The initial layer has weights determined by num_input_vals
			if i <= 0:
				temp_matrix = np.random.uniform(-1, 1, (num_neurons_array[i], num_input_vals))
				
			else:
				temp_matrix = np.random.uniform(-1, 1, (num_neurons_array[i], num_neurons_array[i - 1]))
			
			self.weights_array.append(temp_matrix)
			
			# bias_array initially set to 1 with the same dimensionality
			# as weights_array to align for evaluation. 			
			self.bias_array.append(np.ones((num_neurons_array[i], 1)))
			
		
	
	def set_quadratic_cost_function(self):
			self.cost_function = self.quadratic_cost_function
			self.d_cost_function = self.d_quadratic_cost_function
			
			#Used for saving the network
			self.cost_string = "Cost Function: Quadratic\n"
			
	
	def evaluate_network(self, input_vector_matrix):
		# Passes input_vector_matrix through the network and returns
		# output of last layer (outputs_array).
		
		# Converts the input to np.array and stores it as first value
		# in inputs_array.
		self.inputs_array = [np.asarray([input_vector_matrix]).T]
		
		# input_stimuli_array stores the stimulus to each neuron in a
		# layer (weights * input to neuron + bias)
		self.input_stimuli_array = [] 
		
		# Iterates through each layer in the network and evaluates the 
		# input to that layer. Then determines the output of that layer.
		for i in range(len(self.weights_array)):
			weighted_inputs_array = (self.weights_array[i] * self.inputs_array[i].T)
			weighted_array_sum = np.sum(weighted_inputs_array, axis=1, keepdims=True) \
								+ self.bias_array[i]
			self.input_stimuli_array.append(weighted_array_sum)
			neuron_output_array = self.activation_function(weighted_array_sum)
			
			# If the layer is not the output layer
			if i < (len(self.weights_array) - 1):
				self.inputs_array.append(neuron_output_array)
				
			# Else the output array is saved seperately.
			else:
				self.outputs_array = neuron_output_array
				
		return self.outputs_array
		
	def calculate_errors(self, exp_val_vector):
		# Calculates the error in each layer of the network using
		# backwards propigation.
		
		self.error_array = []
		
		exp_out_array = (np.asarray([exp_val_vector])).T
		
		# Iterates through the network calculating the error in layers
		# determined by the exp_val_vector (expected value vector). 
		# Error is then passed along the network until all neurons have 
		# an error value.
		for i in range((len(self.weights_array) - 1), -1, -1):
			
			# Output Layer
			if i >= (len(self.weights_array) - 1):
				error_in_layer = (self.d_cost_function(exp_out_array, self.outputs_array) \
					* self.d_activation_function(self.input_stimuli_array[-1]))
					
			else:
				error_in_layer = np.sum((self.weights_array[i + 1].T * self.error_array[0].T), axis=1, keepdims=True)
				error_in_layer *= self.d_activation_function(self.input_stimuli_array[i])
			
			# Because the backpropigation starts at the output layer, 
			# to maintain array consistency the most recently calculated
			# error_in_layer is added to the front of the error_array.
			self.error_array.insert(0, error_in_layer)
		
		return self.error_array

	def add_cost(self):
		
		# If no cost arrays exist they are created. (cost arrays cleared
		# after update_network)
		if len(self.weight_cost) <= 0:
			self.weight_cost = []
			self.bias_cost = []
			for i in range(len(self.weights_array)):
				self.weight_cost.append(self.inputs_array[i].T * self.error_array[i])
				self.bias_cost.append(self.error_array[i])
				
		else:
			for i in range(len(self.weights_array)):
				
				self.weight_cost[i] += (self.inputs_array[i].T * self.error_array[i])
				self.bias_cost[i] += self.error_array[i]
		

		return (self.weight_cost, self.bias_cost)
		
	def update_network(self, norm_factor):
		# Updates the weights and biases based on cost arrays.
		# norm_factor averages the cost.

		for i in range(len(self.weights_array)):
			self.weights_array[i] -= ((self.learn_rate / norm_factor) * self.weight_cost[i])
			self.bias_array[i] -= ((self.learn_rate / norm_factor) * self.bias_cost[i])
		
		# Cost arrays are reset here.
		self.weight_cost = []
		self.bias_cost = []

## ----------Training Methods ----------		
	
	def batch_train(self, input_matrix, output_matrix, batch_size, \
					verbose=False):
		
		# Prevents the j value from exceeding the input_matrix index.
		upper_limit = len(input_matrix) - len(input_matrix) % batch_size
		
		training_error = 0.0
		
		# Iterate through input_matrix and train network in batches.
		for i in range(0, upper_limit, batch_size):
			batch_error = 0.0
			for j in range(batch_size):
				self.evaluate_network(input_matrix[i + j])
				self.calculate_errors(output_matrix[i + j])
				self.add_cost()
				
				# Calculates the training error per batch
				corr_output = (np.asarray([output_matrix[i + j]])).T
				batch_error += (np.sum(np.abs(corr_output - \
								self.outputs_array) / corr_output) * 100.0)\
								 / np.shape(self.outputs_array)[0]
			
			# Averages the batch error					 
			batch_error = batch_error / batch_size
			if verbose == True:
				print batch_error, "% training error"
			
			training_error += batch_error		
			
			self.update_network(1)
		
		# Averages the training error.
		training_error = training_error / (upper_limit / batch_size)
		
		return training_error
		
	def online_train(self, input_vector, output_vector):
		# Utilizes batch_train with a batch_size of 1.
		
		return self.batch_train([input_vector], [output_vector], 1)
	
	
	def stochastic_train(self, input_matrix, output_matrix, train_size,\
							test_size, max_num_epochs, report_epochs, \
							max_error_value):
								
		#Error calculated incorrectly
								 
		# Trains using a stochastic method. Randomizes input to 
		# determine an approximation of the cost function on a smaller
		# data set. May speed up learning in some cases.							
		error_val = 100.0
		num_epochs = 0.0
		
		#Create the data set used for testing network ability
		random_index_list = [i for i in range(len(input_matrix))]
		random.shuffle(random_index_list)
		
		test_in = []
		test_out = []
		
		for i in range(test_size):
			test_in.append(input_matrix[random_index_list[i]])
			test_out.append(output_matrix[random_index_list[i]])
			
		input_matrix = [n for n in input_matrix if n not in test_in]
		output_matrix = [m for m in output_matrix if m not in test_out]
		
		
		while not (error_val < max_error_value or num_epochs >= max_num_epochs):
			
			#Trains the network.
			train_error = 0.0
			for i in range(report_epochs):
				train_error += self.stochastic_single_epoch_train(input_matrix, output_matrix, train_size)
				print train_error
				num_epochs += 1
			
			# Averages the training error over the training cycle. (maybe report after every epoch?)
			train_error = train_error / report_epochs
			
			# Network is tested and error determined. Testing is done
			# in a very similar way to training, only without using the
			# whole data set as the test set.
			
			cross_error = 0.0
			for j in range(test_size):
				net_out = self.evaluate_network(test_in[j])
				corr_out = (np.asarray([test_out[j]])).T
				temp_error = (np.sum(np.abs(corr_out - net_out) \
								/ corr_out) * 100.0) / np.shape(net_out)[0]
				
				cross_error += temp_error
			

			error_val = cross_error / test_size
			
			print "Number of Epochs: ", num_epochs
			print "Average Error of training set ", train_error, "%"
			print "Average Error of test set: ", error_val, "%"

			
	def stochastic_single_epoch_train(self, input_matrix, output_matrix, train_size):
		# Performs training through one epoch, or using the entire input
		# matrix once.
		
		#Error calculated incorrectly
		
		# First the input/output matrix pairs are placed up randomly
		# into mini-batch buckets.
		num_buckets = len(input_matrix) / train_size
		
		batch_buckets = [[] for a in range(num_buckets)]
		
		random_index_list = [i for i in range(len(input_matrix))]
		random.shuffle(random_index_list)
		random_index_value = 0
		
		while (random_index_value < len(random_index_list)):
			for j in range(len(batch_buckets)):
				if random_index_value >= len(random_index_list):
					break
				else:
					batch_buckets[j].append((input_matrix[random_index_value], \
											output_matrix[random_index_value]))
					random_index_value += 1
		
				
		# Then each bucket is trained on the network.
		training_error = 0.0
		for bucket in batch_buckets:
			bucket_error = 0.0
			for j in range(len(bucket)):
					self.evaluate_network(bucket[j][0])
					self.calculate_errors(bucket[j][1])
					self.add_cost()
					
					# Calculates and displays the training error per batch
					corr_output = (np.asarray([bucket[j][1]]).T)
					bucket_error += (np.sum(np.abs(corr_output - \
									self.outputs_array) / corr_output) * 100.0)\
									 / np.shape(self.outputs_array)[0]
					
			# Averages the batch error					 
			bucket_error = bucket_error / len(bucket)
			training_error += bucket_error	
			self.update_network(len(bucket))		
			
		# Averages the training error.
		training_error = training_error / len(batch_buckets)	
		return training_error
			
			
## ----------Activation Functions ----------				
	def log_sigmoid(self, input_stimulus):
		#Returns a value from 0 to 1 and has a variable slope.
		
		sig_val = 	1.0 / (1.0 + (np.e ** (-1 * input_stimulus)))
		return sig_val
		
	def d_log_sigmoid(self, input_stimulus):
		#Returns the derivative of the log_sigmoid activation function.
		#The derivative is used when determing the error in a neuron.
		
		sig_derivative = (np.e ** input_stimulus) \
							/ (np.square(1.0 + (np.e ** input_stimulus)))
			
		return sig_derivative
		
	def tan_hyperbolic(input_stimulus):
		# Returns a value from -1 to 1. Similar to log_sigmoid but 
		# offers negative values.
		
		hyp_value = np.tanh(input_stimulus)
		return hyp_value
		
	def d_tan_hyperbolic(input_stimulus):
		# Returns the derivative of the tan_hyperbolic fxn.
		
		d_hyp_value = (np.sech(input_stimulus)) ** 2
		return d_hype_value
	
	def set_activation_function_sigmoid(self, sig_slope_param = 1):
		#Sets activation function as a sigmoid. Can adjust the 
		#parameters of the sigmoid if necessary. This is a useful 
		#activation function because there is a 'soft' change from 0
		#to 1 when compared to the step function, resulting in much more
		#gradual output changes.
		
		self.sig_slope_param = sig_slope_param
		self.activation_function = self.log_sigmoid
		self.d_activation_function = self.d_log_sigmoid
		
		#Used for network saving
		self.activation_string = "Activation Function: Sigmoid\nSlope Parameter: " + str(self.sig_slope_param) + "\n"
	
	def set_activation_function_tan_hyperbolic(self, slope_param = 1):
		#Sets activation function as a tangent hyperbolic function.
		# This is a useful activation function because there is a 'soft' 
		# change from -1 to 1. This function differes from the sigmoid
		# function in that it allows negative neural output values. 
		
		self.activation_function = self.tan_hyperbolic
		self.d_activation_function = self.d_tan_hyperbolic
		
	
		
## ---------- Different Cost Functions ----------			
		
	def quadratic_cost_function(self, exp_value_array, calc_val_array):
		# Both params are 2d arrays with the values in columns equal to
		# output from a certain set of inputs. The number of columns is 
		# equal to the number of values trained on. array sizes should
		# match.
		

		num_values = exp_value_array.shape[1]
		
		cost_vector = (np.sum(((exp_value_matrix - calc_val_matrix)**2), \
								axis=1, keepdims=True)) / (2.0 * num_values)
		
		return cost_vector
		
	def d_quadratic_cost_function(self, exp_vector, calc_vector):
		# Takes the expected value and the calculated value
		# as parameters and returns the derivative of the quadratic cost
		# function for those values.
		
		return calc_vector - exp_vector

## ----------Network Storage and Loading ----------

	def save_network(self, filename):
		network_string = ""
		network_string += "Network Saved: " + str(datetime.datetime.now()) + "\n"
		network_string += self.cost_string
		network_string += self.activation_string
		network_string += "Weights Array: \n"
		network_string += str(self.weights_array)
		network_string += "\nBias Array: \n"
		network_string += str(self.bias_array)
		fout = open(filename, "w")
		fout.write(network_string)
		fout.close()
		return True
		
		
	def load_network(self, network_file):
		default_network = Network(1, 1, [1,1,1])
		fin = open(network_file, 'r')
		fin_str = fin.read()
		print fin_str
				
def test():
	test_input = []
	test_output = []
	for i in range(10000):
		in_val1 = random.uniform(-2, 2)
		out_val1 = abs(math.sin(in_val1))
		in_val2 = random.uniform(-2, 2)
		out_val2 = abs(math.sin(in_val2))
		test_input.append([in_val1, in_val2])
		test_output.append([out_val1, out_val2])

	
	start = time.clock()	
	test_network = Network(2, 2, [15, 50, 2])
	test_network.save_network("HELLO.txt")
	test_network.load_network("HELLO.txt")
	raise ValueError()

	#test_network.batch_train(test_input, test_output, 5)
	test_network.stochastic_train(test_input, test_output, 10, 200, 100, 4, 2)
	#print test_network.weights_array
	#print test_network.bias_array
	#test_network.save_network("TESTFILE")
	for j in range(10):
		rand_to_test1 = random.uniform(-2, 2)
		rand_to_test2 = random.uniform(-2, 2)
		print "Output of Network"
		out = test_network.evaluate_network([rand_to_test1, rand_to_test2])
		print out
		print "Correct Output"
		print [abs(np.sin(rand_to_test1)), abs(np.sin(rand_to_test2))]
		#print "Error"
		#print abs((abs(np.sin(rand_to_test))) - out[0]) / abs(np.sin(rand_to_test)) * 100
	end = time.clock()
	print "Elapsed: ", (end - start)
test()
		
		 
						
		
