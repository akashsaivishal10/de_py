# 1. What is a List?
# A Python list is a collection used to store multiple values in a single variable.
employee_name = ["Akash", "Sai", "Vishal"]
print(employee_name)
# Instead of creating four separate variables, we can store all employee names in one list.

# Important list characteristics
# - Ordered: Maintains insertion order.
# - Mutable: We can modify values.
# - Allows duplicates: Same values can appear multiple times.
# - Allows different data types: Integer, string, float, Boolean, etc.

employee = ["Akash", 27, 42000, True]
print(employee)

# 2. Accessing List Elements (Indexing) Python list indexing starts from 0, not 1.

sales = [1000, 2000, 3000, 4000, 5000]
print(sales[0])
print(sales[1])
print(sales[2])
print(sales[3])
print(sales[4])
# print(sales[5]) IndexError: list index out of range

# negative  indexing   ->accessing last elements
print(sales[-1])
print(sales[-2])

# 3. Adding Elements to a List
# There are three important methods.

sales1 = [1000, 2000, 3000]
print(sales1)
sales1.append(4000)  # Adds one element at the end.
print(sales1)

# B. insert()
# Adds an element at a specific index.

sales1.insert(0, 1000)
print(sales1)
# C. extend()
# Adds multiple elements from another iterable.
sales1.extend([5000, 6000])
print(sales1)

# append() vs extend()
a = [10, 20]
a.append([30, 40])
print(a)

b = [10, 20]
b.extend([30, 40])
print(b)

# 4. Removing Elements
# remove() -	Removes a specific value
# pop()	- Removes an element by index and returns it
# del -	Deletes an element or a slice
# clear() -	Removes all elements
# Example 1 – remove():
numbers = [10, 20, 30, 40]
print(numbers)
numbers.remove(20)
print(numbers)
numbers1 = [100, 200, 300, 400]
# Example 2 – pop():
removed = numbers1.pop()
print(f"{removed}")
print(numbers1)
# Example 3 – del:

numbers2 = [100, 2000, 3000, 4000]
del numbers2[1]
del numbers2
# print(numbers2)NameError: name 'numbers2' is not defined. Did you mean: 'numbers'?
# Example 4 – clear():
numbers3 = [100, 2000, 3000, 4000]
print(numbers3)
numbers3.clear()
print(numbers3)

# 5. Updating List Elements
# We can modify an existing list element using its index.
numbers3 = [100, 2000, 3000, 4000]
numbers3[0] = 1000
print(numbers3)

# 6. Sorting and Reversing
# sort()
# Sorts elements in ascending order.
numbers = [50, 10, 40, 20, 30]
numbers.sort()

print(numbers)

# Descending order:

numbers.sort(reverse=True)
print(numbers)

# reverse()
# Reverses the current order.
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)
# 7. List Slicing
# Slicing allows us to extract a portion of a list.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:5])


numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])  # First 3 elements
print(numbers[2:])  # Index 2 to end
print(numbers[::2])  # Every second element
print(numbers[::-1])  # Reverse the list

numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n * n)
print(squares)
# Example 1: Sort employees by age
employees = [
    {"name": "akash", "age": 27},
    {"name": "sai", "age": 34},
    {"name": "vishal", "age": 22}
]

employees.sort(key=lambda e:e["age"])
print(employees)
# Example 2: Sort products by price (Highest first)
products = [
    {"product": "Laptop", "price": 60000},
    {"product": "Mobile", "price": 25000},
    {"product": "Tablet", "price": 35000},
]

products.sort(key=lambda p:p["price"],reverse=True)
print(products)

employees1 = [
    {"name": "Ravi", "salary": 80000},
    {"name": "Akash", "salary": 90000},
    {"name": "John", "salary": 80000},
    {"name": "David", "salary": 90000},
]

employees1.sort(key=lambda e:(-e["salary"],e["name"]))
print(employees1)

# 1. What is List Comprehension?
# List comprehension is a shorter way to create a new list using an existing iterable
# (such as a list, range, or tuple).
# Normal for-loop approach:
numbers = [1, 2, 3, 4, 5]

squares = []

for x in numbers:
    squares.append(x ** 2)

print(squares)

# List comprehension approach:
squares = [x**2 for x in numbers]
print(squares)

# 4. List comprehension with IF condition
result =[x for x in range(10) if x %2 ==0]
print(result)

raw = ["  Alice ", " BOB  ", "carol  ", None, "  DAVE"]
clean = [r.strip().title() for r in raw if r is not None]
print(clean)

batches = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
test = [x for batch in batches for x in batch ]

# for batch in batches → Select one inner list.

# for x in batch → Select each element inside it.

# x → Add that element to the new list.

print(test)
# Example A: Extract employee salaries above 50,000
employees = [
    {"name": "Akash", "salary": 45000},
    {"name": "Ravi", "salary": 65000},
    {"name": "John", "salary": 75000},
    {"name": "David", "salary": 40000}
]

high_salary =[emp["salary"] for emp in employees if emp["salary"]>50000]
print(high_salary)

# Example B: Convert strings to uppercase

columns = ["customer_id", "customer_name", "city", "salary"]

upper_case = [col.upper() for col in columns]
print(upper_case)

# Example C: Filter successful API records

api_records = [
    {"id": 101, "status": "SUCCESS"},
    {"id": 102, "status": "FAILED"},
    {"id": 103, "status": "SUCCESS"},
    {"id": 104, "status": "FAILED"}
]

successful_records = [rec for rec in api_records if rec["status"]=="SUCCESS"]
print(successful_records)

# 8. Advanced: IF-ELSE in List Comprehension

numbers = [1, 2, 3, 4, 5, 6]
data = ["EVEN "if x%2==0 else "ODD" for x in numbers]
print(data)