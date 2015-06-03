from duelgame import *

def new_unforgivable(self):
    self.textWidget.setText(random.choice(['"I will not curse!"', '"I will behave!"', '"I\'m sorry!"']))
    return "FaceF"


def screen(winners):
    if not hasattr(winners[0],'jailed') and winners[0].getName() == 'Brent':
        takeAway(winners[0])
        return False
    return True
    
def takeAway(criminal):
    win = GraphWin("Wizard Duel: Cut Scene", 80*WORLD_WIDTH, 80*WORLD_HEIGHT)
    win.setCoords(-0.5,-0.5,WORLD_WIDTH-0.5,WORLD_HEIGHT-0.5)
    grass = Image(Point(WORLD_WIDTH/2,WORLD_HEIGHT/2),"grass_big.gif")
    grass.draw(win)

    world = World(win)
    
    wiz = criminal
    startX,startY = (6,5)
    startFacing = random.choice(['N','E','S','W'])
    imgFile ="wizard_penguin3.gif"
    wiz.setupInWorld(imgFile,startX,startY,startFacing,world)
    world.addWizard(wiz)       
    wiz.draw(win)

    startMessage = DisplayMessage("Oh no!\n\n One of the wizards has broken \n the dueling rules, and \n used an unforgivable curse!")
    startMessage.draw(win)
    time.sleep(6)
    startMessage.setText("Thankfully, the special spells surrounding \n the dueling arena prevent true death \n by the killing curse.")
    time.sleep(6)
    startMessage.setText("But what should be done with this criminal?")
    time.sleep(6)
    startMessage.undraw()
   
    dementor = Image(Point(1,4),"dementor.gif")
    dementor.draw(win)
    dementorTxt = Text(Point(1,2),"Dementor from Azkaban")
    dementorTxt.setTextColor('white')
    dementorTxt.setSize(14)
    dementorTxt.draw(win)
    for i in range(260):
        dementor.move(0.01,0)
        dementorTxt.move(0.01,0)
        time.sleep(0.01)
    
    dementorTxt.setText('"Imperio!"')
    time.sleep(2)
    criminal.undraw()
    criminal.image = Image(Point(criminal.getX(),criminal.getY()),"wizard_jailed.gif")
    criminal.draw(win)
    criminal.jailed = True
    criminal.__class__.unforgivable = new_unforgivable
    time.sleep(3)
    dementorTxt.setText('"My work is done."')  
    dementor.undraw()
    dementor.draw(win)
    dementorTxt.undraw()
    dementorTxt.draw(win)
    for i in range(250):
        dementor.move(0.03,0)
        dementorTxt.move(0.03,0)
        time.sleep(0.01)
    
    startMessage.setText("Now, on with the match!")
    startMessage.draw(win)
    time.sleep(3)
    startMessage.undraw()
    #win.getMouse()
    time.sleep(2)
    win.close()

