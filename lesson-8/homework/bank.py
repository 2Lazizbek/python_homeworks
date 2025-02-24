from random import randint
import csv

filename = "bank_records.csv"

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number  # Unique account identifier
        self.name = name  # Account holder's name
        self.balance = balance  # Current account balance

class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store all accounts
        self.load_from_file()  # Load existing accounts from file
    
    def load_from_file(self):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                # Load accounts from CSV into dictionary
                self.accounts = {int(account_num): Account(int(account_num), name, float(balance)) for account_num, name, balance in reader}
        except FileNotFoundError:
            print("File not found! There are no account data.")
            self.accounts = {}

    def save_to_file(self):
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            # Save all accounts to CSV file
            writer.writerows([[value.account_number, value.name, value.balance] for value in self.accounts.values()])

    def output_menu(self):
        # Display the main menu options
        print("""------------------
1. Create account
2. View account
3. Deposit
4. Withdraw
5. Save changes
------------------
""")
    
    def get_amount(self, purpose):
        while True:
            try:
                amount = float(input(f"Enter the amount for {purpose}: "))
                if amount <= 0:
                    raise ValueError("Enter positive amount.")
                if amount >= 100000:
                    raise ValueError("Given amount exceeds the maximum amount for single transaction.")
                break
            except ValueError as e:
                print(e)
        return amount  # Return validated amount

    def create_account(self, name, initial_deposit):
        account_number = randint(1000, 9999)  # Generate a random 4-digit account number
        while account_number in self.accounts.keys():
            account_number = randint(1000, 9999)  # Ensure the account number is unique
        user = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = user  # Add new account to dictionary
        with open(filename, "a", newline='') as file:
            csv.writer(file).writerow([account_number, name, initial_deposit])  # Append new account to CSV

    def view_account(self, account_number):
        if account_number in self.accounts:
            # Display account details
            print(f"Account number: {account_number}\nName: {self.accounts[account_number].name}\nBalance: {self.accounts[account_number].balance}")
        else:
            print("Account with this account number doesn't exist in database.")

    def deposit(self, account_number, amount):
        self.accounts[account_number].balance += amount  # Update account balance
        print(f"${amount} has been deposited to your account.")

    def withdraw(self, account_number, amount):
        if amount > self.accounts[account_number].balance:
            print("Insufficient balance.")
        else:
            self.accounts[account_number].balance -= amount  # Update account balance
            print(f"${amount} has been withdrawn from your account.")
    
    def input_account_number(self):
        while True:
            try:
                account_num = int(input("Enter your account number: "))
                if account_num not in self.accounts:
                    raise ValueError("Account number doesn't exist.")
                if not (1000 <= account_num <= 9999):
                    raise ValueError("Account number should be a 4-digit integer.")
                break
            except ValueError as e:
                print(e)
        return account_num  # Return validated account number

def menu():
    mybank = Bank()  # Initialize the bank system
    while True:
        mybank.output_menu()  # Display menu
        while True:
            try:
                choice = int(input("--->"))
                if not (1 <= choice <= 5):
                    raise ValueError("Input integer between 1 and 5.")
                break
            except ValueError as e:
                print(e)
        if choice == 1:
            name = input("Enter your name: ")
            while len(name) > 50 or any(name == value.name for value in mybank.accounts.values()):
                if len(name) > 50:
                    print("Name is too long. Maximum 50 characters.")
                else:
                    print("Name is already taken.")
                name = input("Enter your name: ")
            amount = mybank.get_amount("deposit")
            mybank.create_account(name, amount)  # Create a new account
            
        elif choice == 2:
            account_number = mybank.input_account_number()
            mybank.view_account(account_number)  # View account details

        elif choice == 3:
            account_number = mybank.input_account_number()
            amount = mybank.get_amount("deposit")
            mybank.deposit(account_number, amount)  # Deposit funds
            
        elif choice == 4:
            account_number = mybank.input_account_number()
            amount = mybank.get_amount("withdrawal")
            mybank.withdraw(account_number, amount)  # Withdraw funds
        elif choice == 5:
            mybank.save_to_file()  # Save changes to file
        else:
            print("Invalid input.")

menu()  # Start the program