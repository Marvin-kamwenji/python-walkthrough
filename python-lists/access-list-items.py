# DECLARING LIST ITEMS
myList = ["apple", "banana", "cherry"]

# USING CONSTRUCTOR
theList = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))

# PRINTING THE SECOND ITEM OF MYLIST
print(myList[1])

# PRINTING THE LAST ITEM OF THELIST
print(theList[-1])

# RETURNING THE THIRD, FORTH AND FIVE ITEMS IN THELIST
print(theList[2:5])

# RETURNING ITEMS FROM THE BEGINNING TO SPECIFIED INDEX
print(theList[:4])

# RETURNING ITEMS FROM A CERTAIN INDEX TO THE END
print(theList[2:])

# CHECK IF ITEM EXISTS IN THE LIST
if "apple" in theList:
    print("Yes, Apple is in the list")