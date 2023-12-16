import sys
import re
import Financialtools
from datetime import datetime
import sys

def main():
        # 检查是否有命令行参数传入
    if len(sys.argv) > 1:
        welcome_message = sys.argv[1]
        print(welcome_message)
    manager = Financialtools.FinanceManager()
    while True:  # 进入无限循环，允许连续录入数据
        try:
            manager.input_record()
        except ValueError as e:
            print(e)
            
        # 新增货币转换部分
        convert_currency = input("Do you want to convert the amount to another currency? (yes/no): ")
        if convert_currency.lower() == 'yes':
            from_currency = input("Enter the currency of the amount (e.g., EUR, GBP): ")
            amount = float(input("Please enter the amount in " + from_currency + ": "))
            converted_amount = manager.convert_currency(amount, from_currency)
            print(f"Converted amount in USD: {converted_amount}")
            # 以下是如何处理转换后的金额
            # 例如，可以选择是否用转换后的金额替代原金额
            use_converted = input("Do you want to use the converted amount in USD for the record? (yes/no): ")
            if use_converted.lower() == 'yes':
                amount = converted_amount

        continue_choice = input("Do you want to continue entering more records? (yes/no): ")
        if continue_choice.lower() != "yes":
            break  # 如果用户不想继续录入数据，退出循环

# 显示类别总金额
    category_summary = manager.get_category_summary()
    print("Category Summary:")
    for category, amount in category_summary.items():
        print(f"{category}: {amount}")

# 提供用户选项
    choice = input("Do you want to remove records by date? (yes/no): ")
    if choice.lower() == 'yes':
        manager.remove_records_by_date()

    manager.display_records()
    #更新，获取财务总汇
    manager.update_category_summary()
    summary = manager.get_financial_summary()
    print(f"Total Income: {summary[0]}, Total Outcome: {summary[1]}")


    # 提供用户选项，是否将结果写入文件
    write_to_file = input("Do you want to write the results to a file? (yes/no): ")
    if write_to_file.lower() == 'yes':
        filename = input("Enter the filename: ")
        manager.save_to_file(filename)

if __name__ == "__main__":
    main()