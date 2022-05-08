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
        print('Do you wish to start?')
        user_input = input('Press y for yes or n for no:')
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
    Calculates number turns
    """
    max_turns = (len(word)+2)
    print(f'You have {max_turns} guesses for this word!\n')
    return max_turns


def display_board(missed_letters, correct_letters, secret_word):
    print('Missed letters: ', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
        print()
    
    num = '_' * len(secret_word)

    for guess in range(0, num):
        if secret_word[guess] in correct_letters:
            print(secret_word[guess], end=' ')
        elif secret_word[guess] == '':
            print('', end='')
        else:
            print('_', end=' ')
    print('')


def loop_letters(lives_left, word_in_play):
    """
    Looping through the word
    according to the number of lives left.
    When lives_left == 0 or all letters are
    found the loop will break
    """
    guess = secret_word
    letters_guessed = ""
    letters_guessed += guess

    while lives_left > 0:
        input('Please enter a letter: ')
        guess = input().strip().lower()
        if len(guess) != 1:
            print('You only have to guess one letter!')
        elif guess in letters_guessed:
            print(f'You have already used {guess}!')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a value that is a letter')
        elif guess in word_in_play:
            print(f'{guess} is in the random word')
            return guess
        else:
            lives_left -= 1
            print(f'{guess} is incorrect. You have {lives_left} attempts left')


start_game()
game_is_finished = False
missed_letters = ''
correct_letters = ''
secret_word = pick_random_word(whateverword)
number_of_lives_left = calculate_max_turns(secret_word)
loop_letters(number_of_lives_left, secret_word)

while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = loop_letters(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Congratulations you guessed all the letters')
            print(f'of the word {secret_word}!')
            game_is_finished = True
    else:
        missed_letters += guess
        if len(missed_letters) == number_of_lives_left:
            display_board(missed_letters, correct_letters, secret_word)
            print("Unfortnuately you didn't guess the correct")
            print('letters in the word.')
            print(f'The word was {secret_word}')
            game_is_finished = True

    if game_is_finished:
        if start_game():
            start_game()
            missed_letters = ''
            correct_letters = ''
            game_is_finished = False
            secret_word = pick_random_word(whateverword)
            number_of_lives_left = calculate_max_turns(secret_word)
        else:
            exit()
