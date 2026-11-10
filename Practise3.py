# def greet():
#     print('Hello Students')
# #greet()

# def Welcome():
#     print('Welcome to python Class')
# Welcome()
# greet()

# def greet(name):
#     print('Hello', name)
# greet('Nimitha')

#Create a function called square() that: takes one number as a parameter prints its square

# num=int(input('Enter the number '))
# def square(num):
#     print('Square of the given number is ' , num*num)
# square(num)

# Create a function called add() that: takes two numbers as parameters prints their sum

# num1=int(input('Enter the number1 : '))
# num2=int(input('Enter the number2 : '))
# def add(num1,num2):
#     print('The sum of given two numbers is ' , num1+num2 )
# add(num1,num2)

# Create a function multiply() that:

# takes two numbers
# returns their multiplication
# store the returned value in a variable
# print the variable

# num1=int(input('Enter the number1 : '))
# num2=int(input('Enter the number2 : '))
# def multiply(num1,num2):
#    return num1 * num2
# result=multiply(num1,num2)
# print(result)

# Create a function called subtract() that:

# takes two numbers
# returns their difference
# stores the result in a variable
# prints the result

# num1=int(input('Enter the number1 : '))
# num2=int(input('Enter the number2 : '))
# def subtract(num1,num2):
#    return num1 - num2
# difference = subtract(num1,num2)
# print ('The difference of given two number is : ', difference)

# Create a function called check_number() that takes one number and:
# If the number is positive → return "Positive"
# If the number is negative → return "Negative"
# If the number is zero → return "Zero"

# num=int(input('Enter the number : '))
# def check(num):
#    if num>0:
#       return 'The given Number is Positive'
#    elif num<0:
#       return 'The given number is Negativ'
#    else:
#       return 'The given number is Zero'
# result= check(num)
# print(result)

# Create a function called even_odd() that:
# takes one number
# returns "Even" if the number is even
# returns "Odd" if the number is odd
# store the result in a variable
# print the result

# num = int(input('Enter the number : '))
# def even_odd(num):
#    if num%2==0:
#       return 'The given number is even'
#    else:
#       return 'The given number is odd'
# result=even_odd(num)
# print(result)

# def greet(name='User'):
#    print('Hello ' , name)
# greet('Nimitha')
# greet()

# def greet(name='Guest'):
#    print ('Hello ',name)
# greet()
# greet('Sujith')


# Create a function called employee() with 3 parameters:

# name
# age
# department

# It should print all three.

# def employee(name,age,dept):
#     print('Name :',name)
#     print('Age:',age)
#     print('Department :',dept)
# employee('Nimitha',30,'Testing')


# def sum_numbers(*numbers):
#     total=0
#     for i in numbers:
#      total=total+i
#     return total
# result=sum_numbers(25,25,100)
# print(result)


# Create a function called find_largest() that:
# accepts any number of numbers using *args
# finds the largest number using a for loop
# returns the largest number
# prints the result
 
def find_largest(*num):
    largest=0
    for i in num:
        
        if largest<i:
            largest=i
    return largest    
        
large= find_largest(10,30,25,100,50)
print('the largest is', large )
