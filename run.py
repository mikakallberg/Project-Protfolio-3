# Use limited array first to get code working
import random
from art import * 

tprint('mikaela')

randomword = ['furthermore', 'copying', 'periodic', 'mental']

# This variabel lets user initiate the game
# Credit for code structure (not a complete copy paste) to 
# Code Grepper, please see README for link.
start_game = input('Do you wish to start? Press y for yes or n for no: ')
if start_game == ('y'):
    print('game starting')
elif start_game == ('n'):
    print('break statement')


def pick_random_word(randomword):
    """
    This function selects a random word from source
    and generates the number of guesses a user has
    """
    if start_game == 'y':
        word_in_play = random.choice(randomword)
        max_turns = (len(word_in_play)+2)
        print(word_in_play)
        print(f'You have {max_turns} guesses for this word!')


pick_random_word(randomword)


