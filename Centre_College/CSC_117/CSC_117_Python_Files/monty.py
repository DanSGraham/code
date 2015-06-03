#
#The Monty Game
#By Daniel Graham

from graphics import *
from better_button import Button
import random

    

def main():
    window = GraphWin("Monty Game!", 400,400)
    welcome = Text(Point(200,200), "Welcome to the Monty Game! \n Behind one of these doors is a new car! \n Behind the others are goats... \n Good Luck!!")
    welcome.draw(window)
    winner_text = Text(Point(200,200), "Congratulations! You WON A NEW CAR!")
    loser_text = Text(Point(200,200), "Sorry you only won a goat...too BAAAAAAD")
    window.getMouse()
    welcome.undraw()
    door_1 = Button(Point(200,100),200,90, "Door 1")
    door_2 = Button(Point(200,200),200, 90, "Door 2")
    door_3 = Button(Point(200,300),200, 90, "Door 3")
    door_1.draw(window)
    door_2.draw(window)
    door_3.draw(window)
    winner = random.randrange(1,4)
    while True:
        click_point = window.getMouse()
        if (door_1.clicked(click_point) and winner == 1) or (door_2.clicked(click_point) and winner == 2)\
           or (door_3.clicked(click_point) and winner == 3):
            door_1.undraw()
            door_2.undraw()
            door_3.undraw()
            winner_text.draw(window)
            window.getMouse()
            winner_text.undraw()
            break
        elif  (door_1.clicked(click_point) and winner != 1) or (door_2.clicked(click_point) and winner != 2)\
           or (door_3.clicked(click_point) and winner != 3):

            door_1.undraw()
            door_2.undraw()
            door_3.undraw()
            loser_text.draw(window)
            window.getMouse()
            loser_text.undraw()
            break
    try_again = Text(Point(200,200), "Play Again?")
    try_again.draw(window)
    yes = Button(Point(100,300),50,50, "Yes!")
    no = Button(Point(300,300),50,50, "No")
    yes.draw(window)
    no.draw(window)
    while True:
        click_point1 = window.getMouse()
        if yes.clicked(click_point1):
            play_again = 1
            break
        elif no.clicked(click_point1):
            play_again = 0
            break
    
    window.close()
    if play_again == 1:
        main()
    
    
    
        
       
    

main()
