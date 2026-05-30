# Lists in Python (Detailed Explanation)

# A List is one of the most commonly used collection data types
# in Python.

# Used to store multiple values in a single variable.
# Lists are ordered, mutable (changeable), 
# and allow duplicate values.
# Represented using square brackets [].

# 1. Creating a List 
numbers  =[10,20,30,40,50]
print(numbers)

# 2. List Can Store Different Data Types 
data = [2341,"Akash",50000.00,True]
print(data)

# 3. Accessing List Elements (Indexing) Indexes start from 0.
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative Indexing 
print(fruits[-1])
print(fruits[-2])

# 4. List Slicing
# syntax  list[start:end:step]
numbers =[10,20,30,40,50,60,70,80]

print(numbers[2:6])
print(numbers[1:2])
print(numbers[::-1])

# 5. Modifying List Elements

# Lists are mutable.
data = [2341,"Akash",50000.00,True]
print(f"before  {data}")
data[1] ="Akash Sai Vishal"
print(f" after mutable {data}")

# Important List Methods
# 6. append()

# Adds an element at the end.

num = [10,30,55]
print(f"before append {num}")

num.append([35,80])
print(f"after append {num}")

# 7. insert()
# Adds an element at a specific position.

numbers = [10, 20, 30]
numbers.insert(2,70)
print(numbers)

# 8. extend()

# Adds multiple elements.

numb = [10,20]
numb.extend([50,60,10,40])
print(numb)

# 9. remove()

# Removes the first matching value.

numbers = [10,20,30,40,50,60]

numbers.remove(30)
print(numbers )
# 10. pop()

# Removes element using index.

numbers = [10,20,30,40,50,60]
numbers.pop(3)
print(numbers)

# 11. clear()

# Removes all elements.
numbers = [10,20,30,40,50,60]
numbers.clear()
print(numbers)
# 12. index()
# Returns position of element.
fruits =["Apple","Banana","Pine Apple"]
print(fruits.index("Banana"))

# 13. count()
# Counts occurrences.
numbers = [10, 20, 20, 30, 20]
print(numbers.count(20))

# 14. sort()
# Sorts the list.
numbers = [50, 20, 40, 10]
numbers.sort()
print(numbers)

# Descending Order
numbers.sort(reverse=True)
print(numbers)

# 15. reverse()
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)

# 16. copy()
# Creates a copy.
numbers = [10, 20, 30]
print(numbers)
num = numbers.copy()
print(num)

# Iterating Through Lists
# Using for Loop
fruits =["Apple","Banana","Pine Apple"]
for fr in fruits :
    print(fr)
    
# Using range()
fruits = ["Apple", "Banana", "Mango"]
for fr in range(len(fruits)):
    print(fr,fruits[fr])
    