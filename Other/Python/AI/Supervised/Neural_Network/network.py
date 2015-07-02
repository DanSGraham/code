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

#import numpy

#TODO: 
#		0. Check over code. Do all the functions act correctly? Are they named appropriately? Commented so anyone can pick it up and understand how it works?
#		1. Add matrix functionality to speed up considerably. 
#			Current version is for learning purposes.
#		2. Add recurrent feature.
#		3. Add genetic weight adjustment.
#		4. Add fuzzy logic
#		5. Other kinds of NN

from neuron import *
import math

class Network:
	#A class to specify a network of neurons
	
	def __init__(self, num_input_vals, num_poss_out, num_neurons_array):
		
		self.neural_network = []
		self.learn_rate = 1.0
		#num_poss_out should be the same as the last number in \
		#num_neurons_array.
		
		#Create initial layer.
		temp_array = []
		prev_layer = -1
		for num_in_layer in num_neurons_array:
			temp_array = []
			for i in range(num_in_layer):
				if prev_layer != -1:
					#If not the first layer, it creates all neurons and 
					#Connects them to the previous layer
					
					new_neuron = Neuron(num_neurons_array[prev_layer])
					for it_neuron in self.neural_network[prev_layer]:
						it_neuron.connect_neuron(new_neuron)
					
				else:
					new_neuron = Neuron(num_input_vals)
					
				temp_array.append(new_neuron)
			prev_layer += 1
				
			self.neural_network.append(temp_array)

	def set_learn_rate(self, new_learn_rate):
		self.learn_rate = new_learn_rate
		
	def quad_calc_error(self, exp_val_vector, calc_val_vector):
		#Sets the error variable of each neuron based on inputs and outputs.
		#Currently for the quadratic cost function only.
		for i in range((len(self.neural_network) - 1), 0, -1):
			#Iterates through each layer in the network and assigns
			#errors to the neurons.
			
			if i >= (len(self.neural_network) - 1): #Set error of output layer
				for j in range(len(calc_value_vector)): #Both vectors must align.
					error_in_neuron = (calc_val_vector[j] - exp_val_vector[j]) \
					* self.neural_network[i][j].d_activation_function(self.neural_network[i][j].input_sum)
					self.neural_network[i][j].set_error(error_in_neuron)
			else:
				for k in range(self.neural_network[i]): #Iterate through other layers setting errors.
					#not sure how to calculate the error in other layers.
					error_in_neuron = 0
					curr_neuron = self.neural_network[i][k]
					for down_neuron in curr_neuron.downstream_neurons:
						error_in_neuron += down_neuron.weights[k] * \
											down_neuron.error
					error_in_neuron *= curr_neuron.d_activation_function(curr_neuron.input_sum)
					curr_neuron.error = error_in_neuron

					
					
		
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
				
		for unaveraged_val in out_vector:
			averaged_val = unaveraged_val / (2,0 * len(calc_val_matrix))
			cost_vector.append(averaged_val)
		
		return cost_vector
		
				
			
			
				
				
