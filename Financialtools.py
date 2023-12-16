#INST126 Final Project
#Shenghao Gu
#UID 119385487
import re
from datetime import datetime
from forex_python.converter import CurrencyRates


#Advanced String function Def
def split_string(input_string, delimiter=' '):
    return input_string.split(delimiter)
def use_raw_string(path):
    # Returning a raw string representation of a file path
    return r'{}'.format(path)

def is_valid_date(date_string):
    # Regex pattern for a simple date in format YYYY-MM-DD
    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    return pattern.match(date_string) is not None

def extract_amount_from_record(record_string):
    # Regex to extract amount from a record assuming format "Amount: $123.45"
    pattern = re.compile(r'Amount:\s+\$(\d+\.\d{2})')
    match = pattern.search(record_string)
    return match.group(1) if match else None

class FinancialRecord:
    def __init__(self, category, amount, date, description):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

class FinanceManager:
    def __init__(self):
        self.records = []
        self.category_summary = {"Income": 0, "Outcome": 0}  #Initializes the total amount of the category

    #Add a financial record to the record list.
    def add_record(self, record):
        self.records.append(record)
        if record.category == "Income":
            self.category_summary["Income"] += record.amount
        elif record.category == "Outcome":
            self.category_summary["Outcome"] += record.amount

    # The user enters financial record information and adds it to the list of records.
    def input_record(self):
        while True:
            category = input("Please enter category (Income/Outcome): ")
            if re.match(r'^(Income|Outcome)$', category):
                break
            else:
                print("Category entered incorrectly! Only can be 'Income' or 'Outcome'")

        amount = input("Please enter the amount: ")
        while not re.match(r'^\d+(\.\d+)?$', amount):
            print("Amount entered in the wrong format")
            amount = input("Please enter the amount: ")

        date = input("Please enter the date (YYYY-MM-DD): ")
        while True:
            try:
                datetime.strptime(date, '%Y-%m-%d')
                break
            except ValueError:
                print("The date format is incorrect. The correct format is: YYYY-MM-DD")
                date = input("Please enter the date (YYYY-MM-DD): ")

        description = input("Please enter a description: ")

         # Use the split_string function here to split the description
        words_list = split_string(description)
        print("Description split into words:", words_list)

        record = FinancialRecord(category, float(amount), date, description)
        self.add_record(record)

        return record  # Return the entered record
    
    #Displays details of all financial records.
    def display_records(self):
        for record in self.records:
            print(f"Category: {record.category}, Amount: {record.amount}, Date: {record.date}, Description: {record.description}")

    #Write financial records to a file.
    def save_to_file(self, filename, append=True): 
        mode = 'a' if append else 'w'
        with open(filename, mode) as file:
            for record in self.records:
                file.write(f"{record.category},{record.amount},{record.date},{record.description}\n")

    #Update total dollar totals for each category.
    def update_category_summary(self):
        self.category_summary.clear()
        for record in self.records:
            self.category_summary[record.category] = self.category_summary.get(record.category, 0) + record.amount

    #Get financial summary information, including total income and total outcomes
    def get_financial_summary(self):
        total_income = self.category_summary.get("Income", 0)
        total_outcome = self.category_summary.get("Outcome", 0)
        return total_income, total_outcome #Total income and total outcoms

    #Deletes records based on the date range entered by the user.
    def remove_records_by_date(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        self.records = [record for record in self.records if not (start_date <= record.date <= end_date)]
        print(f"Records between {start_date} and {end_date} have been removed.")

    #Get a summary of category totals.
    def get_category_summary(self):
        return self.category_summary
    
    #Convert a specified amount from one currency to another.
    def convert_currency(self, amount, from_currency, to_currency='USD'):
        converter = CurrencyRates()
        converted_amount = converter.convert(from_currency, to_currency, amount)
        return converted_amount