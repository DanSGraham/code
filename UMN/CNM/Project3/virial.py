import math

rc2 = 81.0

def vir_calc_methane(box_length, box_width, coord):
	sigma = 3.73
	epsilon = 169.
	vir = 0.0
	n = len(coord)
	l = box_length
	w = box_width
	for i in range(0, n-1):
		particle_1 = coord[i]
		for j in range(i+1, n):
			particle_n = coord[j]
			dist = particle_1 - particle_n
			dist[0] = dist[0] - round(dist[0]/l) * l
			dist[1] = dist[1] - round(dist[1]/l) * l
			dist[2] = dist[2] - round(dist[2]/w) * w
			
			dist2 = dist ** 2
			r2 = sum(dist2)
			
			if r2 < rc2:
				r6 = r2 ** 3.
				vir += ((24 * epsilon * (sigma ** 6)) * (1./r6) * (2 * (sigma ** 6) * (1./r6) - 1))#*(10.**-20.)
	return vir


def vir_calc_graphene(box_length, box_width, coord, graphene_coord):
	sigma = 3.71
	epsilon = 76.
	vir = 0.0
	n = len(coord)
	g_n = len(graphene_coord)
	l = box_length
	w = box_width
	for i in range(g_n):
		particle_1 = graphene_coord[i]
		for j in range(n):
			particle_n = coord[j]
			dist = particle_1 - particle_n
			dist[0] = dist[0] - round(dist[0]/l) * l
			dist[1] = dist[1] - round(dist[1]/l) * l
			dist[2] = dist[2] - round(dist[2]/w) * w
			
			dist2 = dist ** 2
			r2 = sum(dist2)
			
			if r2 < rc2:
				r6 = r2 ** 3.
				vir += ((24 * epsilon * (sigma ** 6)) * (1./r6) * (2 * (sigma ** 6) * (1./r6) - 1))#*(10.**-20.)
	return vir
