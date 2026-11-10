# a=int(input('Enter the number to check even or odd - '))
# if a%2==0:
#     print('The number is even')
# else:
#     print('The number is odd')


# a=int(input('Enter 1st number'))
# b=int(input('Enter 2nd number'))
# sum = a+b
# sub = a-b
# mul = a*b
# div = a/b
# print('Addition =', sum)
# print('substraction =', sub)
# print('Multiplication =', mul)
# print('Division=', div)


# a=int(input('Enter 1st number - '))
# b=int(input('Enter 2nd number - '))
# print('Addition =', a+b)
# print('substraction =', a-b)
# print('Multiplication =', a*b)
# print('Division=', a/b)


# a=int(input('Enter the number - '))
# print(('The square of the number is'), a*a)
# print(('The cube of the number is'), a*a*a)
# print(('Remainder when divided by 2 is'),a%2)



# mark=int(input('Enter the marks - '))
# if mark >= 95:
#     print('The Grade is A+')
# elif mark >= 90:
#      print('The Grade is A')
# elif mark >= 80:
#       print('The Grade is B')
# elif mark >= 70:
#       print('The Grade is C')
# elif mark <= 60 and mark >= 40:
#       print('The Grade is D')
# else:
#       print('You failed')


# username = input('Enter Username :')
# pwd = input('Enter Password : ')

# if username =='admin' and pwd =='12345':
#     print ('You have logged in successfully')
# else:
#     print('Invalid Username and Password')



# a = int(input('Enter 1st number : '))
# b = int(input('Enter 2nd number : '))
# if a>b:
#     print( a, 'is greater')
# else:
#     print( b, 'is greater ')


# temp = int(input('Enter the temperature : '))
# if temp>30:
#     print('It is hot')
# elif temp<30 and temp>20 :
#     print('It is Warm')
# else:
#     print('It is cold')


# pwd = input('Enter the Password : ')
# if pwd == 'AdminUser':
#     print('You logged in successfully')
# else :
#     print('Incorrect Password')



# num = int(input('Enter the number to check if divisible by 5 : '))
# if num%5==0 :
#     print('The number is divisible by 5')
# else:
#     print('The number is not divisible by 5')


# bal = int(input('Enter the Balance amount : '))
# amt = int(input('Enter the withdrawal amount : '))
# if amt > bal :
#     print('Insufficient Balance')
# if amt <= bal :
#     print('Withdrawal successful, Remaining Balance is ', bal-amt)
# if amt <= 0:
#     print('Invalid amount')


# i=1
# while i<5:
#     print(i)
#     i=i+1

# i=0
# while i<100:
#     print( i)
#     i = i +2


# i=10
# while i>0:
#     print(i)
#     i = i-1
# print('Done')

# password = ""

# while password != "python123":
#     password = input("Enter password: ")

# print("Access granted!")

# num=0
# while num<=10:
#     print(num)
#     # num=num+2

# Exercise 1: Print first 10 natural numbers using for loop
# Exercise 2: Calculate sum of all numbers from 1 to a given number
# Exercise 3: Print multiplication table of a given number
# Exercise 4: Display a message “Done” after the successful execution of the for loop
# Exercise 5: Display numbers from -10 to -1 using for loop


# i=1
# while i<=10:
#     print(i)
#     # i = i+1

# num=int(input('Enter the num : '))
# i=1
# sum=0
# while i <= num:
#     sum = sum + i
#     i= i+1
# print(sum)

# num=int(input('Enter the num : '))
# i = 1
# while i<=10:
#     print(num * i)
#     i = i +1
    
# i = -10
# while i <= -1:
#     print(i)
#     i = i+1

#WAP to create a list of 5 numbers and print the list.
# i =  [1,2,3,4,5]
# print(i)

#WAP to create a list of 5 fruits and print the first fruit.
fruits = ['apple' , 'Banana' , 'Cherry' , 'Mango' , 'Kiwi']
print(fruits[0])
fruits.append("Grapes")
print(fruits)