# WAP 2 — Vehicles # Create:
# Car → move() prints "Car is driving"
# Boat → move() prints "Boat is sailing"
# Airplane → move() prints "Airplane is flying"
# Create a list containing all three objects and use a for loop.

# Expected output:
# Car is driving
# Boat is sailing
# Airplane is flying

class Car:
    def move(self):
        print('Car is driving')

class Boat:
    def move(self):
        print('Boat is Sailing')

class Airplane:
    def move(self):
        print('Airplane is flying')

vehicles=[Car(),Boat(),Airplane()]

for i in vehicles:
    i.move()

#WAP — Payment Methods 💳

# Create three classes:
# CreditCard with a method pay()
# UPI with a method pay()
# Cash with a method pay()
# The pay() method should print different messages.

# For example:
# Credit Card → Payment made using Credit Card
# UPI → Payment made using UPI
# Cash → Payment made using Cash

class Creditcard():
    def pay(self):
        print('Payment made using Credit Card')

class UPI():
    def pay(self):
        print('Payment made using UPI')

class Cash():
    def pay(self):
        print('Payment made using Cash')

payments=[Creditcard(),UPI(),Cash()]

for payment in payments:
    payment.pay()


#Create 3 classes:

# Developer
# Tester
# Manager
#realistic by using __init__() so that the salary is passed as an argument, e.g. Developer(80000).

class Developer:
    def __init__(self,salary):
        self.salary=salary

    def show_salary(self):
        print(f'Developer salary is {self.salary}')

class Tester:
    def __init__(self,salary):
        self.salary=salary

    def show_salary(self):
        print(f'Tester salary is {self.salary}')

class Manager:
    def __init__(self,salary):
        self.salary=salary

    def show_salary(self):
        print(f'Manager salary is {self.salary}')

salary=[Developer(5000),Tester(4000),Manager(7000)]

for i in salary:
    i.show_salary()


#Create three classes:

# SavingsAccount
# CurrentAccount
# SalaryAccount

# Each class should have:

# __init__(self, balance) to store the balance.
# A method called show_balance()


class SavingsAccount:
    def __init__(self,balance):
        self.balance=balance

    def show_balance(self):
        print(f'Savings Account Balance is {self.balance}')

class CurrentAccount:
    def __init__(self,balance):
        self.balance=balance

    def show_balance(self):
        print(f'Current Account Balance is {self.balance}')

class SalaryAccount:
    def __init__(self,balance):
        self.balance=balance

    def show_balance(self):
        print(f'Salary Account Balance is {self.balance}')

account = [SavingsAccount(100000),CurrentAccount(35000),SalaryAccount(678900)]

for i in account:
    i.show_balance()