# 2. Tuples in Python
# Immutable
#  Ordered
#  Allows duplicates


# A Tuple is similar to a list, but you cannot modify its elements after creation.

employee = ("Akash", 27, 45000)

print(employee)
print(type(employee))

# Example 2: Accessing tuple elements
employee = ("Akash", 27, 45000)

print(employee[0])
print(employee[1])
print(employee[2])

# Example 3: Immutable behavior

employee = ("Akash", 27, 45000)

# employee[1] = 28 #TypeError: 'tuple' object does not support item assignment
# why Because tuples are immutable.

# Example 4: Tuple methods
# Only two built-in tuple methods:

numbers = (10, 20, 30, 20, 40)

print(numbers.count(20))
print(numbers.index(30))

# Example 5: Tuple unpacking
employee = ("Akash", 27, "Data Engineer")
name, age, role = employee
print(name)
print(age)
print(role)

# 3. Sets in Python
# A Set is a collection that stores only unique elements.
# Mutable ,Unordered ,Unique values only
# Example 1: Creating a set
numbers = {10, 20, 30, 10, 20}
print(numbers)

# Example 2: Adding and removing elements
numbers = {10, 20, 30}
numbers.add(40)  # add only one element
numbers.update({40, 50, 60})  # add multiple elements
removed = numbers.pop()
print(removed)
numbers.remove(20)  # remove specific element
print(numbers)

customer_ids = [101, 102, 103, 101, 102, 104]
unique_ids = set(customer_ids)
print(unique_ids)


source_a = {101, 102, 103, 104}
source_b = {103, 104, 105, 106}

# A. Union – All unique values
print(source_a | source_b)

# B. Intersection – Common values
print(source_a & source_b)
# C. Difference – Values present only in A

print(source_a - source_b)

# D. Symmetric Difference – Values not common to both 
print(source_a ^ source_b)