#A program to calculate the energy of a diatomic molecule from Hartree-Fock methods
#By Daniel Graham

#TODO: condense basis
#Add DFT

import numpy as np
import math

#Parameters are STO-3G taken from EMSL
H_alpha_params = np.matrix([[3.42525091, 0.62391373, 0.16885540]])
He_alpha_params = np.matrix([[6.36242139, 1.15892300, 0.31364979]])

#Values are in angstroms
H_intNucDist = 1.4
He_intNucDist = 3.779452263

#A function to normalize the eigenfxns
#Inputs: basis set
#Outputs: normalization_factors
def normalizeBasisSet(basisSet):
	normalization_Factors = np.copy(basisSet)
	normalization_Factors = (np.power((normalization_Factors * 2) / (math.pi), (3./4.)))
	return normalization_Factors

#A function to create a normalization matrix
def normalizeMatrix(norm1, norm2):
	row = np.concatenate((norm1, norm2), axis=1)
	column = row.T
	return np.multiply(row, column)
	
#A function to return the overlap matrix S
#Inputs: 2 gaussian alpha parameter matrices, and the internuclear distance
#Outputs: Numpy matrix of S
def overlapMatrix(basis_aParam1, basis_aParam2, intNucDist):
	#Equation found for formula in Modern Quantum Chemistry by Szabo eqn A.9 pg 412

	a = basis_aParam1
	b = a.T
	coeff = np.power((math.pi/(a + b)), (3./2.))
	exponent = 0
	basis_aParam1_matrix = coeff
	
	a = basis_aParam2
	b = a.T
	coeff = np.power((math.pi/(a + b)), (3./2.))
	exponent = 0
	basis_aParam2_matrix = coeff
	
	a = basis_aParam1
	b = basis_aParam2.T
	coeff = np.power((math.pi/(a + b)), (3./2.))
	exponent = -1 * (np.multiply(a,b)/(a + b)) * (intNucDist ** 2.)
	basis_param1byparam2_matrix = np.multiply(coeff, np.exp(exponent))
	
	basis_param2byparam1_matrix = basis_param1byparam2_matrix.T
	
	matrix1 = np.concatenate((basis_aParam1_matrix, basis_param1byparam2_matrix))
	matrix2 = np.concatenate((basis_param2byparam1_matrix, basis_aParam2_matrix))
	matrix = np.concatenate((matrix1, matrix2), axis=1)
	
	return matrix
	
#A function to return the kinetic energy matrix
#Inputs: Basis vectors, internuclear distance
#Output: Kinetic Energy Matrix
def kineticEnergy(basis_aParam1, basis_aParam2, intNucDist):

	#Equation found for formula in Modern Quantum Chemistry by Szabo eqn A.11 pg 412
	a = basis_aParam1
	b = a.T
	mult1 = (np.multiply(a,b))/(a + b)
	mult2 = 3.
	mult3 = np.power((math.pi/(a + b)), (3./2.))
	mult4 = 1.
	basis_aParam1_matrix = np.multiply(np.multiply(mult1, mult2), np.multiply(mult3, mult4))
	
	a = basis_aParam2
	b = a.T
	mult1 = (np.multiply(a,b))/(a + b)
	mult2 = 3.
	mult3 = np.power((math.pi/(a + b)), (3./2.))
	mult4 = 1.
	basis_aParam2_matrix = np.multiply(np.multiply(mult1, mult2), np.multiply(mult3, mult4))
	
	a = basis_aParam1
	b = basis_aParam2.T
	mult1 = (np.multiply(a,b))/(a + b)
	exponent1 = (-1 *(np.multiply(a,b)/(a + b)) * (intNucDist ** 2.))
	mult2 = 3. + 2. * exponent1
	mult3 = np.power((math.pi/(a + b)), (3./2.))
	mult4 = np.exp(exponent1)	
	basis_param1byparam2_matrix = np.multiply(np.multiply(mult1, mult2), np.multiply(mult3, mult4))
	
	basis_param2byparam1_matrix = basis_param1byparam2_matrix.T
	
	matrix1 = np.concatenate((basis_aParam1_matrix, basis_param1byparam2_matrix))
	matrix2 = np.concatenate((basis_param2byparam1_matrix, basis_aParam2_matrix))
	matrix = np.concatenate((matrix1, matrix2), axis=1)
	
	return matrix
	
#A function to return the potential energy matrix for core Hamiltonian
#Inputs: 2 basis vectors, nuclear charge, internuclear distance, a boolean swap
#Output: Potential energy matrix
#Swap is used if the order of the basis sets has been swapped and must be adjusted in the final matrix
def potentialNucEnergy(potential_onNuc_basis, basis_aParam2, intNucDist, nucCharge, swap):
	#Equation found for formula in Modern Quantum Chemistry by Szabo eqn A.33 pg 415
	#Always assume potential_onNuc_basis is zeroed on the nucleus which charge is specified
	
	#TODO:Check answers with John
	
	a = potential_onNuc_basis
	b = a.T
	coeff = ((-2 * math.pi)/(a + b)) * nucCharge
	exponent = 0
	f0_Function_input = 0
	f0_Function = 1
	potential_onNuc_basis_matrix = coeff
	
	a = basis_aParam2
	b = a.T
	coeff = ((-2 * math.pi)/(a + b)) * nucCharge
	exponent = 0
	f0_function_input = (a + b) * (intNucDist ** 2)
	f0_erf = np.power(f0_function_input, .5)
	for x in np.nditer(f0_erf, op_flags=['readwrite']):
		x[...] = math.erf(x)
	f0_Function = 0.5 * np.multiply(np.power((math.pi/f0_function_input), .5), f0_erf)
	basis_aParam2_matrix = np.multiply(coeff, f0_Function)
	
	a = potential_onNuc_basis
	b = basis_aParam2.T
	coeff = ((-2 * math.pi)/(a + b)) * nucCharge
	exponent = (-1 * (np.multiply(a,b)/(a + b)) * (intNucDist ** 2))
	f0_function_input = ((a * 0) + np.power((b * intNucDist), 2.))/(a + b)
	f0_erf = np.power(f0_function_input, .5)
	for x in np.nditer(f0_erf, op_flags=['readwrite']):
		x[...] = math.erf(x)
	f0_Function = 0.5 * np.multiply(np.power((math.pi/f0_function_input), .5), f0_erf)
	
	basis_set1toset2_matrix = np.multiply(np.multiply(coeff, f0_Function), np.exp(exponent))
	
	basis_set2toset1_matrix = basis_set1toset2_matrix.T
	
	
	if (swap):
		matrix1 = np.concatenate((basis_aParam2_matrix, basis_set1toset2_matrix))
		matrix2 = np.concatenate((basis_set2toset1_matrix, potential_onNuc_basis_matrix))
		matrix = np.concatenate((matrix1, matrix2), axis=1)
		
	else:
		matrix1 = np.concatenate((potential_onNuc_basis_matrix, basis_set2toset1_matrix))
		matrix2 = np.concatenate((basis_set1toset2_matrix, basis_aParam2_matrix))
		matrix = np.concatenate((matrix1, matrix2), axis=1)
		
	return matrix
	
#A function to return the core Hamiltonian matrix
#Inputs: Two basis vectors, internuclearDistance, nuclear charge of both atoms
#Outputs: Core Hamiltonian matrix
def coreHamiltonian(basis_aParam1, basis_aParam2, intNucDist, nucCharge1, nucCharge2):
	#Calculate Kinetic Energy matrix
	T_Matrix = kineticEnergy(basis_aParam1, basis_aParam2, intNucDist)
	v1_Matrix = potentialNucEnergy(basis_aParam1, basis_aParam2, intNucDist, nucCharge1, False)
	v2_Matrix = potentialNucEnergy(basis_aParam2, basis_aParam1, intNucDist, nucCharge2, True)
	return T_Matrix + v1_Matrix + v2_Matrix

#A helper function to determine the repulsionCalculation
def repulsionCalculation(a, b, c, d, rAB, rCD, rPQ):
	firstTerm = (2 * math.pi ** (5./2.))/((a + b)*(c + d)*(a + b + c + d) ** .5)
	secondTerm = math.exp((((-a * b)/(a + b)) * (rAB ** 2)) - (((c * d)/(c + d)) * (rCD ** 2)))
	thirdTermInput = (((a + b)*(c + d))/(a + b + c + d)) * (rPQ ** 2)
	if thirdTermInput == 0:
		thirdTerm = 1
	else:
		thirdTerm = (.5 * ((math.pi/thirdTermInput)**.5)) * math.erf((thirdTermInput ** .5))
		
	return firstTerm * secondTerm * thirdTerm

"""Values not saved but instead calculated OTF in electronElectronIntegral
#A function to determine the electron-electron repulsion
#Input: basis sets for each atoms
#Output: Matrix of values
def electronElectronRepulsion(basis_aParam1, basis_aParam2, intNucDist, normMatrix):
	#Equation found for formula in Modern Quantum Chemistry by Szabo eqn A.41 pg 416
	#Check which basis a set is from to determine the intNucDistance
	
	#TODO:Normalize
	#Make matrix operations
	
	#Okay for now I have to do this iteratively. I can't think of a way to do it with matrices and also keep it general.
	
	matrix = []
	rAB = 0
	rCD = 0
	rPQ = 0
	for i0 in np.nditer(basis_aParam1):
		for i1 in np.nditer(basis_aParam1):
			row = []
			rCD = 0
			for i2 in np.nditer(basis_aParam1):
				for i3 in np.nditer(basis_aParam1):
					rAB = 0
					rPQ = 0
					row.append(repulsionCalculation(i2, i3, i0, i1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = intNucDist
					rPQ = (j3 / (i2 + j3)) * intNucDist
					row.append(repulsionCalculation(i2, j3, i0, i1, rAB, rCD, rPQ))
			for j2 in np.nditer(basis_aParam2):
				for i3 in np.nditer(basis_aParam1):
					rAB = intNucDist
					rPQ = (j2 / (j2 + i3)) * intNucDist
					row.append(repulsionCalculation(j2, i3, i0, i1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = 0
					rPQ = 2. * intNucDist
					row.append(repulsionCalculation(j2, j3, i0, i1, rAB, rCD, rPQ))
			matrix.append(row)
			
		for j1 in np.nditer(basis_aParam2):
			row = []
			rCD = intNucDist
			
			for i2 in np.nditer(basis_aParam1):
				for i3 in np.nditer(basis_aParam1):
					rAB = 0
					rPQ = -(j1/(i0 + j1)) * intNucDist
					row.append(repulsionCalculation(i2, i3, i0, j1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = intNucDist
					rPQ = ((j3 / (i2 + j3)) - (j1 / (i0 + j1))) * intNucDist
					row.append(repulsionCalculation(i2, j3, i0, j1, rAB, rCD, rPQ))
			for j2 in np.nditer(basis_aParam2):
				for i3 in np.nditer(basis_aParam1):
					rAB = intNucDist
					rPQ = ((j2 / (j2 + i3)) - (j1 / (i0 + j1))) * intNucDist
					row.append(repulsionCalculation(j2, i3, i0, j1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = 0
					rPQ = (2 - (j1/(i0 + j1))) * intNucDist
					row.append(repulsionCalculation(j2, j3, i0, j1, rAB, rCD, rPQ))
			matrix.append(row)
			
	for j0 in np.nditer(basis_aParam2):
		for i1 in np.nditer(basis_aParam1):
			row = []
			rCD = intNucDist
			
			for i2 in np.nditer(basis_aParam1):
				for i3 in np.nditer(basis_aParam1):
					rAB = 0
					rPQ = -(j0/(j0 + i1)) * intNucDist
					row.append(repulsionCalculation(i2, i3, j0, i1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = intNucDist
					rPQ = ((j3 / (i2 + j3)) - (j0 / (j0 + i1))) * intNucDist
					row.append(repulsionCalculation(i2, j3, j0, i1, rAB, rCD, rPQ))
			for j2 in np.nditer(basis_aParam2):
				for i3 in np.nditer(basis_aParam1):
					rAB = intNucDist
					rPQ = ((j2 / (j2 + i3)) - (j0/(j0 + i1))) * intNucDist
					row.append(repulsionCalculation(j2, i3, j0, i1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = 0
					rPQ = (2 - (j0/(j0 + i1))) * intNucDist
					row.append(repulsionCalculation(j2, j3, j0, i1, rAB, rCD, rPQ))
			matrix.append(row)
			
		for j1 in np.nditer(basis_aParam2):
			row = []
			rCD = 0
			for i2 in np.nditer(basis_aParam1):
				for i3 in np.nditer(basis_aParam1):
					rAB = 0
					rPQ = -2. * intNucDist
					row.append(repulsionCalculation(i2, i3, j0, j1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = intNucDist
					rPQ = ((j3 / (i2 + j3)) - 2) * intNucDist
					row.append(repulsionCalculation(i2, j3, j0, j1, rAB, rCD, rPQ))
			for j2 in np.nditer(basis_aParam2):
				for i3 in np.nditer(basis_aParam1):
					rAB = intNucDist
					rPQ = ((j2 / (j2 + i3)) - 2) * intNucDist
					row.append(repulsionCalculation(j2, i3, j0, j1, rAB, rCD, rPQ))
				for j3 in np.nditer(basis_aParam2):
					rAB = 0	
					rPQ = 0
					row.append(repulsionCalculation(j2, j3, j0, j1, rAB, rCD, rPQ))
			matrix.append(row)
			
	#Convert array to numpy array.
	outMatrix = np.matrix(matrix)
	
	#Normalize
	toNorm = []
	for i in np.nditer(normMatrix):
		toNorm.append(i)
		
	toNorm = np.matrix([toNorm])
	normMatrix = np.multiply(toNorm, toNorm.T)
	return np.multiply(outMatrix, normMatrix)
"""

#Function to determine the orthogonalization matrix for the fock operator
#Input: overlapMatrix
#Output: the orthoganalizationMatrix
#Check this function.
def orthonormalizationMatrix(overlapMatrix):
	sqrtDiagS = np.diag(np.power(np.linalg.eigh(overlapMatrix)[0], -.5))
	diagonalizingMatrixU = np.matrix(np.linalg.eigh(overlapMatrix)[1])
	return (diagonalizingMatrixU * sqrtDiagS)
	
#A function to determine coeffecients
#Input: orthoganalizationMatrix, fockMatrix
#Output: return the coefficient matrix	
def coeffMatrix(orthoganalizationMatrix, fockMatrix):
	orthonormalFock = (orthoganalizationMatrix.T) * fockMatrix * orthoganalizationMatrix
	coeffValues, coeffOrtho = np.linalg.eigh(orthonormalFock)
	actualCoeff = orthoganalizationMatrix * coeffOrtho
	return actualCoeff
 
#A function to determine the density matrix
#Input: The Coeffecient matrix
#Output: The densityMatrix
def densityMatrix(coeffMatrix, numElectrons):
	#For now assume that the 1 and 4th orbitals are the lowest two energy, but ideal method is to have that pre determined.
	#Szabo pg. 139, eqn. 3.145
	densityMatrix = np.copy(coeffMatrix)
	densityMatrix.fill(0)
	for i in range(numElectrons/2):
		prodMat = coeffMatrix[:,i]
		densityMatrix += np.multiply(prodMat, prodMat.T)
		
	return densityMatrix * 2

#A function to determine the two electron fock
#Input: the density matrix and the repulsion matrix
#Output: The two electron fock matrix (G)
def twoElectronFock(dMatrix, basis_1, basis_2, intNucDist, normMatrix):
	#Szabo pg. 141 3.154
	gMatrix = np.copy(dMatrix)
	gMatrix.fill(0)
	it1 = np.nditer(gMatrix, flags=['multi_index'])
	while not it1.finished:
		gMatrixIndex = it1.multi_index
		it2 = np.nditer(dMatrix, flags=['multi_index'])
		cellValue = 0
		while not it2.finished:
			if it1.multi_index[0] < basis_1.shape[1]:
				if it1.multi_index[1] < basis_1.shape[1]:
					if it2.multi_index[0] < basis_1.shape[1]:
						if it2. multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = 0
							rCD = 0
							rPQ = 0
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_1.item(b), basis_1.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b) * normMatrix.item(c,d)
							rAB = 0
							rCD = 0
							rPQ = 0
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_1.item(d), basis_1.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d) * normMatrix.item(c,b)
							
						else:
							a = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = 0
							rCD = intNucDist
							rPQ = (basis_2.item(d) * intNucDist) / (basis_1.item(c) + basis_2.item(d))
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_1.item(b), basis_1.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b) * normMatrix.item(c,d1)
							rAB = intNucDist
							rCD = 0
							rPQ = (basis_2.item(d) * intNucDist) / (basis_1.item(a) + basis_2.item(d))
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_2.item(d), basis_1.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d1) * normMatrix.item(c,b)
					else:
						if it2.multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = 0
							rCD = intNucDist
							rPQ = (basis_2.item(c) * intNucDist) / (basis_2.item(c) + basis_1.item(d))
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_1.item(b), basis_2.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b) * normMatrix.item(c1,d)
							rAB = 0
							rCD = intNucDist
							rPQ = (basis_2.item(c) * intNucDist) / (basis_2.item(c) + basis_1.item(b))
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_1.item(d), basis_2.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d) * normMatrix.item(c1,b)
						else:
							a = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = 0
							rCD = 0
							rPQ = intNucDist
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_1.item(b), basis_2.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b) * normMatrix.item(c1,d1)
							rAB = intNucDist
							rCD = intNucDist
							rPQ = (basis_2.item(d) * intNucDist) / (basis_1.item(a) + basis_2.item(d)) - (basis_2.item(c) * intNucDist) / (basis_2.item(c) + basis_1.item(b))
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_2.item(d), basis_2.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d1) * normMatrix.item(c1,b)
				else:
					if it2.multi_index[0] < basis_1.shape[1]:
						if it2. multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = intNucDist
							rCD = 0
							rPQ = (basis_2.item(b) * intNucDist) / (basis_1.item(a) + basis_2.item(b))
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_2.item(b), basis_1.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b1) * normMatrix.item(c,d)
							rAB = 0
							rCD = intNucDist
							rPQ = (basis_2.item(b) * intNucDist) / (basis_1.item(c) + basis_2.item(b))
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_1.item(d), basis_1.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d) * normMatrix.item(c,b1)
							
						else:
							a = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = intNucDist
							rCD = intNucDist
							rPQ = (basis_2.item(b) * intNucDist) / (basis_1.item(a) + basis_2.item(b)) - (basis_2.item(d) * intNucDist) / (basis_1.item(c) + basis_2.item(d))
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_2.item(b), basis_1.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b1) * normMatrix.item(c,d1)
							rAB = intNucDist
							rCD = intNucDist
							rPQ = (basis_2.item(d) * intNucDist) / (basis_1.item(a) + basis_2.item(d)) - (basis_2.item(b) * intNucDist) / (basis_1.item(c) + basis_2.item(b))
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_2.item(d), basis_1.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d1) * normMatrix.item(c,b1)
					else:
						if it2.multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = intNucDist
							rCD = intNucDist
							rPQ = (basis_2.item(b) * intNucDist) / (basis_1.item(a) + basis_2.item(b)) - (basis_2.item(c) * intNucDist) / (basis_2.item(c) + basis_1.item(d))
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_2.item(b), basis_2.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b1) * normMatrix.item(c1,d)
							rAB = 0
							rCD = 0
							rPQ = intNucDist
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_1.item(d), basis_2.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d) * normMatrix.item(c1,b1)
						else:
							a = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = intNucDist
							rCD = 0
							rPQ = ((basis_2.item(b) * intNucDist) / (basis_1.item(a) + basis_2.item(b))) - (intNucDist)
							repulsion1 = repulsionCalculation(basis_1.item(a), basis_2.item(b), basis_2.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a,b1) * normMatrix.item(c1,d1)
							rAB = intNucDist
							rCD = 0
							rPQ = ((basis_2.item(d) * intNucDist) / (basis_1.item(a) + basis_2.item(d))) - (intNucDist)
							repulsion2 = repulsionCalculation(basis_1.item(a), basis_2.item(d), basis_2.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a,d1) * normMatrix.item(c1,b1)
			else:
				if it1.multi_index[1] < basis_1.shape[1]:
					if it2.multi_index[0] < basis_1.shape[1]:
						if it2. multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = intNucDist
							rCD = 0
							rPQ = (basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(b))
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_1.item(b), basis_1.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b) * normMatrix.item(c,d)
							rAB = intNucDist
							rCD = 0
							rPQ = (basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(d))
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_1.item(d), basis_1.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d) * normMatrix.item(c,b)
							
						else:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = intNucDist
							rCD = intNucDist
							rPQ = (basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(b)) - (basis_2.item(d) * intNucDist) / (basis_1.item(c) + basis_2.item(d))
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_1.item(b), basis_1.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b) * normMatrix.item(c,d1)
							rAB = 0
							rCD = 0
							rPQ = intNucDist
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_2.item(d), basis_1.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d1) * normMatrix.item(c,b)
					else:
						if it2.multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = intNucDist
							rCD = intNucDist
							rPQ = (basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(b)) - (basis_2.item(c) * intNucDist) / (basis_2.item(c) + basis_1.item(d))
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_1.item(b), basis_2.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b) * normMatrix.item(c1,d)
							rAB = intNucDist
							rCD = intNucDist
							rPQ = (basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(d)) - (basis_2.item(c) * intNucDist) / (basis_2.item(c) + basis_1.item(b))
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_1.item(d), basis_2.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d) * normMatrix.item(c1,b)
						else:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = intNucDist
							rCD = 0
							rPQ = ((basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(b))) - (intNucDist)
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_1.item(b), basis_2.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b) * normMatrix.item(c1,d1)
							rAB = 0
							rCD = intNucDist
							rPQ = (intNucDist) - ((basis_2.item(c) * intNucDist) / (basis_2.item(c) + basis_1.item(b)))
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_2.item(d), basis_2.item(c), basis_1.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d1) * normMatrix.item(c1,b)
				else:
					if it2.multi_index[0] < basis_1.shape[1]:
						if it2. multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = 0
							rCD = 0
							rPQ = (intNucDist)
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_2.item(b), basis_1.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b1) * normMatrix.item(c,d)
							rAB = intNucDist
							rCD = intNucDist
							rPQ = ((basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(d))) - ((basis_2.item(b) * intNucDist) / (basis_1.item(c) + basis_2.item(b)))
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_1.item(d), basis_1.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d) * normMatrix.item(c,b1)
							
						else:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = 0
							rCD = intNucDist
							rPQ = (intNucDist) - (basis_2.item(d) * intNucDist) / (basis_1.item(c) + basis_2.item(d))
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_2.item(b), basis_1.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b1) * normMatrix.item(c,d1)
							rAB = 0
							rCD = intNucDist
							rPQ = (intNucDist) - (basis_2.item(b) * intNucDist) / (basis_1.item(c) + basis_2.item(b))
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_2.item(d), basis_1.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d1) * normMatrix.item(c,b1)
					else:
						if it2.multi_index[1] < basis_1.shape[1]:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1]
							rAB = 0
							rCD = intNucDist
							rPQ = (intNucDist) - (basis_2.item(c) * intNucDist) / (basis_1.item(d) + basis_2.item(c))
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_2.item(b), basis_2.item(c), basis_1.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b1) * normMatrix.item(c1,d)
							rAB = intNucDist
							rCD = 0
							rPQ = ((basis_2.item(a) * intNucDist) / (basis_2.item(a) + basis_1.item(d))) - intNucDist
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_1.item(d), basis_2.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d) * normMatrix.item(c1,b1)
						else:
							a = it1.multi_index[0] % basis_1.shape[1]
							a1 = it1.multi_index[0]
							b = it1.multi_index[1] % basis_1.shape[1]
							b1 = it1.multi_index[1]
							c = it2.multi_index[0] % basis_1.shape[1]
							c1 = it2.multi_index[0]
							d = it2.multi_index[1] % basis_1.shape[1]
							d1 = it2.multi_index[1]
							rAB = 0
							rCD = 0
							rPQ = 0
							repulsion1 = repulsionCalculation(basis_2.item(a), basis_2.item(b), basis_2.item(c), basis_2.item(d), rAB, rCD, rPQ) * normMatrix.item(a1,b1) * normMatrix.item(c1,d1)
							repulsion2 = repulsionCalculation(basis_2.item(a), basis_2.item(d), basis_2.item(c), basis_2.item(b), rAB, rCD, rPQ) * normMatrix.item(a1,d1) * normMatrix.item(c1,b1)
		
			cellValue += it2[0] * (repulsion1 - .5 * repulsion2)
			it2.iternext()

		gMatrix[it1.multi_index[0]][it1.multi_index[1]] = cellValue
		it1.iternext()
	return gMatrix

#A function to generate an SCF 
def SCFLoop(basis_1, basis_2, intNucDist, nucCharge1, nucCharge2, numElectrons):
	norm = normalizeMatrix(normalizeBasisSet(basis_1), normalizeBasisSet(basis_2))
	overlap = np.multiply(overlapMatrix(basis_1, basis_2, intNucDist), norm)
	coreHam = np.multiply(coreHamiltonian(basis_1, basis_2, intNucDist, nucCharge1, nucCharge2), norm)
	fock = coreHam
	oMatrix = orthonormalizationMatrix(overlap)
	cMatrix = coeffMatrix(oMatrix, fock)
	dMatrix1 = densityMatrix(cMatrix, numElectrons)
	gMatrix = twoElectronFock(dMatrix1, basis_1, basis_2, intNucDist, norm)
	converge = False
	numLoops = 0
	while not converge: #Should be until consistent field
		fock = coreHam + gMatrix
		cMatrix = coeffMatrix(oMatrix, fock)
		dMatrix2 = densityMatrix(cMatrix, numElectrons)
		if (np.sum(np.subtract(dMatrix1, dMatrix2)) <= 0):
			converge = True
		gMatrix = twoElectronFock(dMatrix2, basis_1, basis_2, intNucDist, norm)
		dMatrix1 = dMatrix2
		numLoops += 1
		print numLoops
	energy = 0.5 * np.sum(np.multiply(dMatrix1, (coreHam + coreHam + gMatrix)))
	
	print "Electronic Energy"
	print energy
	
	print "Total Energy"
	print energy + (nucCharge1 * nucCharge2) / intNucDist
	
def test():
	print "This is a test:\n"
	norm = normalizeMatrix(normalizeBasisSet(He_alpha_params), normalizeBasisSet(He_alpha_params))
	overlap = overlapMatrix(He_alpha_params, He_alpha_params, He_intNucDist)
	kinetic = kineticEnergy(He_alpha_params, He_alpha_params, He_intNucDist)
	attract1 = potentialNucEnergy(He_alpha_params, He_alpha_params, He_intNucDist, 2, False)
	attract2 = potentialNucEnergy(He_alpha_params, He_alpha_params, He_intNucDist, 2, True)
	print "Core Hamiltonian:"
	core = coreHamiltonian(He_alpha_params, He_alpha_params, He_intNucDist, 2, 2)
	print np.multiply(core, norm)
	print "\n"
	print "\n"
	print "OrthonormMatrix"
	oMatrix = orthonormalizationMatrix(np.multiply(overlap, norm))
	print oMatrix
	print "\n"
	print "Density Matrix:"
	cMatrix = coeffMatrix(oMatrix, core)
	dMatrix = densityMatrix(cMatrix, 4)
	print dMatrix
	print "\n"
	print "Coeffecient Matrix:"
	print cMatrix
	print "\n"
	print "G Matrix"
	gMatrix = twoElectronFock(dMatrix, eeRepulsionMatrix)
	print gMatrix
	print "\n"
	
	
SCFLoop(He_alpha_params, He_alpha_params, He_intNucDist, 2, 2, 4)
#test()
