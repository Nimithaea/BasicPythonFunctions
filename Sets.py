# Exercise 1: Basic Set Operations
set={2,4,5,9,6.5,5,2,0,1,'Nimitha',True,False}
print(set)
print(len(set))
set.add(100)
print(set)
set.discard(9)
print(set)
set.remove(6.5)
print(set)

# Exercise 3: Find the Length of a Set
print(len(set))





# Exercise 2: Clear All Elements
a=set.clear()
print(a)

# Exercise 4: Check if a Set is Empty
set1={100,200,300,500,200}
if(len(set))==0:
    print('The set is Not empty')
else:
    print('The list is empty')

# Exercise 5: Union of Sets
set2={100,200,300,400}
set3={300,400,500,600}
Intersection_set=set2|set3
print('The Union of two sets ', Intersection_set)

# Exercise 8: Symmetric Difference
#symmetric_difference= set2^set3
symmetric_difference1=set2.symmetric_difference(set3)
print('Symmetric Difference - ', symmetric_difference1)

# Exercise 7: Difference of Sets
difference_set=set2-set3
print('The diffence of sets ', difference_set)

# Exercise 9: Find Max and Min
max=max(set2)
print('The Maximun numbner is', max)
print('The minimun number is', min(set2))


# Exercise 10: Sum of Set Elements
sum=sum(set2)
print('The sum is' , sum)

