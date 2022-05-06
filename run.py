# Use limited array first to get code working
import random
from art import * 

tprint('mikaela')

randomword = ['furthermore', 'copying', 'periodic', 'mental']
lettersGuessed = ""

# This variabel lets user initiate the game
# Credit for code structure (not a complete copy paste) to 
# Code Grepper, please see README for link.
print('This is a hangman type game.')
print('The computer will generate a random word.')
print('The number of times you have to guess the letters of that word,')
print('depends on the number of letters in that random word.')
print('You get 2 extra attempts with each word.')
start_game = input('Do you wish to start? Press y for yes or n for no: ')
if start_game == ('y'):
    print('Lets build a bear!')
elif start_game == ('n'):
    print('Okey, have a nice day!')


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

    while max_turns > 0:
        guess = input('Please enter a letter: ')
        if guess in word_in_play:
            print(f'{guess} is in the random word')
            break
        else:
            max_turns -= 1
            print(f'{guess} was incorrect. You have {max_turns} attempts left.')
            break


pick_random_word(randomword)

