a=lambda x,y,z: print(x+y+z)
a(10,20,30)

#Write a Python program to square and cube every number in a given list of integers using Lambda
num=[1,2,3,4,5]
sqr=list(map(lambda x: x**2,num))
print('Square: ', sqr)
cube=list(map(lambda y:y**3,num))
print('Cube: ',cube)

#Write a Python program to count the even and odd numbers in a given list of integers using Lambda.
numbers=[20,45,78,30,33,79,1]
count=0
even=len(list(filter(lambda x:x%2==0,numbers)))
odd=len(list(filter(lambda x:x%2!=0,numbers)))
print('even number count :',even)
print('Odd number count :',odd)

#Write a Python program to add two given lists using map and lambda.
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
add_list=list(map(lambda x,y: x+y,list1,list2))
print('Add list :', add_list)

#Write a Python program to sort tuples using Lambda.
tup=(700,100,50,500,250,1000.25)
tup_list=list(tup)
sorting=sorted(tup_list, key=lambda x:x)
print(tuple(sorting),' - Sorted tuple')