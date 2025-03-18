'''
Number Guessing Game:
    Write a program to have the computer randomly select a number between 1 and
    100, and then prompt the player to guess the number. The program should give
    hints if the guess is too high or too low.
    
    Optional Enhancements:
        • Allow the user to specify the minimum and maximum values for the number
        range before the game starts. This gives the player more control over the
        difficulty level.
        • Implement a feature that limits the number of guesses a player can make. If
        the player runs out of attempts, the game should end, and the correct number
        should be revealed.
        • Add a feature that keeps track of the fewest attempts it took to guess the
        number correctly. The program should display this "best score" at the end of
        each game.
'''
from random import randint

class NumberGuessingGame:
    """
    A class to represent the Number Guessing Game.

    Attributes:
        best_score (float): Tracks the fewest number of attempts it took to guess the number correctly.
    """

    def __init__(self):
        """
        Initializes the NumberGuessingGame class.

        Attributes:
            best_score (float): Tracks the fewest number of attempts it took to 
                                guess the number correctly.
        """
        self.best_score = float('inf')  # Initialize the best score to an infinite value

    def play_game(self, lucky_number_min, lucky_number_max):
        """
        Plays a single round of the number guessing game.

        Args:
            lucky_number_min (int): The minimum value for the range of the lucky number.
            lucky_number_max (int): The maximum value for the range of the lucky number.

        Gameplay:
            - The computer randomly selects a number within the specified range.
            - The player has a limited number of attempts to guess the number.
            - Provides feedback if the guess is too high, too low, or correct.
            - Tracks and updates the best score if the player guesses the number in fewer attempts.

        Raises:
            ValueError: If the player's input is not a valid integer.
        """

        lucky_number = randint(lucky_number_min, lucky_number_max)
        print(f'LUCKY NUMBER IS: {lucky_number}')

        number_of_guesses = 5
        current_guess = 0
        while current_guess < number_of_guesses:
            try:
                player_guess = int(input('Guess the number (between 1 and 100 inclusive): '))
                if not(1 <= player_guess <= 100):
                    print("Please enter a valid number!")
                elif player_guess > lucky_number:
                    print("Too high!")
                elif player_guess < lucky_number:
                    print("Too low!")
                else:
                    print("Congratulations! You guessed the number!")
                    # Check if the current number of guesses is the best score
                    if current_guess + 1 < self.best_score:
                        self.best_score = current_guess + 1
                    break
            except ValueError:
                print("Please enter a valid number!")
            current_guess += 1
        else:
            print(f'You lost. Number of guesses exceeded! The lucky number is {lucky_number}.')

        print(f'Best score so far (fewest attempts): {self.best_score}')


# Main game loop
game = NumberGuessingGame()
while True:
    game.play_game(int(input("Please enter minimum number for range: ")),
                   int(input("Please enter maximum number for range: ")))
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
