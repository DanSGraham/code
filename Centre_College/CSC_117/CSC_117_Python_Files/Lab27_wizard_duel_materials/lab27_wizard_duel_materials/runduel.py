import duelgame
from randomwizard import RandomWizard
from scaredywizard import ScaredyWizard
from DanielGraham_wizard3 import DanielGrahamWizard
from DanielGraham_wizard4 import DanielGrahamWizard1


def main():
    wiz1 = RandomWizard()
    wiz2 = ScaredyWizard()
    wiz3 = DanielGrahamWizard1()
    wiz4 = DanielGrahamWizard()
    
    wizards = [wiz1, wiz2, wiz3, wiz4]  #include wiz4?
    
    duelgame.DELAY_FACTOR = 1    #larger=slower, smaller=faster
    numRounds = 80  # you can change the max number of rounds
    return duelgame.doFullDuel(wizards,numRounds) 
   
if __name__ == '__main__':
    win_count = 0
    new_win_count = 0
    for j in range(250):
        winner = main()
        for name in winner:
            if name.getHouse() == 'Slytherin123':
                win_count += 1
            if name.getHouse() == 'Slytherin':
                new_win_count +=1
    print " 3.0 lived through:",win_count
    print "4.0 lived through:", new_win_count
        
    
    
