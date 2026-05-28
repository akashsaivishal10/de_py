# A variable is a name used to store data in memory.
name = "Akash"
# name is a variable name
# Akash is a values stored 
# = assignment operator 
# Why Variables Are Important in Data Engineering
# In Data Engineering, variables are used everywhere:

# storing file paths
# database credentials
# API responses
# Spark DataFrames
# SQL queries
# counts and aggregations
# configuration values
# pipeline states

database_name = "sales_db"
file_path = "/data/customers.csv"
total_records = 50000
# Without variables, managing data pipelines becomes impossible.

# Variable Creation

# Python is dynamically typed
age = 25
salary = 50000.75
name = "Akash"
is_active = True

# allowed 
name = "Akash"
user_age = 25
_marks = 90
salary2025 = 1000

# not allowed 
# 2name = "Akash"      # starts with number
# user-name = "Akash"  # hyphen not allowed
# class = "Python"     # keyword not allowed

# case senstivity
name = "Akash"
Name = "Sai"

print(name)
print(Name)

# Multiple Variable Assignment
a=b=c= 100
print(a)
print(b)
print(c)

# Different values 
x,y,z =10,20,30
print(x)
print(y)
print(z)

# swapping variables

a=10
b=20

a,b =b,a
print(f"value of a is {a}")
print(f"value of b is {b}")

# A tuple in Python is an ordered, immutable collection of items.

# How to create a tuple

# You use parentheses ():

my_tuple =(10,20,30)
print(my_tuple[0])
# Why tuples are immutable
# my_tuple[0]=90 TypeError: 'tuple' object does not support item assignment

# Tuple with different data types

# Tuples can store mixed types:
    
t = (1, "hello", 3.5, True)

# list 
numbers = [1, 2, 3]

# Dictionary 
student = {
    "name": "Akash",
    "age": 25
}

# Checking Variable Type 
print(type(student["name"]))

# Type Conversion (Casting)
# Integer to String
age =25;
print(str(age))
# String to Integer
num = "100"

print(int(num))

# Mutable vs Immutable Variables
# Immutable

# Cannot change after creation.

# Examples:

# int
# float
# string
# tuple

name = "Akash"

name = "Sai"

# Mutable

# Can change directly.

# Examples:

# list
# dictionary
# set

numbers = [1, 2, 3]

numbers.append(4)