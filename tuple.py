#Purpose: This exercise introduces you to the fundamental building blocks of working with tuples: 
# creating them, retrieving individual elements using index positions, 

# a=(5,10,15.5,'Nimitha',True)
# b=10,
# print(a)
# print(type(a))
# print(type(b))
# print(a[2])
# print(a[0:3])
# print(a[:1:-1])
# print(len(a))


#Exercise 1: Basic Tuple Operations
a=(5,10,15.5,'Nimitha',True)
b=10,
print(a)
print(type(a))
print(type(b))
print(a[2])
print(a[0:3])
print(a[:1:-1])
print(len(a))


# Exercise 2: The Trailing Comma
b=(100,)
print(b)
print(type(b))

# Exercise 3: Tuple Repetition
c=(150,200,300,100,500)
print(c*2)


# Exercise 4: Tuple Concatenation
d=b+c
print(d)

# Exercise 5: Tuple Slicing
print(c[2])
print(c[0:3])
print(c[:1:-1])

# Exercise 6: Tuple Reversal
print(c[::-1])

# Exercise 7: Counting
print(len(c))

# Exercise 8: Tuple Unpacking
e,f,g,h,i=c
print(e)
print(f)


# Exercise 9: The Swap Trick
swap1=(100,200,300)
swap2=(650,750,850)
swap1,swap2=swap2,swap1
print('Swap1 - ', swap1)
print('Swap2 - ',swap2)

# Exercise 10: Nested Tuple Access
nested=(5,6,8,"Rishi",True,(9,7,8,"Rishi",(1,1,1.6,"Rishi",True),True))
print(nested[5][1])
print(nested[5][4][3])
print(nested[5][4][4])





