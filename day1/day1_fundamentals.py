# What is a variable?
# A variable is a name used to store a value in memory.
# Example 1: Basic variables
name ="akash",
age =27 
salary =45000
experience =4

print(name)
print(age)
print(salary)
print(experience)

# Example 2: Updating variables

salary =45000
print(salary)
salary =76000
print(salary)

# Python variables are dynamic. You can change their values during execution.

a=100
b=100
c=100
print(a,b,c)

a=b=c=100
print(a,b,c)


# 2. Data Types in Python
# What are data types?
# Data types define what kind of value a variable stores.
# Numeric data types  ->Stores whole numbers.
age = 25
employee_count = 100
# 2. Float (float) ->Stores decimal numbers.
salary = 75000.50
percentage = 85.5
# 3. Complex (complex) Stores complex numbers.
number = 3 + 5j

# B. String (str) ->Stores text values.

employee_name = "Akash"
city = "Hyderabad"

print(employee_name)
print(type(employee_name))

# C. Boolean (bool)
# Stores only two values:
# - True
# - False

is_active = True
is_deleted = False

print(is_active)
print(type(is_active))

# D. Sequence data types
# 1. List -> Stores multiple values. Lists are mutable (modifiable).

employeee = ["akash" ,"sai" ,"vishal"]
print(employeee[0])
employeee.append("yakkaluru")
print(employeee)

# 2. Tuple -> Stores multiple values. Tuples are immutable.
departments = ("IT", "HR", "Finance")
print(departments[0])
# departments.append("SALES") ->'tuple' object has no attribute 'append'
# 3. Range ->Represents a sequence of numbers.
numbers = range(1, 6)
print(list(numbers))

# E. Set ->Stores unique values and removes duplicates.  Order is not guaranteed.
numbers = {10, 20, 10, 30, 20}
print(numbers)
# F. Dictionary (dict) ->Stores data in key-value pairs.
employee = {
    "id": 101,
    "name": "Akash",
    "salary": 75000,
    "department": "IT"
}

print(employee["name"])
print(employee["salary"])

# How to check data types?
# Use the type() function.

a = 100
b = 99.50
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Type conversion (Type Casting)
# Converting one data type into another.

ab="100"
print(type(ab))
dc =int(ab)
print(type(dc))

# 3. Operators in Python
# Operators are symbols used to perform operations on values and variables.
# A. Arithmetic operators ->Used for mathematical calculations 
a = 20
b = 10

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Modulus
print(a ** b)  # Power

# B. Comparison operators
# Used to compare two values. The result is always Boolean (True or False).

a = 100
b = 50

print(a == b) #false
print(a != b) #true
print(a > b) #true
print(a < b) #false
print(a >= b) #true
print(a <= b) #false

# C. Logical operators
# Used to combine multiple conditions.

# Three important operators:
# - and
# - or
# - not
age = 25
salary = 80000

print(age > 18 and salary > 50000)
print(age > 30 or salary > 50000)
print(not age > 18)

# D. Assignment operators
# Used to assign or update values.

a = 10

a += 5
print(a)    # 15

a -= 3
print(a)    # 12

a *= 2
print(a)    # 24

a /= 4
print(a)    # 6.0

# E. Membership operators
# Check whether a value exists in a collection.

# Two operators:
# - in
# - not in
employees = ["Akash", "Ravi", "Kiran"]

print("Akash" in employees)
print("John" not in employees)

# F. Identity operators
# Check whether two variables refer to the same object in memory.
# - is
# - is not

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)   # True
print(a is c)   # False
print(a == c)   # True
# Important difference:
#  == compares values.
#  is compares object identity.

# Q1. Create variables for employee_name, employee_age, employee_salary and print all values.
employee_name ="akash"
employee_age =27
employee_salary =45000
print(employee_name,employee_age,employee_salary)

# Create five variables using int, float, string, boolean and list. Print their data types.
employee_name ="akash"
employee_age =27
employee_salary =45000.86
employee_exits = True 
employee_domain = ["dev" ,"analyst"]
print(type(employee_name))
print(type(employee_age))
print(type(employee_salary))
print(type(employee_exits))
print(type(employee_domain))

# Q3. Convert salary = '85000' into an integer and add 15000.

salary = '8500'
print(15000 +int(salary))
# Q4. Create two numbers a = 25 and b = 10. Perform all arithmetic operations.
a = 25 
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Q5. Check whether salary = 90000 is greater than 50000 and less than 100000.
salary = 90000
print(salary >50000 and salary<100000)

# Q6. Check whether age = 25 and experience = 4 satisfy age greater than 18 AND experience greater than 3.

age =25
experience=4
print(age >18 and experience >3 )

# Q7. Create a list of five employee names and check whether 'Akash' exists.
employees = ["Akash", "Ravi", "Kiran"]

print("Akash "in employees)

# Q8. Create an employee dictionary containing id, name, salary and active status. Print each value.
employee= {
    "id" :"EMP021",
    "name" :"Akash",
    "salary" :76999,
    "active" :True
}
print(employee["id"])
print(employee["name"])
print(employee["salary"])
print(employee["active"])