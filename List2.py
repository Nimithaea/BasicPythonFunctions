# Exercise 5. Calculate the Product of All Elements
a=[25,100,75,45,10]
product=1
for i in a:
    product=i*product
print('Product of All Element is :',product)

# Exercise 6. Count Even and Odd Numbers
even=0
odd=0
for i in a:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print('Even Numbers:' , even)
print('Odd Numbers:',odd)

# Exercise 7. Reverse a List 
a.reverse()
print('Reverse List is - ', a)
#Exercise 8. Sort a List of Numbers
a.sort()
print('The sorted list is - ',a)
# Exercise 9. Create a Copy of a List
b= a.copy()
print('List Copy :',b)
# Exercise 10. Combine Two Lists
c = a + b
print('The combined List is',c)

