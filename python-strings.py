# ACCESSING CHARACTERS IN A STRING
a = "Hello, World!"
print(a[1])

# LOOPING THROUGH A STRING
for x in "bananas":
    print(x)

# CHECKING LENGTH OF STRING
a = "Hello, World!"
print("This will print the length of string a",len(a))

# CHECK STRING
txt = "The best things in life are free!"
if("free" in txt):
    print("Yes 'free' is inside txt")

# CHECK IF NOT
if("expensive" not in txt):
    print("No, 'expensive' is NOT present")

# SLICING STRINGS
print(a[2:5])

# SLICING STRINGS FROM THE START
print(a[:7])

# SLICING TO THE END
print(a[6:])

# NEGATIVE INDEXING
print(a[-6:-1])


# MODIFY TO UPPERCASE
print(a.upper())

# MODIFY TO LOWERCASE
print(a.lower())

# REMOVE WHITESPACE
b = " Hello, World! "
print(b.strip())  #returns "Hello, World!"


# REPLACE STRING
print(a.replace("H", "J"))