'''a=100
if a>=100:
    print('A is greater than or equal to 100')
else:
    print('A is lesser than 100')'''



# age=20
# if age>=18:
#     print('You are eligible for voting')
# else:
#     print('You are not eligible for voting')

# age=20
# if age>=21:
#     print('You are eligible to participate in election')
# else:
#     print('You are not eligible to participate in election')


age=int(input('Enter the age')) #Typecasting
if age>=21:
    print('You are eligible for voting and participating in election')
elif age>18 and age<=21:
    print('You are eligible for voting but not eligible to paricipate in election')
else:
    print('You are not eligible for voting')