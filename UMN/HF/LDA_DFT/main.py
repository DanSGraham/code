#A program to calculate the energy of a diatomic molecule from Hartree-Fock methods
#By Daniel Graham

#TODO: Add DFT Part

import numpy as np
import math

class basis_function:

    def __init__(self, a_params, coeff, norm, position, nuclearCharge):
        self.aparams = a_params
        self.coeff = coeff
        self.norm_coeff = np.multiply(normalizeBasisSet(a_params), coeff)
        self.norm = norm
        self.position = position
        self.nuclearCharge = nuclearCharge

    def setOverallNorm(self, norm):
        self.overall_norm = norm

#Values are in angstroms
H_intNucDist = 0.74
atomicCharge = 1.
numElectrons = 2

#A function to normalize the eigenfxns
#Input: Contracted basis set alpha parameters
#Outputs: normalization_factor
def normalizeBasisSet(basisSet):
	normalization_Factors = np.copy(basisSet)
	normalization_Factors = (np.power((normalization_Factors * 2) / (math.pi), (3./4.)))
	return normalization_Factors

#A function to return the overlap matrix S of a contracted basis set.
#Inputs: 2 gaussian alpha parameter vectors, the weighting coeffecients, 
# and the internuclear distance. Norm assumed.
#Outputs: Numpy matrix of S
def overlapMatrixElement(basis_1, basis_2):
	#Equation found for formula in Modern Quantum Chemistry by Szabo eqn A.9 pg 412

        element_val = 0
        for i in range(len(basis_1.aparams)):
            for j in range(len(basis_2.aparams)):
                p = basis_1.aparams[i] + basis_2.aparams[j]
                q = (basis_1.aparams[i] * basis_2.aparams[j])/p
                coeff = (basis_1.norm_coeff[i] * basis_2.norm_coeff[j] * 
                         (math.pi / p) ** (3./2.))
	        exponent = (-q * (basis_2.position - basis_1.position) ** 2.)
                element_val += coeff * np.exp(exponent)

	return element_val

def overlapMatrix(basis_functions):
    sMatrix = np.zeros((len(basis_functions), len(basis_functions)))
    for i in range(len(basis_functions)):
        for j in range(len(basis_functions)):
            sMatrix[i][j] = overlapMatrixElement(basis_functions[i], basis_functions[j])

    #Normalize WFs
    for k in range(len(basis_functions)):
        norm = 1./np.sqrt(sMatrix[k][k])
        basis_functions[k].setOverallNorm(norm)

    for i in range(len(basis_functions)):
        for j in range(len(basis_functions)):
            sMatrix[i][j] = basis_functions[i].overall_norm * basis_functions[j].overall_norm * sMatrix[i][j]

    return sMatrix


#Returns the kinetic energy value of a matrix
#Inputs: two basis vector elements
#Outputs: The Kinetic energy element of a matrix
def kineticEnergyElement(basis_1, basis_2):

    element_val = 0
    for i in range(len(basis_1.aparams)):
        for j in range(len(basis_2.aparams)):
            p = basis_1.aparams[i] + basis_2.aparams[j]
            q = (basis_1.aparams[i] * basis_2.aparams[j])/p
            coeff = (basis_1.norm_coeff[i] * basis_2.norm_coeff[j] * 
                q * (3 - (2 * q) * (basis_2.position - basis_1.position) ** 2)
                * (math.pi/p) ** (3./2.)) 
            exponent = (-q * (basis_2.position - basis_1.position) ** (2.))
            element_val += coeff * np.exp(exponent)

    return element_val

#A function to return the kinetic energy matrix
#Inputs: Basis vectors
#Output: Kinetic Energy Matrix
def kineticEnergyMatrix(basis_functions):

    kEMatrix = np.zeros((len(basis_functions), len(basis_functions)))
    for i in range(len(basis_functions)):
        for j in range(len(basis_functions)):
            norm = basis_functions[i].overall_norm * basis_functions[j].overall_norm
            kEMatrix[i][j] = (norm * 
                kineticEnergyElement(basis_functions[i], basis_functions[j]))

    return kEMatrix
	

#A function to return the F_0 function
#Inputs: 2 basis vector elements
#Output: F_0 value
def F_0(t):
    if t == 0:
        out_val = 1
    else:
        out_val = 0.5 * (math.pi / t) ** (0.5) * math.erf(t ** 0.5)
    return out_val
    

#A function to return the interNuclear potential energy for an individual element of the matrix
#Inputs: 2 basis vector elements, 
#Output: Internuclear potential energy matrix element
def internuclearPotentialElement(basis_1, basis_2, charge, atom_position):

    element_val = 0
    for i in range(len(basis_1.aparams)):
        for j in range(len(basis_2.aparams)):
            p = basis_1.aparams[i] + basis_2.aparams[j]
            q = (basis_1.aparams[i] * basis_2.aparams[j])/p
            coeff = (basis_1.norm_coeff[i] * basis_2.norm_coeff[j] * 
                (-2. * math.pi / p) * charge)
            exponent = (-q * (basis_2.position - basis_1.position) ** (2.))

            #Something wrong after here.
            Rp = ((basis_1.aparams[i] * basis_1.position + 
                basis_2.aparams[j] * basis_2.position) / p )
            fun_0 = F_0(p * (Rp - atom_position) ** 2.)
            element_val += coeff * np.exp(exponent) * fun_0

    return element_val

#A function to return the interNuclear potential matrix
#Inputs: basis vectors
#Output: InterNuclear Potential Energy Matrix
def internuclearPotentialMatrix(basis_functions, atom):

    #This is specific to the code for two atoms and two basis sets. Not general
    basis_functions_2 = [basis_functions[:2], basis_functions[2:]]
    atom_position = basis_functions_2[atom][0].position
    atom_charge = basis_functions_2[atom][0].nuclearCharge
    iNPMatrix = np.zeros((len(basis_functions), len(basis_functions)))
    for i in range(len(basis_functions)):
        for j in range(len(basis_functions)):
            norm = basis_functions[i].overall_norm * basis_functions[j].overall_norm
            iNPMatrix[i][j] = (norm * 
                internuclearPotentialElement(basis_functions[i], basis_functions[j], atom_charge, atom_position))

    return iNPMatrix

#A function to return the core Hamiltonian matrix
#Inputs: Basis sets
#Outputs: Core Hamiltonian matrix
def coreHamiltonian(basis_functions):
	#Calculate Kinetic Energy matrix
	T_Matrix = kineticEnergyMatrix(basis_functions)
	v1_Matrix = internuclearPotentialMatrix(basis_functions, 0)
	v2_Matrix = internuclearPotentialMatrix(basis_functions, 1)
	return T_Matrix + v1_Matrix + v2_Matrix



#A helper function to determine the repulsionElement 
#Inputs: 4 basis elements
#Outputs: Repulsion energy for that element
def repulsionElement(basis_1, basis_2, basis_3, basis_4):
	#Equation found for formula in Modern Quantum Chemistry by Szabo eqn A.41 pg 416
        
        element_val = 0
        for i in range(len(basis_1.aparams)):
            for j in range(len(basis_2.aparams)):
                pAB = basis_1.aparams[i] + basis_2.aparams[j]
                qAB = (basis_1.aparams[i] * basis_2.aparams[j]) / pAB
                rAB = (basis_2.position - basis_1.position) ** 2.
                rP = (basis_1.aparams[i] * basis_1.position + basis_2.aparams[j] * basis_2.position) / pAB
                for k in range(len(basis_3.aparams)):
                    for m in range(len(basis_4.aparams)):
                        pCD = basis_3.aparams[k] + basis_4.aparams[m]
                        qCD = (basis_3.aparams[k] * basis_4.aparams[m]) / pCD
                        rCD = (basis_4.position - basis_3.position) ** 2.
                        rQ = (basis_3.aparams[k] * basis_3.position + basis_4.aparams[m] * basis_4.position) / pCD
                        coeff = (basis_1.norm_coeff[i] * basis_2.norm_coeff[j] * basis_3.norm_coeff[k] * basis_4.norm_coeff[m])
                        firstTerm = (2. * math.pi ** (5./2.)) / (pAB * pCD * (pAB + pCD) ** 0.5)
                        secondTerm = np.exp(-qAB * rAB - qCD * rCD)
                        thirdTerm = F_0(((pAB * pCD) / (pAB + pCD)) * (rP - rQ) ** 2.)
                        element_val += firstTerm * secondTerm * thirdTerm * coeff

	return element_val

#A function to determine the electron-electron repulsion
#Input: basis_set
#Output: Matrix of values
def electronElectronRepulsion(basis_set):

    eeMatrix = np.zeros((len(basis_set), len(basis_set), len(basis_set), len(basis_set)))
    for A in range(len(basis_set)):
        for B in range(len(basis_set)):
            for C in range(len(basis_set)):
                for D in range(len(basis_set)):
                    eeMatrix[A][B][C][D] = repulsionElement(basis_set[A], basis_set[B], basis_set[C], basis_set[D])

    return eeMatrix

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
	#For now assume that the 1 and 3rd orbitals are the lowest two energy, but ideal method is to have that pre determined.
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
def twoElectronFock(dMatrix, eeMatrix):
	#Szabo pg. 141 3.154
	gMatrix = np.copy(dMatrix)
	gMatrix.fill(0)
        for i in range(gMatrix.shape[0]):
            for j in range(gMatrix.shape[1]):
                #Sum part
                element_val = 0
                for m in range(dMatrix.shape[0]):
                    for n in range(dMatrix.shape[1]):
                        element_val += dMatrix[m][n] * (eeMatrix[i][j][m][n] - 0.5 * eeMatrix[i][n][j][m])

                gMatrix[i][j] = element_val
                            
	return gMatrix

#A function to generate an SCF Energy
#Inputs: basis set list
#Output: Prints energy in Hartrees
def SCFLoop(basis_sets):
        overLap = overlapMatrix(basis_sets)
        coreHam  = coreHamiltonian(basis_sets)
	fock = coreHam
	oMatrix = orthonormalizationMatrix(overLap)
	cMatrix = coeffMatrix(oMatrix, fock)
	dMatrix1 = densityMatrix(cMatrix, numElectrons)
        eeMatrix = electronElectronRepulsion(basis_sets)
	gMatrix = twoElectronFock(dMatrix1, eeMatrix)
	converge = False
	numLoops = 0
	while not converge: #Should be until consistent field
		fock = coreHam + gMatrix
		cMatrix = coeffMatrix(oMatrix, fock)
		dMatrix2 = densityMatrix(cMatrix, numElectrons)
		if (np.square(np.sum(np.subtract(dMatrix1, dMatrix2))) <= 0):
			converge = True
		gMatrix = twoElectronFock(dMatrix2, eeMatrix)
		dMatrix1 = dMatrix2
		numLoops += 1
		print numLoops
	energy = 0.5 * np.sum(np.multiply(dMatrix1, (coreHam + coreHam + gMatrix)))
	
	print "Electronic Energy"
	print energy
	
	print "Total Energy"
	print energy + (atomicCharge) / H_intNucDist

#Takes a molpro file and builds the 2 1s orbital basis
#Input: molpro filename path, distance between the two atoms of interest.
#Output: A list of basisfunction objects. These represent contracted basis sets
def buildBasisSets(filename, interNuclearDistance):
    basis_sets = []
    fin = open(filename, 'r')
    file_string = fin.read()
    file_list = file_string.split("\n")
    for i in range(len(file_list)):
        if len(file_list[i]) > 0 and file_list[i][0] == 's':
            aParams = map(float, file_list[i].split(",")[2:])
            coeff1 = map(float, file_list[i + 1].split(",")[2:])
            coeff2 = map(float, file_list[i + 2].split(",")[2:])

    norm_list = normalizeBasisSet(aParams)
    wf_1a = basis_function(aParams, coeff1, norm_list, 0, atomicCharge)
    wf_2a = basis_function(aParams, coeff2, norm_list, 0, atomicCharge)
    wf_1b = basis_function(aParams, coeff1, norm_list, interNuclearDistance, atomicCharge)
    wf_2b = basis_function(aParams, coeff2, norm_list, interNuclearDistance, atomicCharge)

    basis_sets = [wf_1a, wf_2a, wf_1b, wf_2b]
    return basis_sets
            
    
def main(BasisFile):
    basis_sets = buildBasisSets(BasisFile, H_intNucDist)
    SCFLoop(basis_sets)

	
def test():
	print "This is a test:\n"
        basis_sets = buildBasisSets("H_Basis_Set_ANO-RCC.txt", H_intNucDist)
        overLap = overlapMatrix(basis_sets)
	kinetic = kineticEnergyMatrix(basis_sets)
	attract1 = internuclearPotentialMatrix(basis_sets, 0)
        attract2 = internuclearPotentialMatrix(basis_sets, 1)
        print "Core Hamiltonian:"
        core  = coreHamiltonian(basis_sets)
        print core
	print "\n"
	print "\n"
	print "OrthonormMatrix"
	oMatrix = orthonormalizationMatrix(overLap)
	print oMatrix
	print "\n"
        print "CMATRIX"
	cMatrix = coeffMatrix(oMatrix, core)
        print "EE Matrix:"
        eeMatrix = electronElectronRepulsion(basis_sets)
        print eeMatrix
        dMatrix = densityMatrix(cMatrix, 2)
	print "Density Matrix:"
	print dMatrix
	print "\n"
	print "Coeffecient Matrix:"
	print cMatrix
	print "\n"
	print "G Matrix"
	gMatrix = twoElectronFock(dMatrix, eeMatrix)
	print gMatrix
	print "\n"
	
	
#test()

main("H_Basis_Set_ANO-RCC.txt")
