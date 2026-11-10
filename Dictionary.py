# Exercise 1: Basic Dictionary Operations
a={'name':'Nimitha','age':35,'location':'Germany'}
print(a)
a['occupation']='Tester'
print(a)
print(a['name'])
del a['age']
print(a)


# Exercise 2: Dictionary Operations
print(len(a))

# Exercise 3: Dictionary from Two Lists
names=['Nim','Suji','Devu','Ishaan']
age=[37,40,11,3]
dic1=dict(zip(names,age))
print('The new dictionary : ',dic1)

# Exercise 4: Clear Dictionary
# dic1.clear()
# print('The dictionary after clearing :', dic1)

# Exercise 5: Merge Dictionaries
dic2={'City':'Hamburg','Country':'Germany'}
dic3=dic1| dic2
print('Merged Dictionary :', dic3)

dic4={**dic1,**dic2} #--merge dictionary
print(dic4)

# Exercise 6: Access Nested Dictionary
person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
print(person['name'])
print(person['address']['city'])


# Exercise 7: Access ‘history’ Key From a Nested Dictionary
# Exercise 8: Initialize Dictionary with Default Values




# Exercise 9: Rename a Key of Dictionary
new_dic={'name':'A','age':10,'location':'B'}
new_dic['location']=new_dic['Country']

# Exercise 10: Delete a List of Keysf