
myList = ["apple", "banana", "cherry"]
newList = ["mango", "pineapple", "papaya"]

# ADDING AN ITEM TO THE END OF A LIST
myList.append("orange")
print(myList)

# TO INSERT AT A SPECIFIED INDEX
myList.insert(1, "strawberry")
print(myList)

# APPEND ELEMENTS FROM ANOTHER LIST
myList.extend(newList)
print(myList)