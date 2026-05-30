# Sets in Python
# A Set is a collection of unique elements.
# Unordered (no indexing)
# Mutable (can add/remove elements)
# Does not allow duplicates
# Defined using {} or set()

# Creating a Set

numbers ={10,20,30,40}
print(numbers)
# output :{40, 10, 20, 30}
# Order may vary because sets are unordered.
# Duplicate Values Not Allowed

numbers = {10, 20, 20, 30, 30, 40}
print(numbers)

# Creating an Empty Set

s =set()
print(type(s))

# Accessing Elements
# Sets do not support indexing.
s ={10,20,30}
# print(s[1]) 
# TypeError: 'set' object is not subscriptable

s = {10, 20, 30}

for i in s:
    print(i)
    
# Adding Elements
# add()

# Adds a single element
s.add(80)
print(s)

# update()
# Adds multiple elements.

s.update([90,100,34])
print(s)
# Removing Elements
# remove()

# Removes element.
s.remove(90)
print(s)

# Set Operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union ( | )

# Combines all elements.

print(A|B)

# Intersection ( & )

# Common elements.

print(A&B)
# Difference ( - )

# Elements in A but not B.
print(A - B)

# Symmetric Difference ( ^ )

# Elements present in one set only

print(A ^ B)