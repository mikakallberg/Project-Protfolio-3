# Use limited array first to get code working
import random
from art import * 

tprint('mikaela')

randomword = ['furthermore', 'copying', 'periodic', 'mental']

start_game = input('Do you wish to start? Press y for yes or n for no: ')
if start_game == ('y'):
    print('game starting')
elif start_game == ('n'):
    print('break statement')


def pick_random_word(randomword):
    """
    This function selects a random word from source
    """
    if start_game == 'y':
        word_in_play = random.choice(randomword)
        print(word_in_play)


pick_random_word(randomword)


