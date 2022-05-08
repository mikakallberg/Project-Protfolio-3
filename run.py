# Use limited array first to get code working
import random
from art import *

tprint('mikaela')

whateverword = ['furthermore', 'copying', 'periodic', 'mental']

# This variabel lets user initiate the game
# Credit for code structure (not a complete copy paste) to
# Code Grepper, please see README for link.
print('This is a hangman type game.')
print('The computer will generate a random word.')
print('The number of times you have to guess the letters of that word,')
print('depends on the number of letters in that random word.')
print('You get 2 extra attempts with each word.')


def start_game():
    """
    check if input is y or n
    """
    while True:
        user_input = input('Do you wish to start? Press y for yes or n for no: ')
        if user_input == ('y'):
            break
        elif user_input == ('n'):
            print('Okey, have a nice day!\n')
        else:
            print(f'{user_input} is not correct, please try again\n')
    return 


def pick_random_word(randomword):
    """
    Selects a random word from source
    """
    word_in_play = random.choice(randomword)
    return word_in_play


def calculate_max_turns(word):
    """
    Calculates number of turns
    """
    max_turns = (len(word)+2)
    print(f'You have {max_turns} guesses for this word!\n')
    return max_turns


def loop_letters(lives_left, word_in_play):
    """
    Looping through the word
    according to the number of lives left.
    When lives_left == 0 or all letters are
    found the loop will break
    """
    while lives_left > 0:
        guess = input('Please enter a letter: ')
        if guess in word_in_play:
            print(f'{guess} is in the random word')
        else:
            lives_left -= 1
            print(f'{guess} is incorrect. You have {lives_left} attempts left')

        letters_guessed = ""
        letters_guessed = letters_guessed + guess
        num = len(word_in_play)

        for guess in range(0, num):
            print(word_in_play, guess)
            if word_in_play[guess] == word_in_play:
                print(word_in_play[guess], end='')
            elif word_in_play[guess] == '':
                print('', end='')
            else:
                print('_', end='')
        print('')

        if letters_guessed == word_in_play:
            print(f'Congratulations you guessed all the letters of the word {word_in_play}!')
            break
    else:
        print(f"Unfortnuately you didn't guess the correct letters of the word {word_in_play}")


start_game_command = start_game()
generated_word = pick_random_word(whateverword)
number_of_lives_left = calculate_max_turns(generated_word)
loop_letters(number_of_lives_left, generated_word)
