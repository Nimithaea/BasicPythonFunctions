# a=[10,10.5,20,'Nimitha',True]
# print(a)
# print(a[2])
# print(a[3][2])
# a[1]=15
# print(a)
# print(a[2]) #'Access the third element of a list' 
# print(len(a)) #List Length: Print the total number of item
# #Check if the list is empty
# if len(a)==0:
#     print('The list is empty')
# else:
#     print('The list is not empty')

# #Exercise 1. Perform Basic List Operations
a=[10,20,25.5,30,'Nimitha',True]
print(a)
print(a[2])
print(a[4][2])
print(len(a))

#Exercise 2. Perform List Manipulation
a.append(25)
print(a)

# #Exercise 3. Sum and Average of All Numbers in a List
b=[100,200,500,150]
print(b)
print('The sum of the numbers = ',sum(b))
print('The average of the numbers = ',sum(b)/len(b))

#Exercise 4. Find Maximum and Minimum from List
c=[100,200,500,150,75]
max=0
for i in c:
    if i>max:
        max=i
print('The Maximum number is ' ,max)
min=c[0]
for i in c:
    if i<min:
        min=i
print ('The minimum number is ' , min)