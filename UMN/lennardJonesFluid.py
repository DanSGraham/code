#A program to simulate a Lennard Jones Fluid
#By Daniel Graham


#TODO
#Fill box with particles and visualize
#Connect the energy component
#compare to his code

import math

class Box:

	def __init__(self, length, numParticles):
		self.length = length
		self.numParticles = numParticles
		self.particleList = []
		self.fillBox()
		
	
	def fillBox(self):
		#First take the cube root to determine how many particles 
		#Will go in a direction of the box.
		numPartPerDim = math.ceil(self.numParticles ** (1./3))
		d_btwn_particles = (self.length / numPartPerDim)
		initial_pos = [d_btwn_particles/2, d_btwn_particles/2, d_btwn_particles/2]
		curr_pos = initial_pos
		x = 0
		y = 0
		z = 0
		for p in range(self.numParticles):
			if x >= numPartPerDim:
				y += 1
				x = 0
			if y >= numPartPerDim:
				z += 1
				y = 0
			if z >= numPartPerDim:
				print "HOUSTON, WE HAVE A PROBLEM"	
			newParticle = Particle([initial_pos[0] + d_btwn_particles * x,\
			 initial_pos[1] + d_btwn_particles * y,\
			 initial_pos[2] + d_btwn_particles * z])
			self.particleList.append(newParticle)
			x += 1

class Particle:
	
	def __init__(self, coordList):
		self.coordList = coordList

	def setXCoord(self, newXCoord):
		self.coordList[0] = newXCoord

	def setYCoord(self, newYCoord):
		self.coordList[1] = newYCoord

	def setZCoord(self, newZCoord):
		self.coordList[2] = newZCoord

	def setCoordList(self, newCoordList):
		self.coordList = newCoordList	

def main():
	box = Box(10,500)

main()
