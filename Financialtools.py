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
        self.category_summary = {"Income": 0, "Outcome": 0}  #初始化类别总金额

    def add_record(self, record):#添加一条财务记录到记录列表中。
        self.records.append(record)
        #更新类别总额
        if record.category == "Income":
            self.category_summary["Income"] += record.amount
        elif record.category == "Outcome":
            self.category_summary["Outcome"] += record.amount

    def input_record(self):# 用户输入财务记录信息，并将其添加到记录列表中。
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

         # 在这里使用 split_string 函数拆分描述
        words_list = split_string(description)
        print("Description split into words:", words_list)

        record = FinancialRecord(category, float(amount), date, description)
        self.add_record(record)

        return record  # 返回录入的记录

    def display_records(self):#显示所有财务记录的详细信息。
        for record in self.records:
            print(f"Category: {record.category}, Amount: {record.amount}, Date: {record.date}, Description: {record.description}")

    def save_to_file(self, filename, append=True):#将财务记录写入文件。
        mode = 'a' if append else 'w'
        with open(filename, mode) as file:
            for record in self.records:
                file.write(f"{record.category},{record.amount},{record.date},{record.description}\n")

    def update_category_summary(self):#更新每个类别的总金额汇总。
        self.category_summary.clear()
        for record in self.records:
            self.category_summary[record.category] = self.category_summary.get(record.category, 0) + record.amount

    def get_financial_summary(self):#获取财务汇总信息，包括总收入和总支出
        total_income = self.category_summary.get("Income", 0)
        total_outcome = self.category_summary.get("Outcome", 0)
        return total_income, total_outcome #总收入和总支出

    def remove_records_by_date(self):#根据用户输入的日期范围删除记录。
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        self.records = [record for record in self.records if not (start_date <= record.date <= end_date)]
        print(f"Records between {start_date} and {end_date} have been removed.")

    def get_category_summary(self):
        return self.category_summary
    
    def convert_currency(self, amount, from_currency, to_currency='USD'):
        converter = CurrencyRates()
        converted_amount = converter.convert(from_currency, to_currency, amount)
        return converted_amount



