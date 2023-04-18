myList = ['apple', 'strawberry', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

# REMOVE SPECIFIC ITEM
myList.remove("cherry")
print(myList)

# REMOVE SPECIFIED INDEX
myList.pop(1)
print(myList)

del myList[2]
print(myList)

# REMOVE LAST ELEMENT
myList.pop()
print(myList)

# CLEAR THE LIST
myList.clear()
print(myList)

# DELETE THE ENTIRE LIST
del myList
print(myList)