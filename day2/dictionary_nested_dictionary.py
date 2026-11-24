from collections import Counter
from collections import defaultdict
# 1. What is a Dictionary?
# A dictionary is a Python data structure that stores information in key: value pairs.

employee = {
    "employee_id": 101,
    "employee_name": "Akash",
    "salary": 45000,
    "department": "IT"
}

print(employee)

# 2. Important Dictionary Properties 
# Ordered ->Maintains insertion order
# Mutable ->We can modify values
# Key-value pairs -> Stores data using keys and values
# Unique keys ->Duplicate keys are not maintained
# Different data types -> Values can be strings, integers, lists, etc.

# 3. Accessing Dictionary Values Method 1: Using square brackets
employee = {
    "name": "Akash",
    "age": 27,
    "salary": 45000
}

print(employee["name"])
print(employee["salary"])

# Method 2: Using get()
print(employee.get("salary"))
print(employee.get("name"))
print(employee.get("city" ,"Not Available"))

# 4. Adding New Values

employee["city"] ="Hyderabad"
print(employee)

# 5. Updating Dictionary Values
employee["salary"] =47000
print(employee)
# 6. Deleting Dictionary Values

employee = {
    "name": "Akash",
    "age": 27,
    "salary": 45000
}

employee.pop("age")

print(employee)
# Method 2: del

del employee["salary"]
print(employee)
# Method 3: clear()
employee.clear()
print(employee)
# 7. Dictionary Methods
employee = {
    "name": "Akash",
    "age": 27,
    "salary": 45000
}

print(employee.keys())
print(employee.values())
print(employee.items())
# 8. Looping Through Dictionaries

employee = {
    "name": "Akash",
    "age": 27,
    "salary": 45000
}

for key in employee :
    print(key)
for value in employee.values():
    print(value)
# Example 3: Loop through keys and values

for key,values in employee.items() :
    print(key, ":", value)
    
# 9. Nested Dictionaries A nested dictionary means a dictionary inside another dictionary.

employees = {
    "emp101": {
        "name": "Akash",
        "age": 27,
        "salary": 45000
    },

    "emp102": {
        "name": "Rahul",
        "age": 28,
        "salary": 55000
    },

    "emp103": {
        "name": "Priya",
        "age": 25,
        "salary": 40000
    }
}

print(employees)

# 10. Accessing Nested Dictionary Values
print(employees["emp101"]["name"])
print(employees["emp102"]["age"])
print(employees["emp103"]["salary"])

# 11. Updating Nested Dictionaries 
employees["emp101"]["salary"] =65000

print(employees["emp101"]["salary"])

# 12. Looping Through Nested Dictionaries
for emp_id,details in employees.items() :
    print(f"details of {details}")
    for key,value in details.items():
        print(key,":",value)
# 14. Dictionary Comprehension
# {key: value for item in iterable}

numbers = [1, 2, 3, 4, 5]
squares = {x :x**2 for x in numbers}
print(squares)

employees = {
    "Akash": 45000,
    "Rahul": 55000,
    "Priya": 40000
}


high_salary = {name :salary for name,salary in employees.items() if salary > 45000}
print(high_salary)

# Building a Frequency Map (Counter Pattern) in Python 
# 1. What is a Frequency Map?
# A Frequency Map is a dictionary that stores how many times each value appears.
sentence = "the cat sat on the mat the"

freq ={}
for word in sentence.split():
   freq[word]= freq.get(word,0)+1
print(freq)

# 4. Alternative: Using collections.Counter
freq =Counter(sentence.split())
print(freq)

employees = [
    {"name": "Akash", "department": "IT"},
    {"name": "Rahul", "department": "HR"},
    {"name": "Priya", "department": "IT"},
    {"name": "John", "department": "Finance"},
    {"name": "Sneha", "department": "HR"}
]
group ={}
for emp in employees:
    department = emp["department"]
    if department  not in group :
        group[department]=[]
        
    group[department].append(emp)
print(group)


grouped = defaultdict(list)

print(grouped)

for emp in employees:
    department=emp["department"]
    grouped[department].append(emp)
print(grouped)

# 1. What is Dictionary Comprehension?
# Dictionary comprehension is a shorter way to create dictionaries using a single line of code.

# Normal dictionary creation:
names = ['alice', 'bob', 'carol']

d={}
for name in names :
    d[name]=len(name)
print(d)

# Using dictionary comprehension:

d ={name :len(name) for name in names if len(name)>3}
print(d)

# syntax :{key: value for item in iterable}


marks = {
    "Akash": 85,
    "Rahul": 30,
    "Priya": 75
}

result ={name:"pass" if mark>=35 else "fail" for name,mark in marks.items()}
print(result)