##

from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    def checkbalance(self):
        print("You can check out your balance")
    def viewtransaction(self):
        print("You can see your transaction history")

class CurrentAccount(BankAccount):
    def deposit(self):
        print("Any time u can deposit")
    def withdraw(self):
        print("Unlimited withdraw")

class SavingAccount(BankAccount):
    def deposit(self):
        print("Any time u can deposit")
    def withdraw(self):
        print("limited withdraw per month")

class FixedDeposit(BankAccount):
    def deposit(self):
        print("Only one time u can deposit")
    def withdraw(self):
        print("limited withdraw according to the time")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("Only salary u can deposit")
    def withdraw(self):
        print("limited withdraw per month")

class JointAccount(BankAccount):
    def deposit(self):
        print("u can do shared deposit")
    def withdraw(self):
        print("withdraw depends on base type")

class PensionAccount(BankAccount):
    def deposit(self):
        print("only pension deposit")
    def withdraw(self):
        print("limited withdraw per month")

print("Nihitha Current Account")
nihitha= CurrentAccount()
nihitha.deposit()
nihitha.withdraw()
nihitha.checkbalance()
nihitha.viewtransaction()

print("\nKeerthana Saving Account")
Keerthana= SavingAccount()
Keerthana.deposit()
Keerthana.withdraw()
Keerthana.checkbalance()
Keerthana.viewtransaction()

print("\nRamya Fixed Deposit")
Ramya= FixedDeposit()
Ramya.deposit()
Ramya.withdraw()
Ramya.checkbalance()
Ramya.viewtransaction()

print("\nPriyanka Salary Account")
Priyanka= SalaryAccount()
Priyanka.deposit()
Priyanka.withdraw()
Priyanka.checkbalance()
Priyanka.viewtransaction()

print("\nLeorah and Revathi Joint Account")
LR= JointAccount()
LR.deposit()
LR.withdraw()
LR.checkbalance()
LR.viewtransaction()

print("\nAbhinay Pension Account")
Abhinay= PensionAccount()
Abhinay.deposit()
Abhinay.withdraw()
Abhinay.checkbalance()
Abhinay.viewtransaction()