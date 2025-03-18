'''
SLOT MACHINE GAME:

    The Slot Machine Game is a fun and simple project that simulates a classic slot
    machine. The player starts with a balance, places bets, and spins the reels. If the
    symbols on the reels match, the player wins a payout based on their bet. The
    game continues until the player either runs out of money or decides to walk away
    with their winnings.
    
    Payout Rules:
        • If all three symbols match, the player wins 10 times their bet.
        • If two out of three symbols match, the player wins 2 times their bet.
        • If none of the symbols match, the player loses their bet.
        
    Optional Enhancements
        • Introduce new payout combinations, such as matching two specific symbols,
        for more chances to win.
        
'''
import random

def get_starting_balance():

    """
    Prompts the player to enter their starting balance and validates the input.

    Returns:
        int: The starting balance entered by the player.
    """

    while True:
        try:
            balance = int(input('Enter your starting balance: $'))
            if balance <= 0:
                print('Balance must be a positive number.')
            else:
                return balance
        except ValueError:
            print('Please enter a valid number!')

def get_bet_amount(balance):

    """
    Prompts the player to enter their bet amount and validates the input.

    Args:
        balance (int): The current balance of the player.

    Returns:
        int: The bet amount entered by the player.
    """

    while True:
        try:
            bet_amount = int(input('Enter your bet amount: $'))
            if bet_amount > balance or bet_amount <= 0:
                print(f'Invalid bet amount. You can bet between $1 and ${balance} (inclusive).')
            else:
                return bet_amount
        except ValueError:
            print("Please enter a valid amount!")

def spin_reels():

    """
    Simulates spinning the slot machine reels.

    Returns:
        List[str]: A list of three randomly selected symbols.
    """

    symbols = ['🍒', '🍋', '🔔', '⭐️', '🍉']
    return [random.choice(symbols) for _ in range(3)]

def display_reels(reels):

    """
    Displays the symbols on the slot machine reels.

    Args:
        reels (List[str]): A list of three symbols representing the slot machine reels.
    """

    print(f'{reels[0]} | {reels[1]} | {reels[2]}')

def calcualte_payout(reels, bet):

    """
    Calculates the payout based on the symbols on the reels and the bet amount.

    Args:
        reels (List[str]): A list of three symbols representing the slot machine reels.
        bet (int): The bet amount placed by the player.

    Returns:
        int: The payout amount based on the symbols on the reels.
    """

    if reels[0] == reels[1] ==reels[2]:
        return bet * 10
    if reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return bet * 2
    return 0

def main():

    """
    The main function to run the Slot Machine Game. It initializes the game,
    prompts the player for their starting balance, and manages the game loop
    where the player places bets, spins the reels, and either wins or loses money
    based on the outcome.
    """

    balance = get_starting_balance()

    print('Welcome to the Slot Machine Game!')
    print(f'You start with a balance of ${balance}')

    while balance > 0:
        print(f'\nCurrent balance: ${balance}')

        bet_amount = get_bet_amount(balance)
        reels = spin_reels()
        display_reels(reels)
        payout = calcualte_payout(reels, bet_amount)

        if payout > 0:
            print(f'You won ${payout}!')
        else:
            print('You Lost')

        balance += payout - bet_amount

        if balance <= 0:
            print('You are out of money! Game over.')
            break

        play_again = input('Do you want to play again? (y/n): ').lower()

        if play_again != 'y':
            print(f'You walk away with ${balance}.')
            break

if __name__ == '__main__':
    main()
