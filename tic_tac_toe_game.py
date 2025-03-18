'''
TIC TAC TOE Game:

    Write a program to create a classic Tic Tac Toe game. Two players take turns
    marking Xs and Os on a 3x3 grid. The first player to align three of their marks
    either vertically, horizontally, or diagonally wins the game.
    The board is printed after each move, with colored marks to distinguish between
    the players. The game checks for a winner after each move and ends when a
    player wins or when the board is full, resulting in a draw.
    
    Optional Enhancements
        • Add a scoring system that tracks the number of games won by each player across multiple rounds.
        
        • Allow players to start a new game without restarting the program.
        
        • Modify to allow different board sizes (e.g., 4x4 or 5x5) for a more challenging experience.
        
'''

from termcolor import colored

X = 'X'
O = 'O'

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def cell(mark):
    """
    Returns the formatted representation of a cell on the board.

    Args:
        mark (str): The mark in the cell ('X', 'O', or ' ').

    Returns:
        str: The colored representation of the mark ('X' in red, 'O' in green, or empty).
    """
    if mark == X:
        return colored(mark, 'red')
    return colored(mark, 'green')

def print_board(game_board):
    """
    Prints the current state of the Tic Tac Toe board with formatted cells.

    Args:
        board (list): A 3x3 list representing the game board.
    """
    line = '---+---+---'
    print(line)
    for row in game_board:
        print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])}')
        print(line)

def check_winner(game_board):
    """
    Checks if there is a winner on the board.

    Args:
        board (list): A 3x3 list representing the game board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for column in range(3):
        if game_board[0][column] == game_board[1][column] == game_board[2][column] != ' ':
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != ' ' or game_board[0][2] == game_board[1][1] == game_board[2][0] != ' ':
        return True
    return False

def is_full(game_board):
    """
    Checks if the board is full (no empty spaces left).

    Args:
        game_board (list): A 3x3 list representing the game board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in game_board:
        if ' ' in row:
            return False
    return True

def get_position(prompt):
    """
    Prompts the user to enter a valid position (row or column) on the board.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        int: A valid position (0, 1, or 2).
    """
    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print('Invalid input. ')



def get_move(current_player):
    """
    Prompts the current player to make a move by selecting a valid position on the board.

    Args:
        current_player (str): The current player's mark ('X' or 'O').
    """
    print(f"Player {current_player}'s turn")

    while True:
        row = get_position('Enter row (0 or 1 or 2): ')
        column = get_position('Enter column (0 or 1 or 2): ')

        if board[row][column] == ' ':
            board[row][column] = current_player
            break

        print('This spot is already taken')


def main():
    """
    The main function to run the Tic Tac Toe game.

    Gameplay:
        - Alternates turns between two players ('X' and 'O').
        - Prints the board after each move.
        - Checks for a winner or a full board after each move.
        - Ends the game when a player wins or the board is full.

    Returns:
        None
    """
    print_board(board)

    current_player = X

    while True:
        get_move(current_player)

        print_board(board)

        if check_winner(board):
            print(f'Player {current_player} wins!')
            break

        if is_full(board):
            print('Board is full')
            break

        current_player = O if current_player == X else X


if __name__ == '__main__':
    main()
