Financial management program

1. Function
The program is a financial management computing application built for me to help me record and manage personal and corporate financial data.
Specific functions include:
Real-time exchange rate query: Obtain the current exchange rate between US dollar and RMB from the Internet.
Recording financial data: Allows users to enter records of income and expenses, and users can choose to keep these records in an internal structure.
Currency Calculator: Users can convert the amount entered from one currency to US dollars.
View the Financial Summary: Shows the total income and expenses for all records, as well as a summary by expenditure/income category.
Save and Delete records: Allows users to save financial records to files, or delete records based on date ranges.

2. Instructions for use
Run program
Make sure that Python 3.x is installed on your computer.
Clone or download this repository locally.
Run the Finalsgu.py file in the project root directory. You can do this using the command line interface. ,
For example, enter python Finalsgu.py
Use process:
After the program is started, the user is first asked if he needs to check the current exchange rate between the US dollar and the RMB. Enter yes or no when prompted.
Next, the program allows the user to enter financial records. You need to enter the category (Income or Outcome), amount, date, and description. (Input errors will be checked repeatedly until the user enters the correct format.)
The program provides currency conversion functions. If needed, enter yes to make the currency conversion and follow the prompts. (The currency abbreviation here must be filled in correctly at one time, the number can be filled in incorrectly, the system will ask repeatedly until the input format is correct, but the currency abbreviation is not good, which will lead to program errors)
After the record is entered, the user can choose to continue to enter more records or end the record.
Users can also choose to view the total amount of the category; Delete records for a specific date range; Display all records; Update the total amount of the category; Get a financial summary and save the records to a file.

Command line parameter
If an additional command line argument is provided when you run the program, such as python Finalsgu.py "Welcome to Financial Manager", it is displayed as a welcome message.

Matters needing attention
When entering a date, follow the format YYYY-MM-DD. (2023-12-15)
Make sure you use the correct format when entering the amount (e.g. 123.45).


3. Dependence
This project relies on 'converter.py' for currency conversion functionality. Can be found in the [here] (https://github.com/MicroPyramid/forex-python) related to the original file and detailed information.
Python 3.x
BeautifulSoup4
forex-python


4. Contribute
Welcome to contribute code! fork the repository first and then submit the pull request.

5. License
This project is released under the MIT license.

6. Contact information
For any questions, please contact gsh1422646090@gmail.com.

7.Repo link: https://github.com/Caseroutlaw/inst126finalproject


