# Debugging coin toss.py
# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 10 Project

"""Debug Coin Toss Program, main bug resulted from comparison between different data types"""

import random

guess = ''
outcomes = ['heads', 'tails']
while guess.lower() not in outcomes:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.choice(outcomes)  # Randomly choose heads or tails
if toss == guess.lower():
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess.lower():
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
