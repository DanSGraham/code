#
#A program for a guessing game
# By Daniel Graham
import random
def guessing_game():
    num_guess = 1    #sets up the accumulator for number of guesses
    target = random.randrange(1,100)  #generates the number to guess
    guess = input("Please enter your first guess: ")   #collects user input
    while guess != target:   #while loop continues the game until the user inputs the same value as the target.
        if guess > target:               #These four lines tell the user if they are above or below the target value.
            print "Your guess was high. Try again."
        if guess < target:
            print "Your guess was low. Try again."
        num_guess = num_guess + 1          #Adds number of attempts
        print 
        guess = input("Please enter your guess: ")
    print "Congratulations! You guessed correctly!"      #Last lines congratulate the user on a successful guess.
    print "It only took you", num_guess, "trys."
guessing_game()
        
