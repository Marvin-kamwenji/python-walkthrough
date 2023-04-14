# Creating variables

firstName = "Elizabeth"
lastName = "Muthoni"

print(firstName + " " + lastName)

# CASTING

x = str(3) # This will be '3' 
y = int(3) # This will be 3
z = float(3) # This will be 3.0

# GETTING THE VARIABLE TYPE

age = 50
firstName = "John"
salary = 1234.45

print(type(age))
print(type(firstName))
print(type(salary))

# ASSIGNING MULTIPLE VALUES
firstFruit, secondFruit, thirdFruit = "Bananas", "Straw berries", "Avocados"
print("This is the first value", firstFruit)
print("This is the second value",secondFruit)
print("This is the third value",thirdFruit)

# ONE VALUE TO MULTIPLE VARIABLES
marvinsFruit = brendasFruit = elizabethsFruit = "Mango"

print("Marvin bought a", marvinsFruit)
print("Brenda bought a",brendasFruit)
print("Elizabeth bought a",elizabethsFruit)

# UNPACKING A COLLECTION
fruits = ["Orange", "Watermelon","Banana"]
x, y, z = fruits
print("Fruit x",x)
print("Fruit y", y)
print("Fruit z", z)


# RULES FOR PYTHON VARIABLES

# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores(A-z, 0-9, and _)
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. A variable name cannot be any of the python keywords


# LEGAL VARIABLE NAMES
myVar = "John"
my_var = "John"
_my_var = "John"
myvar = "John"
MYVAR = "John"
myvar2 = "John"

# ILLEGAL VARIABLE NAMES

#1.  2myvar = "John"
#2.  my-var = "John"
#3.  my var = "John"

