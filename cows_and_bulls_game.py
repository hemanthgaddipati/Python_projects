'''
COWS AND BULLS GAME:
    The Cows and Bulls Game is a fun number-guessing challenge that tests your
    logical thinking and problem-solving skills. In this project, you’ll build a game
    where the computer comes up with a secret 4-digit number, and your job is to
    guess it. After each guess, you’ll get feedback in the form of "cows" and "bulls"—
    a "bull" means you’ve guessed the right digit in the right spot, while a "cow"
    means the digit is correct but in the wrong spot.
    
    Optional Enhancements
        • Allow the player to choose a difficulty level at the start of the game, which
        changes the length of the secret number or the number of attempts allowed.
        • Implement a system that offers hints after a certain number of incorrect
        guesses, providing more guidance to the player.

'''

from random import randint

def generated_number():
    return str(randint(1000, 9999))  # Generate a 4-digit number as a string

def validate_guess(player_guess, actual_number):
    cows_and_bulls = [0, 0]  # [cows, bulls]

    # Convert both player_guess and actual_number into lists for easier tracking
    remaining_digits = list(actual_number)

    # First, check for bulls (correct digit in the correct position)
    for i, guess in enumerate(player_guess):
        if guess == actual_number[i]:
            cows_and_bulls[1] += 1
            remaining_digits[i] = None  # Remove the digit from further checks

    # Then, check for cows (correct digit, wrong position)
    for i, guess in enumerate(player_guess):
        if guess != actual_number[i] and guess in remaining_digits:
            cows_and_bulls[0] += 1
            remaining_digits[remaining_digits.index(guess)] = None  # Mark as used

    return cows_and_bulls

def main():
    actual_number = generated_number()  # Generate the number as a string
    print(actual_number)
    print("I generated a 4-digit number, try to guess it!")

    while True:
        current_guess = input('Guess: ')

        if len(current_guess) != 4 or not current_guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        if current_guess == actual_number:
            print("You guessed the correct number. You win!!")
            break

        current_validation = validate_guess(current_guess, actual_number)
        print(f'{current_validation[0]} cows, {current_validation[1]} bulls')

if __name__ == '__main__':
    main()
