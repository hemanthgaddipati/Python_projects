'''

    The Word Guessing Game is a fun and interactive project where players try to
    guess a secret word, one letter at a time. The word is selected randomly from a list
    of words stored in a text file. The player has six attempts to guess the word, with
    each incorrect guess reducing the remaining attempts. Correctly guessed letters
    are revealed in their respective positions, while incorrect guesses prompt the
    player to try again.
    
    Optional Enhancements
        • Implement a hint feature that the player can use once or twice per game to
          reveal a letter in the word. This can make the game a bit easier and more fun.
        • Offer different difficulty levels that change the length of the words to be guessed. 
          Longer words can be for more advanced players, while shorter words could be for beginners.
        • Keep a record of how many games the player has won or lost during their
          session. Display this information at the end of each game.

'''
import random
import re

# read words from text file
def read_words():

    try:
        with open('./helper_files/words.txt', 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print('Words.txt does not exist in the past specified.')
        return []

def display_word(secret_word, guessed_letters):

    word_to_display = ''

    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += '_'

    print(word_to_display)

def get_guess(guessed_letters):

    while True:
        guess = input('Enter a letter: ')

        if len(guess) != 1:
            print('Enter only one letter!')
        elif not re.search('[a-z]', guess):
            print('Enter only letters from a to z')
        elif guess in guessed_letters:
            print('You already guessed that letter.')
        else:
            return guess

def is_word_guessed(secret_word, guessed_letters):

    for letter in secret_word:
        if letter not in guessed_letters:
            return False

    return True

def main():

    words = read_words()

    if not words:
        print('No words loaded from file.')
        return

    secret_word = random.choice(words)
    print(secret_word)

    attempts = 6
    guessed_letters = []

    while attempts > 0:
        display_word(secret_word, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print('Good guess!')
            if is_word_guessed(secret_word, guessed_letters):
                print('Congratulations!!! You guessed the word.')
                break
        else:
            print('Wrong guess.')
            attempts -= 1
            if attempts == 0:
                print(f'Game over! You lost. The word was {secret_word}')

if __name__ == '__main__':
    main()
