#A program to calculate the radial schrodinger for H.
#By DanG 
import matplotlib.pyplot as plt

#Calculate the EigenValues
def eigenVal(l_val):
    startE = -1.0
    endE = 0.5
    stepE = 0.01
    crossE = []
    crossR = []
    currE = startE
    while currE <= endE:
        stepR = 0.01
        startR = 2 * stepR
        endR = 20.0
        currR = startR

        un_1 = 0
        un = (stepR) ** (l_val + 1)
        grn_1 = 0
        potn = -1./stepR
        grn = 2 * ((l_val * (l_val + 1))/ (2 * (stepR ** 2.)) + (potn - currE))
        while currR <= endR:
            potn1 = -1./currR
            h = stepR ** 2. / 12.
            grn1 = 2 * ((l_val * (l_val + 1))/(2 * (currR ** 2.)) + (potn1 - currE))
            un1 = ((2*un*(1+5*grn*h)) - un_1*(1-h*grn_1))/ (1 - h * grn1)
            if (un1 <= 0):
                crossE.append(currE)
                crossR.append(currR)
                break
            grn_1 = grn
            grn = grn1
            un_1 = un
            un = un1
            currR += stepR
        currE+= stepE
    return crossR, crossE

def main():
    for L in range(3):
        rVal, eVal = eigenVal(L)
        print L
        print min(eVal)
        plt.plot(rVal, eVal)
    plt.ylabel("E")
    plt.xlabel("C")
    plt.title("Radial Schroedinger Energy for Hydrogen")
    plt.text(2.5, -.2, r'l=0')
    plt.text(8, -.09, r'l=1')
    plt.text(10, 0, r'l=2')
    plt.show()

main()
