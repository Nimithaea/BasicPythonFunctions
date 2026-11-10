# #Create a Student class with:
# name
# age
# marks
# Create a show() method that prints:
# Name: Nimitha
# Age: 37
# Marks: 85

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def result(self):
        if self.marks>=40 :
            print('Passed')
        else:
            print('Failed')


    def show(self):
        print('Name of the student: ', self.name)
        print('Age of the student: ', self.age)
        print('Mark of the student: ', self.marks)
       
student1 = Student('Nimitha', 35, 95)
student2 = Student('Shanaya', 11, 25)
student1.show()
student1.result()
student2.show()
student2.result()

#   print(f'{self.name} is {self.age} years old and studies in Grade {self.grade} at {self.school}')

# #Create a class BankAccount.
# Constructor should take name and balance.
# Store them using self.
# Create a method display() that prints the account holder and balance.
# Create two different bank account objects.

# class Bank_account:
#     def __init__(self,name,balance,dep,withd):
#         self.name=name
#         self.balance=balance
#         self.dep=dep
#         self.withd=withd
#     # def deposit(self, dep):
#     #     self.dep=dep
#     # def withdrawal(self,withd):
#     #     self.withd=withd
#     def final_balance(self):
#         remaining_balance=self.balance+self.dep-self.withd
#         print(f'The remaining balance is {remaining_balance}')
#     def show(self):
#             print(f'Account Holder Name: {self.name} ')
#             print(f' Current Balance : {self.balance}')
#             print(f'Deposit Amount : {self.dep}')
#             print(f'Withdrawal amount : {self.withd}')
            

# acc_details=Bank_account('Nimitha', 5000,2000,500)
# acc_details.show()
# acc_details.final_balance()

class Account:
    def __init__(self, name,balance):
        self.name=name
        self.balance=balance
    def show(self):
        print(f'The account holder name is : {self.name}')
        print(f'Current Account Balance : {self.balance}')

    def Deposit(self,amount):
        self.balance=amount+self.balance
        print(f'Deposit Amount : ',amount)
        print(f'The current balance amount is :{self.balance}')

    def Withdrawal(self,withdraw):
        self.balance=self.balance-withdraw
        if self.balance>withdraw:
            print(f'the withdrawal Amount is:', withdraw)
            print(f'the current balance is : {self.balance}')
        else:
            print('Insufficient Balance to withdraw from your account')
        

account=Account('Nimitha',10000)
account.show()
account.Deposit(5000)
account.Withdrawal(22500)





#######WAP: Shopping Cart
# Constructor

# The constructor should take:

# customer_name
# total_amount
# Methods

# 1. show()
# Print the customer name and current cart total.

# 2. add_item(amount)
# Add the item price to the current total.

# 3. remove_item(amount)
# Remove the amount from the current total, but only if the amount is not greater than the current total.

# 4. final_amount()
# Print the final cart amount.

class Shopping_Cart:

    def __init__(self,cust_name,tot_amt):
        self.cust_name = cust_name
        self.tot_amt = tot_amt

    def show(self):
        print(' ***** SHOPPING CART PROGRAM ******')
        print(f'Customer name : {self.cust_name}')
        print(f'Total Amount : {self.tot_amt}')

    def add_item(self,item_amt):
        self.tot_amt = self.tot_amt+ item_amt
        print(f'the total item price after adding article is : {self.tot_amt}')

    def remove_item(self,rmv_item):
        if self.tot_amt > rmv_item:
            self.tot_amt = self.tot_amt - rmv_item
            print(f'The total item price after removing article is : {self.tot_amt}')
        else:
            print('Item removal is not possible')

    def final_amt(self):
        print(f'The final amount is : {self.tot_amt}')

    def discount(self):
        discount_amt=0

        if self.tot_amt >= 2000:
            discount_amt = self.tot_amt * 0.20
            self.tot_amt = self.tot_amt - discount_amt
            print(f'The discount amount is : {discount_amt}')
            print(f'The total amount after discount is : {self.tot_amt}')

        elif self.tot_amt >= 1000:
                        discount_amt = self.tot_amt * 0.10
                        self.tot_amt = self.tot_amt - discount_amt
                        print(f'The discount amount is : {discount_amt}')
                        print(f'The total amount after discount is : {self.tot_amt}')

        else:
            print('No discount as the total value is less than 1000')

shopping_cart=Shopping_Cart('Nimitha',2000)
shopping_cart.show()
shopping_cart.add_item(1000)
shopping_cart.remove_item(500)
shopping_cart.discount()
shopping_cart.final_amt()