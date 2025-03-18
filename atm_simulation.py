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
    """
    Represents an ATM with basic functionalities such as checking balance, 
    depositing money, and withdrawing money.

    Attributes:
        balance (float): The current balance in the ATM.
    """

    def __init__(self):

        """
        Initializes the ATM with a balance of 0.
        """
        self.balance = 0

    def check_balance(self):

        """
        Retrieves the current balance of the ATM.

        Returns:
            float: The current balance.
        """
        return self.balance

    def deposit(self, amount):

        """
        Deposits a specified amount into the ATM balance.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is less than or equal to 0.
        """
        if amount <= 0:
            raise ValueError('Deposit amount must be greater than 0')

        self.balance += amount

    def withdraw(self, amount):

        """
        Withdraws a specified amount from the ATM balance.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is less than or equal to 0 or 
                        exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError('Withdrawl amount must be greater than 0.')
        if amount > self.balance:
            raise ValueError('Insufficient balance.')

        self.balance -= amount


class ATMController:
    """
    Handles user interactions with the ATM, including displaying the menu, 
    processing deposits, withdrawals, and checking the balance.

    Attributes:
        atm (ATM): An instance of the ATM class to manage the ATM operations.
    """

    def __init__(self):

        """
        Initializes the ATMController with an instance of the ATM class.
        """
        self.atm = ATM()

    def get_number(self, prompt):

        """
        Prompts the user to enter a number and validates the input.

        Args:
            prompt (str): The message to display to the user.

        Returns:
            float: The valid number entered by the user.
        """
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Please enter a valid number.')

    def display_menu(self):

        """
        Displays the ATM menu options to the user.
        """
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

    def check_balance(self):

        """
        Displays the current balance of the user.
        """
        balance = self.atm.check_balance()
        print(f'Your current balance is: ${balance}')

    def deposit(self):

        """
        Prompts the user to enter an amount to deposit and processes the deposit.

        Handles invalid input and displays appropriate error messages.
        """
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                print(f'Successfully deposited ${amount}.')
                break
            except ValueError as error:
                print(error)

    def withdraw(self):

        """
        Prompts the user to enter an amount to withdraw and processes the withdrawal.

        Handles invalid input and displays appropriate error messages._summary_
        """
        while True:
            try:
                amount = self.get_number('Enter amount to withdraw: ')
                self.atm.withdraw(amount)
                print(f'Successfully withdrew ${amount}.')
                break
            except ValueError as error:
                print(error)

    def run(self):

        """
        Runs the main ATM loop, allowing the user to interact with the ATM by 
        choosing options from the menu.
        """
        while True:
            self.display_menu()
            choice = input('Please choose an option: ')

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print('Thanks for using the ATM. Have a good day.')
                break
            else:
                print('Invalid choice. Please try again.')

def main():

    """
    The entry point of the program. Initializes the ATMController and starts the ATM simulation.
    """
    atm = ATMController()
    atm.run()

if __name__ == '__main__':
    main()
