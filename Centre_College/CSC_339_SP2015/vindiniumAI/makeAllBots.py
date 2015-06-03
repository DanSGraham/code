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

lifeOptions = [str(n) for n in range(10, 56, 15)]

distanceOptions = [str(n) for n in range(2, 5, 1)]

mineCountOptions = [str(n) for n in range(0, 5, 1)]




def makeAllBots():
    d = 0

    #while not (b == 0 and c == 0 and d == 0 and e == 0 and f == 0 and g == 0 and h == 0 and i == 0 and k == 0):
    bot = "(((self.pathDistanceTo(OH.pos, d[0].pos) < 2) and ((d[0].life) < 21) and ((OH.mine_count - d[0].mine_count) < 0) and ((OH.life) > 22))):d[0].pos\n"
    for b in range(2):
        
        
        while d < 3:
            
            if b == 0:
                bot += "(((0 < len(m)) and ((OH == b[" + str(b) + "]) and "
                bot += "((b[0].mine_count - b[1].mine_count) > " + random.choice(mineCountOptions) + ") and "
            else:
                bot += "(((0 < len(m)) and ("
                bot += "((b[0].mine_count - b[3].mine_count) > " + random.choice(mineCountOptions) + ") and "
                       
            bot += "((self.pathDistanceTo(OH.pos, d[" + str(d) + "].pos)) < " + random.choice(distanceOptions) + ") and "
                                
            bot += "((OH.mine_count - d[" + str(d) + "].mine_count) < " + random.choice(mineCountOptions) + ") and "
        
            bot += "((OH.life - d[" + str(d) + "].life) > " + random.choice(lifeOptions) + ") and "
        
            bot += "((OH.life) > " + random.choice(lifeOptions) + ") and "
                                            
            bot += " not (self.pathDistanceTo(OH.pos, m[0]) < " + random.choice(distanceOptions) + ") and "
            bot += "not self.heroAtTavern(d[" + str(d) + "])))):d[" + str(d) + "].pos\n"
        
            d += 1

        d = 0
        bot += "(((OH.life) < 50) and (self.pathDistanceTo(d[0].pos, OH.pos) < " + random.choice(distanceOptions) + ")):t\n"
        bot += "(((OH.life) < 21)):t\n"
    bot += "True:m@0.0/0.0"
        
       
    return bot
    

