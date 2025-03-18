'''
ATM SIMULATION:
    The ATM Simulation project is a practical and engaging exercise where you create
    a simple ATM system. The system allows users to check their balance, deposit
    money, and withdraw funds. This project introduces basic Object-Oriented
    Programming (OOP) concepts by encapsulating the ATM's logic within a class and
    handling user interactions through a controller class.
    
    Optional Enhancements
        • Implement PIN system where users must enter their PIN before accessing the ATM functions.
        • Add a feature to keep track of all transactions (deposits and withdrawals) and
          allow users to view their transaction history.
        • Allow the system to handle multiple user accounts, enabling users to log in
          and manage their individual balances.
'''
class ATM:

    def __init__(self):

        self.balance = 0

    def check_balance(self):

        print(f'Your current balance is: ${self.balance}')

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f'Successfully deposited ${amount}.')
        else:
            print('Deposit amount must be greater than 0.')

    def withdraw(self, amount):

        if amount > self.balance:
            print('Insufficient Balance.')
        elif amount <= 0:
            print('Withdrawl amount must be greater than 0.')
        else:
            self.balance -= amount
            print(f'Successfully withdrew ${amount}.')




def main():
    atm = ATM()
    while True:
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        
        choice = input('Please choose an option: ')
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            while True:
                try:
                    amount = float(input('Enter the amount to deposit: '))
                    atm.deposit(amount)
                    break
                except ValueError:
                    print('Please enter a valid number.')
        elif choice == '3':
            while True:
                try:
                    amount = float(input('Enter amount to withdraw: '))
                    atm.withdraw(amount)
                    break
                except ValueError:
                    print('Please enter a valid number.')
        elif choice == '4':
            print('Thanks for using the ATM. Have a good day.')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
