# Collections are data types used to store multiple values in a single variable.
name1 = "Akash"
name2 = "Sai"
name3 = "Vishal"

# We can store all values together:

names =["Akash","Sai","Vishal"]
# Types of Collections in Python
# List
# Tuple
# Set
# Dictionary
# String (also behaves like a collection)
# 1. List in Python

# A List stores multiple items in a single variable.

# ----->>>>Features of List
# Ordered
# Mutable (can change)
# Allows duplicates
# Uses square brackets []

numbers = [10,20,30,40,50]
print(numbers)

# List Indexing
# Each element has an index position.

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# Negative Indexing

print(numbers[-2])

# List Slicing

numbers = [10, 20, 30, 40, 50,60]

print(numbers[1:4])

numbers = [10, 20, 30, 40, 50,60]

numbers[1] =100

print(numbers)

# append()
# Adds element at end.

numbers.append(90)
print(numbers)

# insert()

numbers.insert(1000,20000)
print(numbers)


numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)

numbers = [10, 20, 30]

numbers.pop()
print(numbers)

numbers = [5, 2, 1, 4]

numbers.sort()
print(numbers)

numbers = [10, 20, 30]

for num in numbers:
    print(num)
    
    
# Tuple in Python

# Tuple is similar to List but:

# Immutable (cannot change)
# Ordered
# Allows duplicates
# Uses parentheses ()

# Tuple Cannot Be Modified
numbers = (10, 20, 30)

# numbers[1] = 200

# Tuple Methods

# Only two major methods:

numbers = (1, 2, 2, 3)

print(numbers.count(2))

numbers = (10, 20, 30)

print(numbers.index(20))