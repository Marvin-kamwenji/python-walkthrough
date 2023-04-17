# SINCE WE CANNOT CONCATENATE STRINGS AND INTEGERS
# PYTHON USES THE FORMAT METHOD TO HELP US ACHIEVE THAT

# SIMPLE EXAMPLE
age = 35
text = "Hey my name is christine, and I am {} years old"
print(text.format(age))

# USING MULTIPLE ARGUMENTS
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# USING INDEXES
myneworder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myneworder.format(quantity, itemno, price))