# Tuples in Python

# A Tuple is a collection data type used to store multiple values in a single variable.
# Ordered 
# Immutable (cannot be changed after creation) 
# Allows duplicate values 
# Can store different data types 

# 1. Creating a Tuple
# Single Element Tuple

t = (10,)
i = (10)
print(type(i))
print(t)
print(type(t))

# Multiple Elements Tuple
t = (10, 20, 30, 40)
print(t)


# Tuple Without Parentheses

t = 10, 20, 30
print(t)
print(type(t))

# 2. Why Use Tuples?
# Tuples are used when data should not change.
# Examples:
# Coordinates (10, 20)
# RGB Colors (255, 0, 0)
# Employee Record IDs
# Database Query Results

# 3. Accessing Tuple Elements
# Positive Indexing

t = ("Apple", "Banana", "Orange")

print(t[0])
print(t[1])
print(t[2])

# Negative Indexing
print(t[-1])
print(t[-2])

# 4. Tuple Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])
print(t[2:4])
print(t[::-1])

# 5. Tuple is Immutable
# You cannot modify tuple elements.
t = (10, 20, 30)
# t[0] =100

# 6. Tuple Packing
# Putting multiple values into a tuple.
t=10,20,30
print(t)

# 7. Tuple Unpacking
# Extracting values from a tuple.
t = (10, 20, 30)
a,b,c =t
print(a)
print(b)
print(c)

employee = ("Akash", 101, "Developer")
name ,emp_id,designation = employee
print(name)
print(emp_id)
print(designation)
# 8. Tuple Methods
# Tuple has only 2 methods.
# count()
# Returns number of occurrences.

t = (10, 20, 10, 30, 10)
print(t.count(10))

# index()
# Returns position of element.
t = (10, 20, 10, 30, 10)

print(t.index(20))

# 9. Built-in Functions with Tuple
t = (10, 20, 30, 40)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))

# 10. Iterating Through Tuple

t = ("Java", "Python", "NodeJS")
for tech in t:
    print(tech)
    
    # Using While Loop
    
    i=0
    while i<len(t):
        print(t)
        i =i+1
        
        
# 12. Converting List to Tuple

num = [10,202,30,40]
data = tuple(num)
print(data)
# 13. Converting Tuple to List
t=(10, 202, 30, 40)
l=list(t)
print(l)