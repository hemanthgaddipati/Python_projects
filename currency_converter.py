'''
CURRENCY CONVERTER:

    Write a program to convert an amount of money from one currency to another
    using fixed exchange rates. The user inputs the amount and selects the currencies
    for conversion.
    
    Optional Enhancements:

        • Modify the program so that the user can see the equivalent amount in several different currencies at the same time. 
          For example, converting 100 USD to EUR, CAD, and GBP all at once.
          
        • Expand the list of available currencies for conversion. This might involve adding more fixed exchange rates to the program.
        
        • Keep a history of the most recent conversions made during the session and display this history at the end of the program.
        
'''

def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount!')


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD', 'GBP', 'AUD', 'JPY', 'INR')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD/GBP/AUD/JPY/INR): ').upper()
        if currency not in currencies:
            print('Invalid currency!')
        else:
            return currency


def convert(amount, source_currency, target_currency):
    exchange_rates = {
        'USD': {'EUR': 0.94, 'CAD': 1.45, 'GBP': 0.74, 'AUD': 1.49, 'JPY': 110.15, 'INR': 75.25},
        'CAD': {'EUR': 0.65, 'USD': 0.69, 'GBP': 0.51, 'AUD': 1.03, 'JPY': 75.86, 'INR': 51.87},
        'EUR': {'USD': 1.06, 'CAD': 1.54, 'GBP': 0.79, 'AUD': 1.59, 'JPY': 117.55, 'INR': 80.03},
        'GBP': {'USD': 1.35, 'CAD': 1.96, 'EUR': 1.26, 'AUD': 2.02, 'JPY': 148.56, 'INR': 101.34},
        'AUD': {'USD': 0.67, 'CAD': 0.97, 'EUR': 0.63, 'GBP': 0.50, 'JPY': 73.66, 'INR': 50.18},
        'JPY': {'USD': 0.0091, 'CAD': 0.013, 'EUR': 0.0085, 'GBP': 0.0067, 'AUD': 0.014, 'INR': 0.68},
        'INR': {'USD': 0.013, 'CAD': 0.019, 'EUR': 0.012, 'GBP': 0.0099, 'AUD': 0.020, 'JPY': 1.46}
    }

    if source_currency == target_currency:
        return amount
    return amount * exchange_rates[source_currency][target_currency]


def main():
    history = []  # List to store the conversion history
    
    while True:
        amount = get_amount()
        source_currency = get_currency('Source')

        # List of target currencies you want to convert to
        target_currencies = ['USD', 'EUR', 'CAD', 'GBP', 'AUD', 'JPY', 'INR']

        # Print the conversion results
        print(f"\nConverting {amount} {source_currency} to the following currencies:")

        for target_currency in target_currencies:
            if target_currency != source_currency:
                converted_amount = convert(amount, source_currency, target_currency)
                print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')
                
                # Add to history
                history.append(f'{amount} {source_currency} -> {converted_amount:.2f} {target_currency}')
            else:
                print(f'{amount} {source_currency} is equal to {amount:.2f} {source_currency}')
                # Add to history
                history.append(f'{amount} {source_currency} -> {amount:.2f} {source_currency}')

        # Ask the user if they want to perform another conversion or exit
        again = input("\nDo you want to convert another amount? (yes/no): ").strip().lower()
        if again != 'yes':
            break

    # Display history at the end
    print("\nConversion History:")
    print("_____________________________")
    for record in history:
        print(record)
        print("_____________________________")



if __name__ == "__main__":
    main()

