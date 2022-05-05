# Use limited array first to get code working
import random
from art import * 

tprint('mikaela')

randomword = ['furthermore', 'copying', 'periodic', 'mental']

def pick_random_word(randomword):
    """
    This function selects a random word from source
    """
    word_in_play = random.choice(randomword)
    print(word_in_play)

pick_random_word(randomword)


