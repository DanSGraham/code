#
#A program for a guessing game
# By Daniel Graham
import random
from graphics import *
def guessing_game():
    win = GraphWin("Guessing Game", 300 ,300)
    guess_box = Entry(Point(150,80), 3) #collects user input
    guess_text = Text(Point(70, 80), "Enter guess: ")
    guess_box.draw(win)
    guess_text.draw(win)
    click_text = Text(Point(150, 40), "Click on the window after entering a guess")
    click_text.draw(win)
    num_guess = 1    #sets up the accumulator for number of guesses
    target = random.randrange(1,100)  #generates the number to guess 
    number_guess_str = "You have guessed", num_guess, "times."
    number_guess_txt = Text(Point(150,120), number_guess_str)
    win.getMouse()
    number_guess_txt.draw(win)
    guess = eval(guess_box.getText())
    while guess != target:   #while loop continues the game until the user inputs the same value as the target.
        if guess > target:               #These four lines tell the user if they are above or below the target value.
            high_text = Text(Point(150,140), "Your guess was high. Try again.")
            high_text.draw(win)
        if guess < target:
            low_text = Text(Point(150,140), "Your guess was low. Try again.")
            low_text.draw(win)
        win.getMouse()
        number_guess_txt.undraw()
        num_guess = num_guess + 1          #Adds number of attempts
        number_guess_str = "You have guessed", num_guess, "times."
        number_guess_txt = Text(Point(150,120), number_guess_str)
        number_guess_txt.draw(win)
        if guess > target:
            high_text.undraw()
        if guess < target:
            low_text.undraw()
        guess = eval(guess_box.getText())
    end_text = Text(Point (150,140), "Congratulations! You guessed correctly!" )     #Last lines congratulate the user on a successful guess.
    end_text.draw(win)
    win.getMouse()
    win.close()
guessing_game()
        
