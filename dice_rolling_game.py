'''
Dice rolling game: 
    Write a program that simulates rolling a pair of dice. Each time the program runs, it
    should randomly generate two numbers between 1 and 6 (inclusive), representing
    the result of each die. The program should then display the results and ask if the
    user would like to roll again.
    
    Optional Enhancements
        • Modify the program so the user can specify how many dice they want to roll.
        • Add a feature that keeps track of how many times the user has rolled the dice
          during the session. This will require a counter that increments each time the
          dice are rolled.
'''
from random import randint

def values(dice):
    result = []
    for _ in range(dice):
        result.append(randint(1,6))
    return tuple(result)

    
def dice_rolling_game(choise = input("Roll the dice? (y/n): ").lower(), 
                      dice = int(input("Enter number of dice: "))):
    if dice == 0:
        print(f'Dice entered = {dice}. Please enter number greater tham 1.')
        return
    
    roll_count = 0
    while True:
        if choise == 'y':
            result = values(dice)
            print(f'{result}')
            choise = input("Roll the dice? (y/n):").lower()
            roll_count += 1
        elif choise == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Invalid Choise!!')
            break
    print(f'Session terminated! Number of Dice rolls this session is {roll_count}.')
    return


dice_rolling_game()
