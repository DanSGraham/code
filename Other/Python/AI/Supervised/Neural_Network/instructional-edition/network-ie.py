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

## THIS IS UNOPTIMIZED!!! This neural network is part of a system that 
# uses iteration instead of matrix operations. Matrix operations are 
## much faster but sometimes more difficult to understand, or install 
## modules to accomplish them. The optimized version uses numpy for 
## matrix operations.

#TODO: 
#		0a. Add different cost functions
#		1. Add matrix functionality to speed up considerably. 
#			Current version is for learning purposes.
#		2. Add recurrent feature.
#		3. Add genetic weight adjustment.
#		4. Add fuzzy logic
#		5. Other kinds of NN

from neuron import *
import math
import random
import datetime


class Network:
	#A class to specify a network of neurons
	def __init__(self, num_input_vals, num_poss_out, num_neurons_array):
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
								layer."""
								
		self.neural_network = [] 

		#Create initial layer.
		prev_layer = -1
		for num_in_layer in num_neurons_array:
			
			layer_array = []#Each index of the network_array is an array
							# built in the layer_array variable.
			for i in range(num_in_layer):
				if prev_layer != -1:
					#If not the first layer, it creates all neurons and 
					#Connects them to the previous layer
					
					new_neuron = Neuron(num_neurons_array[prev_layer])
					#The number of inputs for non-input layers is the 
					#number of neurons in the previous layer.
					
					for it_neuron in self.neural_network[prev_layer]:
						it_neuron.connect_neuron(new_neuron)
					#Connects the neurons in the previous layer to 
					#the next layer.
					
				else:
					new_neuron = Neuron(num_input_vals)
					#In the input layer, the neuron has the same number
					#of inputs as the number of possible inputs to the 
					#network and can't connect becaues there are no
					#other neurons yet.
					
				layer_array.append(new_neuron)
				
			prev_layer += 1
				
			self.neural_network.append(layer_array)

		self.set_quadratic_cost_function()	#Default cost fxn.
			
	def calc_error(self, exp_val_vector, calc_val_vector):
		#Sets the error variable of each neuron based on inputs and 
		#outputs.
		#Parameters:
			#exp_val_vector is the expected output of a specific trial 
			#in an array. If there is only one output expected for each 
			#trial, the array will be of size 1.
			#
			#calc_val_vector is the calculated output of the network
			#given in an array. The indices of the calculated output
			#should match the indices of the expected output
			#(exp_val_vector).
		
		for i in range((len(self.neural_network) - 1), -1, -1):
			#Iterates through each layer in the network and assigns
			#errors to the neurons starting at the output layer.
			
			if i >= (len(self.neural_network) - 1): #Set error of output layer
				for j in range(len(calc_val_vector)): #Both vectors must align.
					curr_neuron = self.neural_network[i][j]
					error_in_neuron = (self.d_cost_function(exp_val_vector[j], calc_val_vector[j]) \
					* curr_neuron.d_activation_function(curr_neuron.input_stimulus))
					curr_neuron.set_error(error_in_neuron)
					
			else:
				for k in range(len(self.neural_network[i])): #Iterate through other layers setting errors.
					error_in_neuron = 0.0
					curr_neuron = self.neural_network[i][k]
					
					for down_neuron in curr_neuron.downstream_neurons:
						error_in_neuron += down_neuron.weights[k] * \
											down_neuron.error
											
					error_in_neuron *= curr_neuron.d_activation_function(curr_neuron.input_stimulus)
					
					#For each neuron [k] in the layer [i] the weights of 
					#the downstream neurons which have inputs directed 
					#to [k] are multiplied by the error in the 
					#downstream neuron, essentially passing the error 
					#through the network. The weighted errors are summed 
					#and then multiplied by the derivative of the 
					#current layer activation function on the current 
					#layer's input associated with this cost.
					
					curr_neuron.set_error(error_in_neuron)
							
	def set_quadratic_cost_function(self):
		self.cost_function = self.quadratic_cost_function
		self.d_cost_function = self.d_quadratic_cost_function
		
	def set_learn_rate(self, new_learn_rate):
		self.learn_rate = new_learn_rate
		
## ---------- Different Cost Functions ----------			
		
	def quadratic_cost_function(self, exp_value_matrix, calc_val_matrix):
		#Both params are 2d matrices with the values in columns equal to
		#output from a certain set of inputs. The number of columns is 
		#equal to the number of values trained on.
		out_vector = []
		cost_vector = []
		#The total cost vector at the end of the calculation.
		
		for i in range(calc_val_martix):
			for j in range(calc_val_matrix[i]):
				vector_val = (exp_value_matrix[i][j] - \
								calc_val_matrix[i][j])**2
				if i == 0:
					out_vector.append(vector_val)
				else:
					out_vector[j] += vector_val
			
		#out_vector is the sum for every output of every individual 
		#neuron. Each index of the out_vector corresponds to a neuron
		#in the output layer.
			
		for unaveraged_val in out_vector:
			averaged_val = unaveraged_val / (2.0 * len(calc_val_matrix))
			cost_vector.append(averaged_val)
		
		#each index of cost_vector corresponds to the same neuron as the
		#index of the out_vector.
		
		return cost_vector
		
	def d_quadratic_cost_function(self, exp_val, calc_val):
		#Takes the expected value and the calculated value
		#as parameters and returns the derivative of the quadratic cost
		#function for those values.
		
		return calc_val - exp_val
	
## ---------- Different training methods ----------

	def batch_train(self, input_matrix, output_matrix, batch_size):
		#Trains the network using a batch backpropagation method.
		#Sums the errors of however many training examples present in 
		#batch_size. Then updates the weights according to that sum.
		for i in range(0, len(input_matrix), batch_size):
			for j in range(batch_size):
				calc_out_vector = self.evaluate_network(input_matrix[i + j])
				self.update_d_cost_values(output_matrix[i + j], \
										calc_out_vector)
				self.clear_network_inputs()
				
			self.update_network(1.0)
			
	def online_train(self, input_vector, output_vector):
		#Takes one input and output set and trains the network on that
		#one set. Usees the batch_training function with a batch of 1.
		self.batch_train(input_vector, output_vector, 1)
	
	
	def stochastic_train(self, input_matrix, output_matrix, train_size, \
							test_size, max_num_epochs, report_epochs, \
							max_error_value):
								 
		# Trains using a stochastic method. Randomizes input to 
		# determine an approximation of the cost function on a smaller
		# data set. May speed up learning in some cases.							
		error_val = 100
		num_epochs = 0
		while not (error_val < max_error_value or num_epochs >= max_num_epochs):
			
			#Trains the network.
			for i in range(report_epochs):
				self.stochastic_single_epoch_train(input_matrix, \
								output_matrix, train_size)
				num_epochs += 1
			
			# Network is tested and error determined. Testing is done
			# in a very similar way to training, only without using the
			# whole data set as the test set.
			random_index_list = [i for i in range(len(input_matrix))]
			random.shuffle(random_index_list)
			train_error = 0.0
			for j in range(test_size):
				temp_error = 0
				test_out = self.evaluate_network(input_matrix[random_index_list[j]])
				self.clear_network_inputs()
				corr_out = output_matrix[random_index_list[j]]
				for k in range(len(test_out)):
					temp_error += (abs(corr_out[k] - test_out[k]) / float(corr_out[k])) * 100.0
				
				temp_error = temp_error / len(test_out)
				train_error += temp_error
				
			train_error = train_error / test_size
			error_val = train_error
			print "Number of Epochs: ", num_epochs
			print "Average Error of test set: ", error_val 
								
								
	def stochastic_single_epoch_train(self, input_matrix, output_matrix, train_size):
		# Performs training through one epoch, or using the entire input
		# matrix once.
		
		
		#First the input/output matrix pairs are placed up randomly
		#into mini-batch buckets.
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
		
				
		#Then each batch is trained on the network.
		for bucket in batch_buckets:
			for j in range(len(bucket)):
				calc_out_vector = self.evaluate_network(bucket[j][0])
				self.update_d_cost_values(bucket[j][1], \
									calc_out_vector)
				self.clear_network_inputs()
			
			self.update_network(len(bucket))
	
	def standard_train(self, input_matrix, output_matrix):
		#Trains the network on a set of input values and output values
		#(input_matrix and output_matrix respectively)
		
		self.online_train(input_matrix, output_matrix)	
						
	def update_d_cost_values(self, exp_val_vector, calc_val_vector):
		#Updates the weight_cost_vector and bias cost vector based
		#on the weights.
		
		self.calc_error(exp_val_vector, calc_val_vector)
		
		for i in range(len(self.neural_network)):
			for j in range(len(self.neural_network[i])):
				curr_neuron = self.neural_network[i][j]
				curr_neuron.add_d_weight_cost_vector()
				curr_neuron.add_d_bias_cost()
	
	
					
	def update_network(self, norm_factor):
		#Updates the weights of the network based on the slope of the 
		#cost function and the learn rate..
			
		#The weights and biases are adjusted:
		for i in range(len(self.neural_network)):
			for j in range(len(self.neural_network[i])):
				curr_neuron = self.neural_network[i][j]
				curr_neuron.adjust_weights(norm_factor)
				curr_neuron.adjust_bias(norm_factor)
				curr_neuron.clear_d_weight_cost_vector()
				curr_neuron.clear_d_bias_cost()

					
	def evaluate_network(self, input_vector):
		# Evaluates the network and returns the calculated vector.
		
		calculated_vector = []
		#Assigns the input vector to each input neuron as the input.
		#Then it sends the signal to the next layer in the same step.
		for input_neuron in self.neural_network[0]:
			input_neuron.set_input(input_vector)
			input_neuron.send_signal()
			
		#Next all hidden layers send the signal
		for j in range(1, (len(self.neural_network) - 1)):
			for hid_neuron in self.neural_network[j]:
				hid_neuron.send_signal()
				
		#Lastly, the output layer is evaluated
		
		for out_neuron in self.neural_network[-1]:
			calculated_vector.append(out_neuron.send_signal())
		
		return calculated_vector	
	
	def clear_network_inputs(self):
		#Clears the inputs currently stored in the network and prepares
		#the network for another set of input values.
		for neural_layer in self.neural_network:
			for neuron in neural_layer:
				neuron.clear_input()
				
										

			
## ----------- Network storage and retrieval ----------
		
	def save_network(self, output_file):
		#A function to save the weights and biases of a network
		#So the learning can be preserved.
		
		#Build network header
		network_string = str(datetime.datetime.now()) + "\n"
		network_string += "["
		for i in range(len(self.neural_network)):
			if i < (len(self.neural_network) - 1):
				network_string += (str(len(self.neural_network[i])) + ", ")
			else:
				network_string += (str(len(self.neural_network[i])))
		network_string += "]\n"
		
		for j in range(len(self.neural_network)):
			network_string += ("Layer " + str(j) + ":\n")
			for neuron in self.neural_network[j]:
				network_string += ("(" + str(neuron.weights) + ", " + str(neuron.bias) + ")\n")
				
		fout = open(output_file, "w")
		fout.write(network_string)
		fout.close()
		
	def load_network(self, input_file):
		#A function to load a previously saved network.
		fin = open(input_file, "r")
		input_string = fin.read()
		fin.close()
		input_list = input_string.split("\n")
		
		try:
			network_layers_list = eval(input_list[1])
		except:
			print "Error opening file"
			return
		
		network_build = []
		prev_layer = -1
		for layer_size in network_layers_list:
			layer_list = []
			for i in range(layer_size):
				if prev_layer != -1:
					#If not the first layer, it creates all neurons and 
					#Connects them to the previous layer
					
					new_neuron = Neuron(network_layers_list[prev_layer])
					#The number of inputs for non-input layers is the 
					#number of neurons in the previous layer.
					
					for it_neuron in network_build[prev_layer]:
						it_neuron.connect_neuron(new_neuron)
					#Connects the neurons in the previous layer to 
					#the next layer.
					
				else:
					new_neuron = Neuron(num_input_vals)
					#take input vals from teh weights of the saved value.
					
				layer_list.append(new_neuron)
			prev_layer += 1
			network_build.append(layer_list)
			
		self.neural_network = network_build	
		
		
				
def test():
	test_input = []
	test_output = []
	for i in range(10000):
		in_val = random.uniform(-2, 2)
		out_val = abs(math.sin(in_val))
		test_input.append([in_val])
		test_output.append([out_val])

		
	test_network = Network(1, 1, [15, 50, 1])
	test_network.stochastic_train(test_input, test_output, 1, 15, 10, 5, 1)
	test_network.save_network("TESTFILE")
	for j in range(10):
		rand_to_test = random.uniform(-2, 2)
		print "Output of Network"
		out = test_network.evaluate_network([rand_to_test])
		print out
		test_network.clear_network_inputs()
		print "Correct Output"
		print abs(math.sin(rand_to_test))
		print "Error"
		print abs((abs(math.sin(rand_to_test))) - out[0]) / abs(math.sin(rand_to_test)) * 100
	
test()
		
		 
						
		
