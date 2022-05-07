# Use limited array first to get code working
import random
from art import *

tprint('mikaela')

whateverword = ['furthermore', 'copying', 'periodic', 'mental']

letters_guessed = ""

# This variabel lets user initiate the game
# Credit for code structure (not a complete copy paste) to
# Code Grepper, please see README for link.
print('This is a hangman type game.')
print('The computer will generate a random word.')
print('The number of times you have to guess the letters of that word,')
print('depends on the number of letters in that random word.')
print('You get 2 extra attempts with each word.')
user_input = input('Do you wish to start? Press y for yes or n for no: \n')


def start_game(value_input):
    """
    check if input is y or n
    """
    value_input = user_input
    while True:
        try:
            value_input == ('y') or value_input == ('n')
        except ValueError as e:
            print(f'{e} is not correct, please try again\n')
            continue
        else:
            break
    return value_input


def pick_random_word(randomword):
    """
    Selects a random word from source
    """
    word_in_play = random.choice(randomword)
    if start_game_command == 'y':
        print(word_in_play)
    return word_in_play


def calculate_max_turns(word):
    """
    Calculates number turns
    """
    print(word)
    max_turns = (len(word)+2)
    print(f'You have {max_turns} guesses for this word!\n')
    return max_turns


def loop_letters(lives_left, word_in_play):
    """
    Looping through the word
    according to the number of lives left
    """
    while lives_left > 0:
        guess = input('Please enter a letter: ')
        if guess in word_in_play:
            print(f'{guess} is in the random word')
            break
        else:
            lives_left -= 1
            print(f'{guess} is incorrect. You have {lives_left} attempts left')
            break


start_game_command = start_game(user_input)
generated_word = pick_random_word(whateverword)
print(generated_word)
number_of_lives_left = calculate_max_turns(generated_word)
loop_letters(number_of_lives_left, generated_word)
