# Take the box measurements and compute initial coordinates
import math
import numpy as np
 
def init_coord(n,l):
	volume = l**3.
	n_3 = round(n**(1./3.))
	clen = math.ceil(volume/(n_3**3.))
	p_box = clen**(1./3.)
	ii = int(round(n**(1./3.)))
	iii = int(n-ii**3)
	if iii < 0:
		iii = 0 
	else:
		iii = int(math.ceil(iii**(1./3.)))
	x = []
	y = []
	z = []
	jj = 0
	p_box1 = p_box*(float(ii)/(ii+iii))
	for i in xrange(int(ii+iii)):
		for j in xrange(ii):
			for k in xrange(ii):  
				jj = jj + 1
				if jj > n:
					break
				if k % 2 == 1:
					x.append(p_box1*i+p_box/2.)
					y.append(p_box*j+p_box/2.)
				else:
					x.append((p_box1*i+p_box) % l)
					y.append((p_box*j+p_box) % l)

				z.append(p_box*k+p_box/2.)
	return np.column_stack((x, y, z))



