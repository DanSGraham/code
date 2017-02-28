#A program to initialize velocities of n particles
#By Daniel Graham

import random
import math
import numpy as np

#6x6x6 with 108 particles. cutoff of 3

def calc_vel(num_particles, temp):
	avg_V = (((3./2.) * temp * num_particles) ** (1./2.))
	x_v = []
	y_v = []
	z_v = []
	totalV = 0.0
	totalV2 = 0
	for i in range(num_particles):
		x = random.uniform(-avg_V, avg_V)
		y = random.uniform(-avg_V, avg_V)
		z = random.uniform(-avg_V, avg_V)
		x_v.append(x)
		y_v.append(y)
		z_v.append(z)

	x_sum = float(sum(x_v)) / float(num_particles)
	y_sum = float(sum(y_v)) / float(num_particles)
	z_sum = float(sum(z_v)) / float(num_particles)
	
	for j in range(num_particles):
		x_v[j] = (x_v[j] - x_sum)
		y_v[j] = (y_v[j] - y_sum)
		z_v[j] = (z_v[j] - z_sum)
		totalV += (x_v[j] ** 2. + y_v[j] ** 2. + z_v[j] ** 2.)
	
	scale_factor = (((3./2.) * temp) / (totalV / num_particles)) ** 0.5
	
	#Readjust the velocities to scale
	
	for k in range(num_particles):
		x_v[k] = (x_v[k]) * scale_factor 
		y_v[k] = (y_v[k]) * scale_factor
		z_v[k] = (z_v[k]) * scale_factor
		totalV2 += (x_v[k] ** 2. + y_v[k] ** 2. + z_v[k] ** 2.)

	return np.column_stack((x_v, y_v, z_v))
