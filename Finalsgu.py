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