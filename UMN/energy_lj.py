#A program to calculate the Leonard Jones Energy
#By Daniel Graham

import math

r_cutoff = 10.0
rc2 = r_cutoff ** 2.0
rc6 = r_cutoff ** 6.0
rc12 = r_cutoff ** 12.0

ecut = 4.0 * ((1/rc12) - (1/rc6))

def energy_cal(num_particles, length, coord):
	en = 0.0
	for i in range (0, n-1):
		particle_1 = coord[i]
		for j in range(i + 1, n):
			particle_n = coord[j]
			dist = particle_1 - particle_n
			for k in range(len(dist)):
				dist[k] = dist[k] - round(dist[k]/l) * l
			dist2 = dist ** 2
			r2 = sum(dist2)
			if r2 < rc2:
				r6 = r2 ** 3.0
				r12 = r2 ** 6.0
				en += 4.0 * ((1/r12) - (1/r6))
	return en


				
