#A program to connect neurons in a network, adjust weights
#import numpy
from neuron import *

class Network:
	
	
	def __init__(self, num_input_vals, num_poss_out, num_neurons_array):
		
		self.neural_network = []
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
						it_neuron.connectNeuron(new_neuron)
					
				else:
					new_neuron = Neuron(num_inputs)
					
				temp_array.append(new_neuron)
			prev_layer += 1
				
			self.neural_network.append(temp_array)
			
		
test = Network(5, 5, [1,4,4,5])
			
				
				
