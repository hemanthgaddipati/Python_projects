'''
PIG DICE GAME:
    The Pig Dice Game is a fun, strategic game where two players compete to be the
    first to reach 100 points. In this project, you’ll build a simplified version of the
    game where each player rolls a die repeatedly to accumulate points. However, if
    they roll a 1, they lose all points accumulated in that turn and must pass the die to
    the other player. The game requires players to decide whether to keep rolling to
    increase their score or to hold and secure their points before risking a roll of 1.
    
    Optional Enhancements
        • Allow players to set a custom target score before starting the game.
        • Modify the program to support more than two players, with each player taking
        turns to roll the dice and accumulate points.
        • Implement a feature that tracks the total score of each player over multiple
        rounds or games, allowing for a cumulative competition.
        • Introduce a rule where rolling two 6s consecutively resets the player’s score
        to 0, adding an extra layer of strategy.
'''
from random import randint

def roll_die():
    return randint(1,6)

def play_turn(player_name):
    turn_score = 0
    print(f"\n{player_name}'s turn")

    while True:
        roll = roll_die()
        print(f'You rolled a {roll}')

        if roll == 1:
            return 0

        turn_score += roll
        choice = input('Roll again? (y/n): ').lower()

        if choice != 'y':
            return turn_score

def main():
    scores = [0, 0]
    current_player = 0

    while True:
        player_name = f'Player {current_player + 1}'
        turn_score = play_turn(player_name)
        scores[current_player] += turn_score

        print(f'\nYou scored {turn_score} points this turn.')
        print(f'Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}.')

        if scores[current_player] >= 100:
            print(f'{player_name} wins!!')
            break

        current_player = 1 if current_player == 0 else 0

if __name__ == '__main__':
    main()
