'''Problem Statement

Design and implement a Banking System using Object-Oriented Programming principles.

The banking system should allow customers to create accounts, deposit money, withdraw money, check balances, and manage different account types.

Your implementation should demonstrate the use of:

Classes and Objects
Encapsulation
Inheritance
Polymorphism
Composition
Single Responsibility Principle (SRP)
Requirements
1. Account Class

Create a base class named Account.

Attributes:
account_id
account_holder_name
balance
Methods:
deposit(amount)
withdraw(amount)
check_balance()
Rules:
Deposits must be greater than zero.
Withdrawals must not exceed available balance.
Display appropriate messages for successful and failed transactions.'''

class Account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0 #protected attribute 

    def check_balance(self):
        print(f"Balance: {self._balance}")

    def deposit(self,amount):
        self._balance+=amount
        print(f"Deposit successfull . {self._balance}")

    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"Withdraw successfull . {self._balance}")
        else:
            print("Balance is less")

class SavingsAccount(Account):
    def __init__(self,id,holder_name,interest_rate=0.04):# 4%
        super().__init__(id,holder_name)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        interest=self._balance*self.interest_rate
        print(f"Interest: {interest}")
    
class CurrentAccount(Account):
    def __init__(self,id,holder_name,overdraft_balance=1000):
        super().__init__(id,holder_name)
        self.overdraft_balance=overdraft_balance

    def withdraw(self,amount):
            if self._balance + self.overdraft_balance>=amount:
                self._balance-=amount
                print(f"Withdraw successfull . {self._balance}")
            else:
                print("Ask if it is overdraft")
class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__account={}

    def create_account(self,id,holder_name,type):
        if type=="savings":
            new_account=SavingsAccount(id,holder_name)
        elif type=="current":
            new_account=CurrentAccount(id, holder_name)
        self.__account[id]=new_account
        print("Account creation successful")
        return new_account
    
    def get_account(self,id):
        if id not in self.__account:
            print("Account not found!")
            return None
        else:
            account=self.__account[id]
            print(f"\nID: {account.id}\nHolder name: {account.holder_name}")
            return account
        
karna=Bank("Karnataka Bank of India","Bangalore")
s=karna.create_account("1","Archana","savings")
c=karna.create_account("2","Shreyas","current")
s.deposit(1000)
c.deposit(10)
s.withdraw(2000)
c.withdraw(500)
s.calculate_interest()