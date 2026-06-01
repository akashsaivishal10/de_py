# Dictionaries in Python

# A Dictionary is a collection used to store data in key-value pairs.

# | Key            | Value               |
# | -------------- | ------------------- |
# | Aadhaar Number | Person Details      |
# | Employee ID    | Employee Details    |
# | Product ID     | Product Information |

# dictionary_name =
# {
#     key1: value1,
#     key2: value2,
#     key3: value3
# }
# Why Use Dictionaries?
# Fast data retrieval
# Store related data together
# Keys are unique
# Mutable (can be modified)

student = {
    "id": 101,
    "name": "Akash",
    "age": 25
}

print(student)

# Creating Dictionaries
# Empty Dictionary

student = {}
print(student)

# Dictionary with Values
employee ={
    "emp_id" :101,
    "emp_name":"Akash",
    "emp_address" :"Hyd"
}
print(employee)

# Accessing Values
# Using Key

print(employee["emp_id"],employee["emp_address"])

# Using get()
# Safer than [] because it doesn't throw an error.
print(employee.get("emp_name"))

# Adding New Items

employee["salary"] =50000
print(employee)
# Updating Values
employee["salary"] =55000
print(employee)
del employee["salary"]
print(employee)
# Dictionary Methods
# keys()

# Returns all keys.
print(employee.keys())
# values()
# Returns all values
print(employee.values())
# items()
# Returns key-value pairs.
print(employee.items())

# update()
# Updates dictionary.

employee.update({"emp_salary":60000})
print(employee)

# clear()

# Removes all items.
print(student.clear())
# Iterating Through Dictionary
# Loop Through Keys

for key in employee:
    print(key)
# Loop Through Values
for values in employee.values():
    print(values)

# Loop Through Key-Value Pairs

for key,values in employee.items():
    print(key, ":" ,values)
# Nested Dictionaries
# Dictionary inside another dictionary.
students ={
    101 :{
        id:101,
        "name":"akash"
    },
    102:{
        id:102,
        "name":"sai"
    }
}