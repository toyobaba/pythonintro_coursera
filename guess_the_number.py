# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
secret_number = 0
player_guess = 0
ranges = 100
remain_guess = 7


# helper function to start and restart the game
def new_game():
    # remove this when you add your code
    global secret_number, ranges, remain_guess
    secret_number = random.randrange(0,ranges)
    print "New game. Range is from 0 to", ranges
    if ranges == 100:
        remain_guess = 7
    else:
        remain_guess = 10
    print "Number of remaining guesses is", remain_guess, "\r\n"
    
def restart():
    new_game()   


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global ranges, remain_guess
    ranges = 100
    new_game()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global ranges, remain_guess
    ranges = 1000
    new_game()  
    
def input_guess(guess):
    # main game logic goes here	
    global player_guess, remain_guess, secret_number
    player_guess = int(guess)
    remain_guess -=1
    print "Guesss was",player_guess
    
    if remain_guess == 0 and secret_number != player_guess:
        print "You have no more guesses"
        print "The secret number is",secret_number," You Lose!\r\n"
        new_game()
    
    elif player_guess < secret_number:
        print "Number of remaining guesses is", remain_guess
        print "Higher!\r\n"
        
    elif player_guess > secret_number:
        print "Number of remaining guesses is", remain_guess
        print "Lower!\r\n"
        
    else:
        print "Number of remaining guesses is", remain_guess
        print "This is the secret number, You Win!\r\n"
        new_game()
        

    
# create frame
f = simplegui.create_frame("Guess the number game", 300,300)


# register event handlers for control elements
f.add_button("Range 0 to 100", range100, 150)
f.add_button("Range 0 to 1000", range1000, 150)
f.add_button("Restart game", restart, 150)
f.add_input("Enter your guess", input_guess, 150)


# call new_game and start frame
new_game()
f.start()


# always remember to check your completed program against the grading rubric
