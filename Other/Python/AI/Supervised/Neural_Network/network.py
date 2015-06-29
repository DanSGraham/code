#A program to connect neurons in a network, adjust weights
#I did most of my research from this great resource:
#http://neuralnetworksanddeeplearning.com/chap1.html
#import numpy

#TODO: 1. Add matrix functionality to speed up considerably. 
#			Current version is for learning purposes.
#		2. Add recurrent feature.
#		3. Add genetic weight adjustment.
#		4. Add fuzzy logic
#		5. Other kinds of NN

from neuron import *

class Network:
	
	
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
					error_in_neuron = (calc_val_vector - exp_val_vector) \
					* self.neural_network[i][j].d_activation_function(self.input_sum)
					self.neural_network[i][j].set_error(error_in_neuron)
			else:
				for k in range(self.neural_network[i]): #Iterate through other layers setting errors.
					#not sure how to calculate the error in other layers.
					error_in_neuron = 
					
		
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
		
	
				
			
			
				
				
