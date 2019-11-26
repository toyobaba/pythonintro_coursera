# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else: 
        return "Number matches no name"

    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 100


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # compute difference of player_number and comp_number modulo five           
    numb_difference = (player_number - comp_number)% 5

    # use if/elif/else to determine winner
    if player_number > 4:
        result = "Player entered invalid name\r\n"
    elif numb_difference == 3 or numb_difference == 4:
        result = "Computer wins!\r\n"
    elif numb_difference == 1 or numb_difference == 2:
        result = "Player wins!\r\n"
    elif numb_difference == 0:
        result = "Player and Computer tie!\r\n"
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    
    # print results
    print "Player chooses", name
    print "Computer chooses", comp_name
    print result

    
# test your code
# test with invalid entry to make sure it catches this
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("Garbage")

# always remember to check your completed program against the grading rubric



