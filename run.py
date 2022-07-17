# Use limited array first to get code working
import random
# import request
# from rand_word import RandomWords


# Return a single random word
# r.get_random_word()
random_word = ['furthermore', 'copying', 'periodic', 'mental']

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
        user_input = input('Press y for yes or n for no:\n')
        if user_input == ('y'):
            break
        elif user_input == ('n'):
            print('Okey, have a nice day!\n')
            exit()
        else:
            print(f'{user_input} is not correct, please try again\n')
    return


def pick_random_word(randomword):
    """
    Selects a random word from source
    """
    return random.choice(randomword)


def calculate_max_turns(word):
    """
    Calculates number turns
    """
    max_turns = (len(word)+2)
    print(f'You have {max_turns} guesses for this word!\n')
    return max_turns


def display_board(missed_letters, correct_letters, secret_word):
    print('Missed letters:\n', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
        print()

    blanks = '_' * len(secret_word)

    for letters in range(len(secret_word)):
        if secret_word[letters] in correct_letters:
            blanks = blanks[
                :letters] + secret_word[letters] + blanks[letters + 1:]

    for letter in blanks:
        print(letter, end='')
    print()


def get_guess(already_guessed):
    while True:
        print('Please enter a letter: ')
        guess = input().strip().lower()
        if len(guess) != 1:
            print('Input a single letter')
        elif guess in already_guessed:
            print('You have already guessed that letter!')
        elif guess not in 'abcdefghijjklmnopqrstuvwxyz':
            print('Only enter letters in the aplhabet please!')
        else:
            return guess


start_game()
missed_letters = ''
correct_letters = ''
secret_word = pick_random_word(random_word)
game_is_finished = False
number_of_lives_left = calculate_max_turns(secret_word)


while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        print(f'{guess} is in the random word')
    else:
        number_of_lives_left -= 1
        print(
            f'{guess} is incorrect. {number_of_lives_left} left')

    if guess in secret_word:
        correct_letters += guess
        found_all_letters = True
        for letters in range(len(secret_word)):
            if secret_word[letters] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Congratulations you built the bear')
            print(f'Congratulations, {secret_word} is the correct word!')
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
        print('Do you wish to start the game again?')
        restart_input = input('Press y for yes or n for no:\n')
        if restart_input == ('y'):
            start_game()

        else:
            exit()
