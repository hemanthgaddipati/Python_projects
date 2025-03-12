'''
    Write a program to simulate a game of Rock, Paper, Scissors.
    The game will prompt the player to choose rock, paper, or scissors by typing 'r',
    'p', or 's'. The computer will randomly select its choice. The game will then display
    both choices using emojis and determine the winner based on the rules.
    
    Optional Enhancements
        • Modify the game so that the first player (or computer) to win two out of three
        rounds is declared the overall winner. This adds a competitive aspect to the
        game.
        • Keep a tally of how many times the player wins, loses, or ties with the
        computer. Display these statistics at the end of the game.
        • Add an option for two players to play against each other, taking turns to input
        their choices. The program should then determine the winner based on their
        inputs.
'''
from random import choice

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def get_user_choice():

    while True:
        user_choice = input('Rock, Paper, Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")
    return

def display_choice(user_choice, computer_choice):

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')
    return

def determine_winner(user_choice, computer_choice):

    winner = None
    if user_choice == computer_choice:
        print('Tie!!')
    elif (
        (user_choice == ROCK and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == ROCK)):
        print('You Lose!')
        winner = 'Computer'
    else:
        print('You Win!')
        winner = 'You'
    return winner

def play_game():

    player_wins = 0
    player_losses = 0
    ties = 0

    while True:
        user_choice = get_user_choice()

        computer_choice = choice(choices)

        display_choice(user_choice, computer_choice)

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'You':
            player_wins += 1
        elif winner == 'Computer':
            player_losses += 1
        else:
            ties += 1

        if player_wins == 2:
            print("You won 2 games before Computer so you WIN!!!")
            break
        if player_losses == 2:
            print("Computer won 2 games before you so you LOST!!!")
            break

        should_continue = input('Continue? (y/n): ').lower()

        if should_continue == 'n':
            print("Thank you for playing.")
            break

    print('---------------------------')
    print('--------Statistics---------')
    print(f'  Total games Played : {sum([player_wins, player_losses, ties])}')
    print(f'  Total games Won : {player_wins}')
    print(f'  Total games Lost : {player_losses}')
    print(f'  Total games Tied : {ties}')
    print('---------------------------')

    return

play_game()
