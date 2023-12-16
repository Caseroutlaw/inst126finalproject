#INST126 Final Project
#Shenghao Gu
#UID 119385487
import sys
import re
import Financialtools
from datetime import datetime
import Currency_exchange 

def main():
    while True: # Loop asks users if they need to check the exchange rate of USD to RMB today
        check_exchange_rate = input("Do you need to know the exchange rate between US dollar and RMB today? (yes/no): ").lower()
        if check_exchange_rate == 'yes':
            ## Call the Currency_exchange module to get the exchange rate
            exchange_rate = Currency_exchange.get_exchange_rate()
            if exchange_rate:
                print(f"USD to CNY Exchange rate: {exchange_rate}")
            else:
                print("Exchange rate data could not be obtained.")
            break
        elif check_exchange_rate == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'. ")

    # # Check if any command line arguments are passed in, and display if so
    if len(sys.argv) > 1:
        welcome_message = sys.argv[1]
        print(welcome_message)
    
    # Create a FinanceManager instance
    manager = Financialtools.FinanceManager()

    while True:  # Enter an infinite loop, allowing continuous data entry
        try:
            manager.input_record() # User enters financial records
        except ValueError as e:
            print(e)

        # currency conversion section
        while True:
                convert_currency = input("Do you want to convert the amount to another currency? (yes/no): ").lower()
                if convert_currency == 'yes':
                    while True:
                        try:
                            from_currency = input("Enter the currency of the amount (e.g., EUR, GBP): ").upper()
                            amount = float(input("Please enter the amount in " + from_currency + ": "))
                            break  # Out of the loop
                        except ValueError:
                            print("Please enter a valid amount.")

                    converted_amount = manager.convert_currency(amount, from_currency) # Call the conversion function and display the converted amount
                    print(f"Converted amount in USD: {converted_amount}")

                    while True:
                        use_converted = input("Do you want to use the converted amount in USD for the record? (yes/no): ").lower()
                        if use_converted in ['yes', 'no']:
                            break  # Out of the loop when the input is valid
                        else:
                            print("Please enter 'yes' or 'no'.")

                    if use_converted == 'yes':
                        amount = converted_amount
                    break  #Out of the loop when the input is valid
                elif convert_currency == 'no':
                    break  #Out of the loop when the input is valid
                else:
                    print("Please enter 'yes' or 'no'. Please re-enter.")

        continue_choice = input("Do you want to continue entering more records? (yes/no): ")
        if continue_choice.lower() != "yes":
            break  # If the user does not want to continue to enter data, exit the loop    


# Displays the total amount of the category
    category_summary = manager.get_category_summary()
    print("Category Summary:")
    for category, amount in category_summary.items():
        print(f"{category}: {amount}")

# Provide user options
    choice = input("Do you want to remove records by date? (yes/no): ")
    if choice.lower() == 'yes':
        manager.remove_records_by_date()

    # Display all financial records
    manager.display_records()
    
    #Update, get financial summary
    manager.update_category_summary()
    summary = manager.get_financial_summary()
    print(f"Total Income: {summary[0]}, Total Outcome: {summary[1]}")


    # Provides the user with the option to write the results to a file
    write_to_file = input("Do you want to write the results to a file? (yes/no): ")
    if write_to_file.lower() == 'yes':
        filename = input("Enter the filename: ")
        manager.save_to_file(filename)

if __name__ == "__main__":
    ## When this script is run as the main program, the main function is called.
    main()