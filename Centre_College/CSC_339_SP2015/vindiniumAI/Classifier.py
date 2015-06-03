#!/usr/bin/python
import game
#import findMaxEarningHeroPosition1 as ai
import ai
import json
import random
import time
from pybrain.datasets    import ClassificationDataSet





def loadBrain(data):
    # #read in file
    # fin = open(filename)
    # data = fin.read()
    # fin.close()
    #print data
    
    #read in as python description!!
    state = eval(data)#json.loads(data)
    #print json.dumps(state,sort_keys=True, indent=4,separators=(',',': '))

    #create game object
    g = game.Game(state)
    #feed it to AI
    brain = ai.AI()
    brain.process(g)

    #brain.printMap()
    return brain


def generateDataSet():

    inFile = open("data/input.txt")
    inData = inFile.readlines()
    inFile.close()
    
    outFile = open("data/output.txt")
    outData = outFile.readlines()
    outFile.close()


    inputs = 120 #you will want to update this based on the state you have... ###I don't understand this comment. How do we update if we haven't calculated the state yet?
    classes= 11 #11 #Not much reson to change this one, there are only 11 destinations.
    allData = ClassificationDataSet(inputs,1,nb_classes=classes)
    start = time.clock()
    for i in range(len(inData)):
        b = loadBrain(inData[i].strip())
        #inputs = len(b.g.heroes) - 1 + len(b.g.taverns_locs) + 4
        #calls functions inside of the ai object.  you will want to write these fcns. 
        ins = b.createInputs(inputs)
        klass = b.determineClass(classes,eval(outData[i].strip()))
        expectedKlass = b.classInverse(klass)
        #if expectedKlass != eval(outData[i].strip()):
        #    print expectedKlass, eval(outData[i].strip())
        allData.addSample(ins,[klass])
        #if(i > 1000): break
        if(i%100==0): print i,len(inData), "elapsed between sets", time.clock() - start
    
    return allData    

    
def main():    
    start = time.clock()
    dataset = generateDataSet()
    dataset.saveToFile("ClassifierDataSet")
    print "elapsed",time.clock()-start


    
main()
