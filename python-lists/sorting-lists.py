cars = ["toyota", "ford", "mercedes", "range rover", "Porsche", "Nissan", "suzuki", "Tesla"]
marks = [23, 28, 65, 87, 96,88, 45,54,34,54,67]

# SORTING IN ASCENDING ORDER
cars.sort()
print(cars)

# SORTING IN DESCENDING ORDER
cars.sort(reverse = True)
print(cars)

# SORTING INTEGERS IN ASCENDING ORDER
marks.sort()
print(marks)

# SORTING INTEGERS IN DESCENDING ORDER
marks.sort(reverse = True)
print(marks)

# CASE INSENSITIVE SORT
cars.sort(key = str.lower)
print(cars)

# REVERSE ORDER
cars.reverse()
print(cars)