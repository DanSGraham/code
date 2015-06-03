#A script to generate finite state bots for vindinium based on certain rules
#By DG

import random

#check all lengths in the line


"""Hero __ranks,
            gold = a
            mines = b
            life = c
            distance = d
            mine positions = m
            own hero = OH
            tavern locations = t
            """
allTargetList = ["a", "b", "c", "d", "m", "OH", "t"]

noTList = ["a", "b", "c", "d", "m", "OH"]

onlyHeroList = ["a", "b", "c", "d", "OH"]


heroOptions = [".life", ".gold", ".mines", ".mine_count", ".pos", ""]

heroNoPOptions = [".life", ".gold", ".mines", ".mine_count", ""]

diffOptions = [".life", ".gold", ".mine_count"]

distOptions = [".mines", ".pos"]

conjunctionList = [" and ", " or "]

diffOperations = [">", "<", "==", "!=", "in"]

equalsCompare = ["==", "!="]

integerCompare = [">", "<", "==", "!="]

qualifierList = ["(diff)", "(dist)", "(None)", "(atT)"]

secondQualDiff = [ "(diff)", "(None)"]

secondQualDist = ["(dist)", "(None)"]

secondQualDiffDist = ["(diff)", "(dist)", "(None)"]

lifeDiffOptions = [str(n) for n in range(-95, 96, 10)]
lifeOptions = [str(n) for n in range(0, 96, 10)]

distanceDiffOptions = [str(n) for n in range(-10, 11, 1)]
distanceOptions = [str(n) for n in range(0, 11, 1)]

goldDiffOptions = [str(n) for n in range(-200, 201, 10)]
goldOptions = [str(n) for n in range(0, 1000, 100)]

mineCountDiffOptions = [str(n) for n in range(-4, 5, 1)]
mineCountOptions = [str(n) for n in range(0, 5, 1)]

conditionalString = ""
numConditionalsPerLine = 1

possibleGoalList = []



def noneQualBuilder():
    qual = "(None)"
    mine_num = ""
    target = ""
    compare = ""
    focus = ""
    focus1 = ""
    focus2 = ""
    secondQual = ""
    tOption = ""
    fOption = ""
    extra = ""
    target = random.choice(noTList)

    #handles if a mine is chosen   
    if target == "m":
        mine_num = random.randint(0, 3)
        target = "(" + str(mine_num) + "<len(" + target + ")) and " + target
        target += "[" + str(mine_num) + "]"
        compare = " in "
        focus = random.choice(onlyHeroList)
        if focus != "OH":
            if focus == "d":
                focus += "[" + str(random.randint(0,2)) + "]"
            else:
                focus += "[" + str(random.randint(0,3)) + "]"
        focus += ".mines"
    #Handles if a hero is chosen
    else:
        if target != "OH":
            if target == "d":
                    target += "[" + str(random.randint(0,2)) + "]"
            else:
                target += "[" + str(random.randint(0,3)) + "]"
        tOption = random.choice(heroNoPOptions)
        #Handles if hero.mines is chosen
        while tOption == ".mines":
            tOption = random.choice(heroNoPOptions)
##            #Has an extra method to iterate through the hero mines to check if the mine is in m
##            extra = "_fa_"
##            compare = " in "
##            focus = "m"
##            #m[i] is the mine that is in the hero list
##            possibleGoalList.append("m[i]")    #NEED TO HANDLE THIS SOMEHOW

        #Handles if hero is chosen
        if tOption == "":
            compare = random.choice(equalsCompare)
            focus = target
            while focus == target and focus[0] == target[0]:
                focus = random.choice(onlyHeroList)
                if focus != "OH":
                    if focus == "d":
                        focus += "[" + str(random.randint(0,2)) + "]"
                    else:
                        focus += "[" + str(random.randint(0,3)) + "]"

        #handles if hero.mine_count, hero.gold, hero.life is chosen            
        else:
            compare = random.choice(integerCompare)
            secondQual = random.choice(secondQualDiff)
            #Allows for multiple after comparison operations, diff and none
            if secondQual == "(None)":
                if tOption == ".life":
                    focus = random.choice(onlyHeroList + lifeOptions)
                if tOption == ".gold":
                    focus = random.choice(onlyHeroList + goldOptions)
                if tOption == ".mine_count":
                    focus = random.choice(onlyHeroList + mineCountOptions)
                    
                if focus in onlyHeroList:
                    focus = target
                    while focus == target:
                        focus = random.choice(onlyHeroList)
                        if focus != "OH":
                            if focus == "d":
                                focus += "[" + str(random.randint(0,2)) + "]"
                            else:
                                focus += "[" + str(random.randint(0,3)) + "]"
                    focus += tOption


            #Allows for the other side to have a difference operation
            elif secondQual == "(diff)":
                if tOption == ".life":
                    focus1 = random.choice(onlyHeroList)
                    focus2 = random.choice(onlyHeroList + lifeOptions)
                if tOption == ".gold":
                    focus1 = random.choice(onlyHeroList)
                    focus2 = random.choice(onlyHeroList + goldOptions)
                if tOption == ".mine_count":
                    focus1 = random.choice(onlyHeroList)
                    focus2 = random.choice(onlyHeroList + mineCountOptions)
                    
                if focus1 in onlyHeroList:
                    focus1 = target
                    while focus1 == target:
                        focus1 = random.choice(onlyHeroList)
                        if focus1 != "OH":
                            if focus1 == "d":
                                focus1 += "[" + str(random.randint(0,2)) + "]"
                            else:
                                focus1 += "[" + str(random.randint(0,3)) + "]"
                    focus1 += tOption

                if focus2 in onlyHeroList:
                    focus2 = focus1
                    while focus2 == focus1:
                        focus2 = random.choice(onlyHeroList)
                        if focus2 != "OH":
                            if focus2 == "d":
                                focus2 += "[" + str(random.randint(0,2)) + "]"
                            else:
                                focus2 += "[" + str(random.randint(0,3)) + "]"
                    focus2 += tOption
    
    #convert into eval ready form

    qual = ""
    if secondQual == "(None)":
        secondQual = ""
    if secondQual == "(diff)":
        secondQual = "-"
    stringToReturn = "(" + qual + target + tOption + extra + compare + "(" + focus
    if secondQual != "":
        stringToReturn += focus1 + secondQual + focus2 
    stringToReturn += "))"
    return stringToReturn
                

def distQualBuilder():
    #Accounts for the distance quality
    #Not done yet. Could also check distances to other hero mines
    qual = "(dist)"
    mine_num = ""
    target1 = ""
    target2 = ""
    compare = ""
    focus = ""
    focus1 = ""
    focus2 = ""
    secondQual = ""
    tOption1 = ""
    tOption2 = ""
    lenT1 = ""
    lenT2 = ""
    lenF1 = ""
    lenF2 = ""
    fOption1 = ""
    fOption12= ""
    fOption = ""
    extra = ""
    target1 = random.choice(allTargetList)

    if target1 in onlyHeroList:
        tOption1 = ".pos"
    if target1 != "OH":
        if target1 == "d":
            target1 += "[" + str(random.randint(0,2)) + "]"
        elif target1 == "m" or target1 == "t":
            randNum = random.randint(0,3)
            lenT1 = "(" + str(randNum) + "<len(" + target1 + ")) and "
            target1 += "[" + str(randNum) + "]"
        else:
            target1 += "[" + str(random.randint(0,3)) + "]"
            
    target2 = target1
    while target2 == target1:
        target2 = random.choice(allTargetList)
        if target2 in onlyHeroList:
            tOption2 = ".pos"
        else:
            tOption2 = ""
        lenT2 = ""    
        if target2 != "OH":
            if target2 == "d":
                target2 += "[" + str(random.randint(0,2)) + "]"
            elif target2 == "m" or target2 == "t":
                randNum = random.randint(0,3)
                lenT2 = "(" + str(randNum) + "<len(" + target2 + ")) and "
                target2 += "[" + str(randNum) + "]"
            else:
                target2 += "[" + str(random.randint(0,3)) + "]"
                
    compare = random.choice(integerCompare)
    secondQual = random.choice(secondQualDist)
    if secondQual == "(None)":
        focus1 = random.choice(distanceOptions)

    if secondQual == "(dist)":
        focus1 = random.choice(allTargetList)
        if focus1 in onlyHeroList:
            fOption1 = ".pos"
        if focus1 != "OH":
            if focus1 == "d":
                focus1 += "[" + str(random.randint(0,2)) + "]"
            elif focus1 == "m" or focus1 == "t":
                randNum = random.randint(0,3)
                lenF1 = "(" + str(randNum) + "<len(" + focus1 + ")) and "
                focus1 += "[" + str(randNum) + "]"
            else:
                focus1 += "[" + str(random.randint(0,3)) + "]"
            
        focus2 = focus1
        while focus2 == focus1:
            focus2 = random.choice(allTargetList)
            if focus2 in onlyHeroList:
                fOption2 = ".pos"
            else:
                fOption2 = ""
            lenF2 = ""    
            if focus2 != "OH":
                if focus2 == "d":
                    focus2 += "[" + str(random.randint(0,2)) + "]"
                elif focus2 == "m" or focus2 == "t":
                    randNum = random.randint(0,3)
                    lenF2 = "(" + str(randNum) + "<len(" + focus2 + ")) and "
                    focus2 += "[" + str(randNum) + "]"
                else:
                    focus2 += "[" + str(random.randint(0,3)) + "]"


    #convert string characteristics into eval ready
    qual = "self.pathDistanceTo("
    if secondQual == "(None)":
        secondQual = ""
    if secondQual == "(dist)":
        secondQual = "self.pathDistanceTo("
    stringToReturn = "(" + lenT1 + lenT2 + lenF1 + lenF2 + "(" + qual +target1 + tOption1 + "," + target2 + tOption2 + ")" + compare + secondQual + focus1 + fOption1
    if secondQual != "":
        stringToReturn += "," + focus2 + fOption2 + ")"
    stringToReturn += "))"
    return stringToReturn

def diffQualBuilder():
    qual = "(diff)"
    mine_num = ""
    target1 = ""
    target2 = ""
    target3 = ""
    target4 = ""
    compare = ""
    focus = ""
    focus1 = ""
    focus2 = ""
    focus3 = ""
    focus4 = ""
    lenT1 = ""
    lenT2 = ""
    lenT3 = ""
    lenT4 = ""
    lenF1 = ""
    lenF2 = ""
    lenF3 = ""
    lenF4 = ""
    
    secondQual = ""
    thirdQual = ""
    fourthQual = ""
    fifthQual = ""
    sixthQual = ""
    tOption1 = ""
    tOption2 = ""
    tOption3 = ""
    tOption4 = ""
    fOption1 = ""
    fOption2 = ""
    fOption3 = ""
    fOption4 = ""
    extra = ""
    secondQual = random.choice(secondQualDist)
    if secondQual == "(dist)":
        thirdQual = secondQual
        target1 = random.choice(allTargetList)
        if target1 in onlyHeroList:
            tOption1 = ".pos"
        if target1 != "OH":
            if target1 == "d":
                target1 += "[" + str(random.randint(0,2)) + "]"
            elif target1 == "m" or target1 == "t":
                randNum = random.randint(0,3)
                lenT1 = "(" + str(randNum) + "<len(" + target1 + ")) and "
                target1 += "[" + str(randNum) + "]"
            else:
                target1 += "[" + str(random.randint(0,3)) + "]"
                
        target2 = target1
        while target2 == target1:
            target2 = random.choice(allTargetList)
            if target2 in onlyHeroList:
                tOption2 = ".pos"
            else:
                tOption2 = ""
            lenT2 = ""    
            if target2 != "OH":
                if target2 == "d":
                    target2 += "[" + str(random.randint(0,2)) + "]"
                elif target2 == "m" or target2 == "t":
                    randNum = random.randint(0,3)
                    lenT2 = "(" + str(randNum) + "<len(" + target2 + ")) and "
                    target2 += "[" + str(randNum) + "]"
                else:
                    target2 += "[" + str(random.randint(0,3)) + "]"

        target3 = random.choice(allTargetList)
        if target3 in onlyHeroList:
            tOption3 = ".pos"
        if target3 != "OH":
            if target3 == "d":
                target3 += "[" + str(random.randint(0,2)) + "]"
            elif target3 == "m" or target3 == "t":
                randNum = random.randint(0,3)
                lenT3 = "(" + str(randNum) + "<len(" + target3 + ")) and "
                target3 += "[" + str(randNum) + "]"
            else:
                target3 += "[" + str(random.randint(0,3)) + "]"
                
        target4 = target3
        while target4 == target3:
            target4 = random.choice(allTargetList)
            if target4 in onlyHeroList:
                tOption4 = ".pos"
            else:
                tOption4 = ""
            lenT4 = ""    
            if target4 != "OH":
                if target4 == "d":
                    target4 += "[" + str(random.randint(0,2)) + "]"
                elif target4 == "m" or target4 == "t":
                    randNum = random.randint(0,3)
                    lenT4 = "(" + str(randNum) + "<len(" + target4 + ")) and "
                    target4 += "[" + str(randNum) + "]"
                else:
                    target4 += "[" + str(random.randint(0,3)) + "]"
    else:
        target1 = random.choice(onlyHeroList)
        tOption1 = random.choice(diffOptions)
        if target1 != "OH":
            if target1 == "d":
                target1 += "[" + str(random.randint(0,2)) + "]"
            else:
                target1 += "[" + str(random.randint(0,3)) + "]"
        
        if tOption1 == ".life":
            target3 = random.choice(onlyHeroList + lifeOptions)
        if tOption1 == ".gold":
            target3 = random.choice(onlyHeroList + goldOptions)
        if tOption1 == ".mine_count":
            target3 = random.choice(onlyHeroList + mineCountOptions)
         
        
        if target3 in onlyHeroList:
            target3 = target1
            tOption3 = tOption1
            while target3 == target1:
                target3 = random.choice(onlyHeroList)
                if target3 != "OH":
                    if target3 == "d":
                        target3 += "[" + str(random.randint(0,2)) + "]"
                    else:
                        target3 += "[" + str(random.randint(0,3)) + "]"
      
    compare = random.choice(integerCompare)
    fourthQual = random.choice(secondQualDiffDist)
    if fourthQual == "(dist)" and secondQual != "(dist)":
        fourthQual = random.choice(secondQualDiff)
        
    if fourthQual == "(None)":
        if tOption1 == ".pos" or tOption1 == "":
            focus1 = random.choice(distanceOptions)

        if tOption1 == ".life":
            focus1 = random.choice(onlyHeroList + lifeOptions)
    
        if tOption1 == ".gold":
            focus1 = random.choice(onlyHeroList + goldOptions)

        if tOption1 == ".mine_count":
            focus1 = random.choice(onlyHeroList + mineCountOptions)

        if focus1 in onlyHeroList:
            fOption1 = tOption1
            if focus1 != "OH":
                if focus1 == "d":
                    focus1 += "[" + str(random.randint(0,2)) + "]"
                else:
                    focus1 += "[" + str(random.randint(0,3)) + "]"
            
    if fourthQual == "(dist)":
        focus1 = random.choice(allTargetList)
        if focus1 in onlyHeroList:
            fOption1 = ".pos"
        if focus1 != "OH":
            if focus1 == "d":
                focus1 += "[" + str(random.randint(0,2)) + "]"
            elif focus1 == "m" or focus1 == "t":
                randNum = random.randint(0,3)
                lenF1 = "(" + str(randNum) + "<len(" + focus1 + ")) and "
                focus1 += "[" + str(randNum) + "]"
            else:
                focus1 += "[" + str(random.randint(0,3)) + "]"
                
        focus2 = focus1
        while focus2 == focus1:
            focus2 = random.choice(allTargetList)
            if focus2 in onlyHeroList:
                fOption2 = ".pos"
            else:
                fOption2 = ""
            lenF2 = ""    
            if focus2 != "OH":
                if focus2 == "d":
                    focus2 += "[" + str(random.randint(0,2)) + "]"
                elif focus2 == "m" or focus2 == "t":
                    randNum = random.randint(0,3)
                    lenF2 = "(" + str(randNum) + "<len(" + focus2 + ")) and "
                    focus2 += "[" + str(randNum) + "]"
                else:
                    focus2 += "[" + str(random.randint(0,3)) + "]"

    if fourthQual == "(diff)":
        #Difference of the same thing measured in the opening:
        focus1 = random.choice(onlyHeroList)
        fOption1 = tOption1
        if focus1 != "OH":
            if focus1 == "d":
                focus1 += "[" + str(random.randint(0,2)) + "]"
            else:
                focus1 += "[" + str(random.randint(0,3)) + "]"
        
        if tOption1 == ".life":
            focus3 = random.choice(onlyHeroList + lifeOptions)
        if tOption1 == ".gold":
            focus3 = random.choice(onlyHeroList + goldOptions)
        if tOption1 == ".mine_count":
            focus3 = random.choice(onlyHeroList + mineCountOptions)
         
        
        if focus3 in onlyHeroList:
            focus3 = focus1
            fOption3 = tOption1
            while focus3 == focus1:
                focus3 = random.choice(onlyHeroList)
                if focus3 != "OH":
                    if focus3 == "d":
                        focus3 += "[" + str(random.randint(0,2)) + "]"
                    else:
                        focus3 += "[" + str(random.randint(0,3)) + "]"
                        
        #Handles if the distances are being differenced in the first part
        if secondQual == "(dist)":
            fifthQual = "(dist)"
            if fifthQual == "(dist)":
                focus1 = random.choice(allTargetList)
                if focus1 in onlyHeroList:
                    fOption1 = ".pos"
                else:
                    fOption1 = ""
                if focus1 != "OH":
                    if focus1 == "d":
                        focus1 += "[" + str(random.randint(0,2)) + "]"
                    elif focus1 == "m" or focus1 == "t":
                        randNum = random.randint(0,3)
                        lenF1 = "(" + str(randNum) + "<len(" + focus1 + ")) and "
                        focus1 += "[" + str(randNum) + "]"
                    else:
                        focus1 += "[" + str(random.randint(0,3)) + "]"
                        
                focus2 = focus1
                while focus2 == focus1:
                    focus2 = random.choice(allTargetList)
                    if focus2 in onlyHeroList:
                        fOption2 = ".pos"
                    else:
                        fOption2 = ""
                    lenF2 = ""
                    if focus2 != "OH":
                        if focus2 == "d":
                            focus2 += "[" + str(random.randint(0,2)) + "]"
                        elif focus2 == "m" or focus2 == "t":
                            randNum = random.randint(0,3)
                            lenF2 = "(" + str(randNum) + "<len(" + focus2 + ")) and "
                            focus2 += "[" + str(randNum) + "]"
                        else:
                            focus2 += "[" + str(random.randint(0,3)) + "]"

            sixthQual = random.choice(secondQualDist)
            if sixthQual == "(dist)":
                focus3 = random.choice(allTargetList)
                if focus3 in onlyHeroList:
                    fOption3 = ".pos"
                else:
                    fOption3 = ""
                if focus3 != "OH":
                    if focus3 == "d":
                        focus3 += "[" + str(random.randint(0,2)) + "]"
                    elif focus3 == "m" or focus3 == "t":
                        randNum = random.randint(0,3)
                        lenF3 = "(" + str(randNum) + "<len(" + focus3 + ")) and "
                        focus3 += "[" + str(randNum) + "]"
                    else:
                        focus3 += "[" + str(random.randint(0,3)) + "]"
                        
                focus4 = focus3
                while focus4 == focus3:
                    focus4 = random.choice(allTargetList)
                    if focus4 in onlyHeroList:
                        fOption4 = ".pos"
                    else:
                        fOption4 = ""
                    lenF4 = ""    
                    if focus4 != "OH":
                        if focus4 == "d":
                            focus4 += "[" + str(random.randint(0,2)) + "]"
                        elif focus4 == "m" or focus4 == "t":
                            randNum = random.randint(0,3)
                            lenF4 = "(" + str(randNum) + "<len(" + focus4 + ")) and "
                            focus4 += "[" + str(randNum) + "]"
                        else:
                            focus4 += "[" + str(random.randint(0,3)) + "]"

            if sixthQual == "(None)":
                focus3 = random.choice(distanceOptions)
                

    #Converts the statements into eval ready ones
    qual = "-"
    if secondQual == "(None)":
        secondQual = ""
    if secondQual == "(dist)":
        secondQual = "self.pathDistanceTo("
    if thirdQual == "(dist)":
        thirdQual = "self.pathDistanceTo("
    if thirdQual == "(None)":
        thirdQual = ""
    if fourthQual == "(None)":
        fourthQual = ""
    if fourthQual == "(diff)":
        fourthQual = "-"
    if fourthQual == "(dist)":
        fourthQual = "self.pathDistanceTo("

    if fifthQual == "(dist)":
        fifthQual = "self.pathDistanceTo("
    if fifthQual == "(None)":
        fifthQual = ""

    if sixthQual == "(dist)":
        sixthQual = "self.pathDistanceTo("
    if sixthQual == "(None)":
        sixthQual = ""
    
    stringToReturn = "((" + lenT1 + lenT2 + lenT3 + lenT4 + lenF1 + lenF2 + lenF3 + lenF4 + "(" + secondQual + target1 + tOption1 #"," + target2 + thirdQual + target3 + target4 + tOption + extra + compare + focus
    if secondQual != "":
        stringToReturn += "," + target2 + tOption2 + ")" + qual
    if thirdQual != "":
        stringToReturn += thirdQual + target3 + tOption3 + "," + target4 + tOption4 + ")"
    else:
        stringToReturn += qual + thirdQual + target3 + tOption3

    stringToReturn += ")" + compare + "("#+ fourthQual +fifthQual + focus1 + fOption1
    if fourthQual == "":
        stringToReturn += fourthQual + focus1 + fOption1 + ")))"#+ "," + focus2 + fOption2 + ")"
    elif fourthQual == "self.pathDistanceTo(":
        stringToReturn += fourthQual + focus1 + fOption1 + "," + focus2 + fOption2 + "))))"
    elif fourthQual == "-":
        if fifthQual == "self.pathDistanceTo(":
            stringToReturn += fifthQual + focus1 + fOption1 + "," + focus2 + fOption2 + ")" + fourthQual
            if sixthQual == "self.pathDistanceTo(":
                stringToReturn += sixthQual + focus3 + fOption3 + "," + focus4 + fOption4 + "))))"
            elif sixthQual == "":
                stringToReturn += focus3 + fOption3 + ")))"
        elif fifthQual == "":
            stringToReturn += focus1 + fOption1 + fourthQual
            if sixthQual == "self.pathDistanceTo(":
                stringToReturn += sixthQual + focus3 + fOption3 + "," + focus4 + fOption4 + "))))"
            elif sixthQual == "":
                stringToReturn += focus3 + fOption3 + ")))"

    return stringToReturn
    #Need to work out the parenthesis logic here    
    
def atTQualBuilder():
    notOrNot = ["not ", ""]
    qual = "self.heroAtTavern("
    target1 = ""
    target1 = random.choice(onlyHeroList)
    if target1 != "OH":
        if target1 == "d":
            target1 += "[" + str(random.randint(0,2)) + "]"
        else:
            target1 += "[" + str(random.randint(0,3)) + "]"
            
    stringToReturn = random.choice(notOrNot) + qual + target1 + ")"
    return stringToReturn    


def actionBuilder():
    #here i could have it go to a mine in the other hero list but that is a later feature
    actionTarget = random.choice(allTargetList)

    returnListOrTuple = random.randint(0,1)
    if actionTarget != "OH":
        if actionTarget == "d":
            actionTarget += "[" + str(random.randint(0,2)) + "].pos"
        else:
            if actionTarget in onlyHeroList:
                actionTarget += "[" + str(random.randint(0,3)) + "].pos"
            else:
                if returnListOrTuple == 1:
                    actionTarget += "[" + str(random.randint(0,3)) + "]"
        #one option could be ".mines" and go to the mine in that list. For later.
    if actionTarget == "OH":
        actionTarget += ".pos"
    return actionTarget

#Qualifiers done. Now I need to build the then part of statements, and build whole phrases.

def makeNewLine(numPStatementsLine):
    numQualPerStatement = random.randint(1,numPStatementsLine)
    statement = "("
    for j in range(numQualPerStatement):
        if j != 0:
            statement += random.choice(conjunctionList)
        sQual = random.choice(qualifierList)
        if sQual == "(None)":
            statement += noneQualBuilder()
        if sQual == "(dist)":
            statement += distQualBuilder()
        if sQual == "(diff)":
            statement += diffQualBuilder()
        if sQual == "(atT)":
            statement += atTQualBuilder()

    statement += "):" + actionBuilder()
    return statement

def makeNewBot(numPLines, numPStatementsLine):
    
    numStatements = random.randint(1,numPLines)
    fullStatement = ""
    for i in range(numStatements):
        
        numQualPerStatement = random.randint(1,numPStatementsLine)
        statement = "("
        for j in range(numQualPerStatement):
            if j != 0:
                statement += random.choice(conjunctionList)
            sQual = random.choice(qualifierList)
            if sQual == "(None)":
                statement += noneQualBuilder()
            if sQual == "(dist)":
                statement += distQualBuilder()
            if sQual == "(diff)":
                statement += diffQualBuilder()
            if sQual == "(atT)":
                statement += atTQualBuilder()

        statement += "):" + actionBuilder() + "\n"
        fullStatement += statement
    #Add the wins and total games at end    
    fullStatement += "True:" + actionBuilder() + "@0.0/0.0\n\n" #Accounts for else condition
    return fullStatement
        
