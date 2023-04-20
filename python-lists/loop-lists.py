
myList = ["apple", "banana", "carrot", "mango", "strawberry", "watermelon"]

# LOOP THROUGH LISTS
for list in myList:
    print(list)

# LOOP THROUGH THE INDEX NUMBERS
for list in range(len(myList)):
    print(myList[list])

# USING A WHILE LOOP
i = 0
while i < len(myList):
    print(myList[i])
    i= i + 1

# LOOPING USING LIST COMPREHENSION
[print(x) for x in myList]