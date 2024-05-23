################################
# Name: Chimi Gyeltshen
# Deparment: Electrical Deparment
# STudent ID no: 02230060
################################
# REFERENCES
# https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
# https://youtu.be/yMvBSriP8MM?si=4JUwMwhT8hycgdNF
################################

import random

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number  # Set the account number
        self.balance = balance  # Set the account balance to it
        self.account_type = account_type  # Set the account type.

    def deposit(self, amount):
        self.balance += amount  #deposited amount is added to the balance.
        return self.balance  # Given updated balance

    def withdraw(self, amount):
        if amount <= self.balance:  # Verify if the withdrawal amount is the same as or less than the balance.
            self.balance -= amount  # Take that money out of your balance.
            return self.balance  # Given updated balance
        else:
            return "Insufficient funds"  # If the withdrawal amount surpasses the balance, than return message.

class PersonalAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Personal")  # creating for personal account type

class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance, "Business")  # creating for business account type

class Bank:
    def __init__(self):
        self.accounts = {}  # an empty dictionary is created to store accounts

    def create_account(self, account_type):
        account_number = random.randint(10000, 99999)  # a random account number is generated
        balance = 0  # set the balance to 0
        if account_type.lower() == "personal":
            account = PersonalAccount(account_number, balance)  #Make an object for your personal account.
        elif account_type.lower() == "business":
            account = BusinessAccount(account_number, balance)  # make an object for your business account.
        else:
            return "Invalid account type"  # Message returned for an invalid account type
        
        with open("accounts.txt", "a") as file:
            file.write(f"{account_number},{account_type},{balance}\n")  # Put account information in the file.
        
        self.accounts[account_number] = account  # Include account information in the dictionary
        return account_number  # Account number generated in return

    def login(self, account_number):
        with open("accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if int(data[0]) == account_number:
                    account_type = data[1]
                    balance = float(data[2])
                    if account_type == "Personal":
                        return PersonalAccount(account_number, balance)  #Bring back the personal account object.
                    elif account_type == "Business":
                        return BusinessAccount(account_number, balance)  #bring back the business account object
                    else:
                        return None  # If the account type is unknown, return None.


    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)  # Amount deposited into the account
        else:
            return "Account not found"  # If there is no account, a message is returned.

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)  # Take money out of the account
            
        else:
            return "Account not found"  # If there is no account, a message is returned.
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]  # Remove the account from the dictionary.
            with open("accounts.txt", "r") as file:
                lines = file.readlines()  # Read every line in the file.
            with open("accounts.txt", "w") as file:
                for line in lines:
                    if line.split(",")[0] != str(account_number):
                        file.write(line)  # rewrite the file without removing the deleted account
            return "Account deleted"  # Message returned after deletion is successful
        else:
            return "Account not found"  # Message returned if the account cannot be found


def main():
    bank = Bank()  # Make a bank object.
    while True:
        print("\n1. Open Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            account_type = input("Enter account type (Personal/Business): ")
            account_number = bank.create_account(account_type)  # Make a fresh account
            print(f"Account created successfully with number: {account_number}")
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            account = bank.login(account_number)  # Access your current account by logging in.
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Delete Account")
                    print("4. Logout")
                    operation = input("Enter operation choice: ")
                    if operation == "1":
                        amount = float(input("Enter deposit amount: "))
                        print(f"New balance: {bank.deposit(account_number, amount)}")
                    elif operation == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        print(f"New balance: {bank.withdraw(account_number, amount)}")
                    elif operation == "3":
                        print(bank.delete_account(account_number))  # Eliminate the account
                        break
                    elif operation == "4":
                        break
                    else:
                        print("Invalid operation choice.")
            else:
                print("Invalid account number.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
