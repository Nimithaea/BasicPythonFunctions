# i=10
# while i<=25:
#     print(i, end=' ')
#     i = i+2

# Exercise 1: Print first 10 natural numbers using while loop
# Exercise 2: Calculate sum of all numbers from 1 to a given number
# Exercise 3: Print multiplication table of a given number
# Exercise 4: Count the total number of digits in a number

# Exercise 1: Print first 10 natural numbers using while loop

# i=1
# while i<=10:
#     print(i ,end=' ')
#     i=i+1

# Exercise 2: Calculate sum of all numbers from 1 to a given number

# i = 1
# num = int(input('Enter the number :'))
# sum = 0
# while i<=num:
#     sum = sum + i
#     i = i + 1
# print('The sum is : ', sum)



# Exercise 3: Print multiplication table of a given number

# num = int(input('Enter the number :'))
# i = 1
# while i<=10:
#     print (i*num , end= ' ')
#     i = i+1


# Exercise 4: Count the total number of digits in a number

num = int(input('Enter the number :'))
count = 0
while num != 0:
    num = num//10
    count = count + 1
print('Count of the total number of digits is : ', count)
