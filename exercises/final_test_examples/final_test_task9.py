import random

class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def account_info(self):
        return f"Account number:{self.account_number} Holder:{self.holder_name} Balance:{self.balance}"

    def __repr__(self):
        return self.account_info()

    def change_bal(self):
        self.balance = float(input("Enter your current balance: "))

# creating a list with all the bank accounts
accounts_list = []
for x in range(2):
    acc = BankAccount(account_number=random.randint(0,100), holder_name=str(input("Enter your name: ")), balance=0)
    acc.change_bal()
    accounts_list.append(acc)
    

def deposit(accounts_list = accounts_list, num = int(input("Enter the account number: ")), amount = float(input("Enter the sum for deposit"))):
    for a in accounts_list:
        if a.account_number == num:
            a.balance += amount
        else:
            print("Wrong account number!")


def withdraw(accounts_list = accounts_list, num = int(input("Enter the account number: ")), amount = float(input("Enter the sum for deposit"))):
    for a in accounts_list:
        if a.account_number == num:
            if a.balance >= amount:
                a.balance -= amount
            else: 
                print("Insuficient availability")
        else:
            print("Wrong account number!")

def get_balance(accounts_list = accounts_list, num = int(input("Enter the account number: "))):
    for a in accounts_list:
        if a.account_number == num:
            print(a.balance)
        else:
            print("Wrong account number!")

def change_name(accounts_list = accounts_list, num = int(input("Enter the account number: ")), name = str(input("Change your name to: "))):
    for a in accounts_list:
        if a.account_number == num:
            a.holder_name = name
            a.account_info()
        else:
            print("Wrong account number!")