# def f1(a,b):
#     print('Nimitha')
#     print('SUM', a+b)
# f1(5,5)

#WAP to define a function for sum, difference, multiplication and division

# def F1(a,b):
#     print('SUM :', a+b)
#     print('Difference :', a-b)
#     print('Multiplication :', a*b)
#     print('Division :',a/b)
# F1(15,5)

# # WAP to print the even number from a range by defining functions
# def evennum():
#    num = int(input('Enter the Range : '))
#    for i in range(num):
#      if i%2 == 0:
#       print(i)
# evennum()

# 1. Write a Python function to find the maximum of three numbers.
def max(a,b,c):
   if a>b & a>c:
      print('The Maximun is',a)
   elif b>c & b>a:
      print('The Maximun is',b)
   else:
      print('The Maximun is',c)
max(200,100,50)
      
# 2. Write a Python function to sum all the numbers in a list.
num=[10,20,30,40,50]
def sum_list():
   sum=0
   for i in num:
    sum=sum+i
   print('Sum of All Element is :',sum)
sum_list()


# 3. Write a Python function to multiply all the numbers in a list.
def prd_list():
   prd=1
   for i in num:
    prd=prd*i
   print('Product of All Element is :',prd)
prd_list() 
   

# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial is:", fact)
factorial(8)



# 5. Write a Python program to print the even numbers from a given list.
list2=[2,5,10,15,20,25]
def evennum1():
   for i in list2:
      if i%2==0:
         print(i)

evennum1()