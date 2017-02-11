#A program to determine the best "bread basket" trading strategy.
#By Daniel Graham



#Independent Variables
#Length of trading period
#Amount of time before dropping
#How many days it had been increasing for
#Size of Basket

#Dependent Variables
#Lowest amount
#Peak amount
#worst day
#Best day
#S& P for the same time period
#Ending amount


import random


class Stock:
    pass
    #holds all stock price info.


class Basket:

    def __init__(self, numSuccessDays, daysUntilDrop, sizeOfBasket):
        
        self.daysToBuildRep = numSuccessDays
        self.daysToDrop = daysUntilDrop
        self.basketSize = sizeOfBasket
        self.basketContents = []

    def addToBasket(self, stockList):
        #While the basket is not full, add a random stock that meets the daysToBuildRep requirement.

        counterToAvoidLoop = 0
        while len(self.basketContents) < self.basketSize:
            counterToAvoidLoop += 1
            if counterToAvoidLoop >= 1000:
                print "INFINITE LOOP IN ADDITION TO BASKET"
                break

            poStock = random.choice(stockList)

            #Prevent multiple additions of same stock
            while poStock in self.basketContents:
                poStock = random.choice(stockList)
                
            meetQual = True
            for i in range(self.daysToBuildRep):
                if poStock.endPrice[i + 1] > poStock.endPrice[i]:
                    meetQual = False
                    break

            if meetQual:
                self.basketContents.append(poStock)
