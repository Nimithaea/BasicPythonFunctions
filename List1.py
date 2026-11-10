a=[10,800,130,40,100,]
#Access the third element of a list
print(a[2])
#List Length: Print the total number of items
print(len(a))
#Check if the list is empty
if len(a)>0:
    print('The list is not empty')
else:
    print('The list is empty')

#Change Element: Change the second element of a list to 200 and print the updated list.
a[1]=200
print(a)

#Append Element: Add 600 o the end of a list and print the new list.
a.append(600)
print(a)

#Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
a.insert(2,300)
print(a)

#Remove Element (by value): Remove 600 from the list and print the list.
a.remove(600)
print(a)

#Remove Element (by index): Remove the element at index 0 from the list print the list.
a.pop(0)
print(a)