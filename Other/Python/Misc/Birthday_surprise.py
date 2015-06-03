#
#A program to make a very special day even specialer ;)
#By THE BIG D
#Inspired by a silly graphic DNewt made in class
#For David Newton

from graphics import *
import time





def blowjob():
    bj_window = GraphWin("peanutButter Jellytime", 500,500)
    bj_head = Circle(Point(250,250), 250)
    bj_head.setFill(color_rgb(239,208,237))
    bj_eye1 = Circle(Point(175,150), 20)
    bj_eye2 = Circle(Point(325,150), 20)
    bj_eye1.setFill('black')
    bj_eye2.setFill('black')
    bj_lips = Circle(Point(250, 400), 50)
    bj_lips.setOutline('red')
    

    #nice and luscious...mmmm
    bj_lips.setWidth(15)
    bj_lips.setFill('black') #like my soul
    bj_head.draw(bj_window)
    bj_lips.draw(bj_window)
    bj_eye1.draw(bj_window)
    bj_eye2.draw(bj_window)
    for i in range(10):
        bj_window.getMouse()
    bj_window.close()


def shut_up():

    su_window = GraphWin("Fine, I will", 500,500)
    su_head = Circle(Point(250,250), 250)
    su_head.setFill(color_rgb(239,208,237))
    su_eye1 = Circle(Point(175,150), 20)
    su_eye2 = Circle(Point(325,150), 20)
    su_eye1.setFill('black')
    su_eye2.setFill('black')
    su_lips = Line(Point(200, 400), Point(300, 400))
    su_lips.setOutline('red')
    

    #nice and quiet...mmmm
    su_lips.setWidth(15) 
    su_head.draw(su_window)
    su_lips.draw(su_window)
    su_eye1.draw(su_window)
    su_eye2.draw(su_window)
    time.sleep(10)
    
    su_head.undraw()
    su_lips.undraw()
    su_eye1.undraw()
    su_eye2.undraw()
    explosion = Image(Point(250,250),'Explosion.png')
    explosion.draw(su_window)
    time.sleep(0.5)
    explosion.undraw()

    STD_TIME = Text(Point (250,250), "NAH THAT WAS LAME. \nTIME FOR A BJ!")
    STD_TIME.setSize(25)
    STD_TIME.setStyle('bold')
    STD_TIME.draw(su_window)
    
    time.sleep(3)
    
    su_window.close()
    blowjob()



##def bake_cake()
##
##
###draws a cake animation
##
##
##def stroke_snake()
##
###Draws a snake



def companion(win):
    hooker_head = Circle(Point(500,100), 75)
    hooker_head.setFill(color_rgb(239,208,237))
    hooker_lips = Oval(Point(475,150), Point(525, 160))
    hooker_lips.setFill('red')
    hooker_lips2 = Line(Point(475,155), Point(525, 155))
    
    hooker_body = Line(Point(500, 125),Point(500,600))
    hooker_rleg = Line(Point(500,600),Point(400, 800))
    hooker_lleg = Line(Point(500,600),Point(600, 800))
    hooker_arms = Line(Point(350, 300),Point(650,300))
    
    hooker_body.setWidth(3)
    hooker_rleg.setWidth(3)
    hooker_lleg.setWidth(3)
    hooker_arms.setWidth(3)
    hooker_eye1 = Circle(Point(480, 75), 10)
    hooker_eye2 = Circle(Point(520, 75), 10)
    hooker_eye1.setFill('black')
    hooker_eye2.setFill('black')

    #I heard you liked um big & juicy ;)
    
    hooker_bewbs1 = Circle(Point(530,300), 50)
    hooker_bewbs2 = Circle(Point(470,300), 50)
    hooker_bootay1 = Circle(Point(520,600), 35)
    hooker_bootay2 = Circle(Point(480,600), 35)
    hooker_bewbs1.setFill('red2')
    hooker_bewbs2.setFill('red2')
    hooker_bootay1.setFill(color_rgb(239,208,237))
    hooker_bootay2. setFill(color_rgb(239,208,237))
    hooker_bootay2.setOutline(color_rgb(239,208,237))
    hooker_bootay1.setOutline(color_rgb(239,208,237))
    
    
    hooker_arms.draw(win)
    hooker_bootay1.draw(win)
    hooker_bootay2.draw(win)
    hooker_rleg.draw(win)
    hooker_lleg.draw(win)
    hooker_body.draw(win)
    hooker_head.draw(win)
    hooker_eye1.draw(win)
    hooker_eye2.draw(win)
    hooker_lips.draw(win)
    hooker_lips2.draw(win)
    hooker_bewbs1.draw(win)
    hooker_bewbs2.draw(win)
    

def main():
    sexy_window = GraphWin("Birthday 'Friend' ;)", 1000,1000)
    sexy_introtext = Text(Point(500,900), "'Hey there big boy. Some of your Slytherin friends sent me for your birthday. \nThey also said something about you having the longest snake in the land....\nMaybe you could show me? ;)'")
    sexy_introtext.setSize(18)
    sexy_introtext.draw(sexy_window)
    companion(sexy_window)
    sexy_window.getMouse()
    sexy_introtext.undraw()
    prompt_text = Text(Point(500,900), "What do you want to do with me, butter nugget? (Put it in my shell...oh ya)")
    prompt_text.setSize(18)
    prompt_text.draw(sexy_window)
    sexy_window.getMouse()
    sexy_window.close()

    desires = raw_input("What do you want me to do for you? (Blow job, Shut up, Bake a cake, Stroke my snake) ")
    

    
                
shut_up()
    

prompt
