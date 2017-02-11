#A program to simulate a MonteCarlo Thing
#By Daniel Graham

import math
import energy_lj
from random import randint
import random

displacement_l = 0.1

def sample(n, l, beta, en_save, coord):
	part_chosen = randint(0, num_particles - 1)
	rx = (random.random() - 0.5) * displacement
	ry = (random.random() - 0.5) * displacement
	rz = (random.random() - 0.5) * displacement
	coord[part_chosen] = coord[part_chosen] * [ rx, ry, rz]
	en = energy_lj.energy_calc(n, l, coord)
	print 'energy', en
	if random.random() > math.exp(-beta * en - en_save):
		coord[part_chosen] = coord[part_chosen] - [ rx, ry, rx]
		print "Reject step"
	return en
