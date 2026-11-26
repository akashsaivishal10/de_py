# syntax ->[expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]
print(even)

# 1.2 Conditional transformation using if-else
# [expression_if_true if condition else expression_if_false for item in iterable]

numbers = [1, 2, 3, 4, 5]
data = ["Even " if num % 2 == 0 else "Odd" for num in numbers]
print(data)

# 1.3 Multiple conditions
# [expression_if_true if condition else expression_if_false for item in iterable]
employees = [
    {"name": "Alice", "salary": 50000, "department": "IT"},
    {"name": "Bob", "salary": 30000, "department": "HR"},
    {"name": "Charlie", "salary": 70000, "department": "IT"},
    {"name": "David", "salary": 25000, "department": "Finance"},
]

result = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 35000 and emp["department"] == "IT"
]

print(result)

# 1.4 Nested list comprehension
# Suppose you have a list of lists.

data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
nested_data =[x for row  in data for x in row]
print(nested_data)

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

result = [
    x
    for row in data
    for x in row 
    if x>40
]
print(result)

raw_data = [
    "Alice",
    "",
    None,
    "Bob",
    "Charlie",
    None,
    ""
]

result_data =[
    raw.strip()
    for raw in raw_data
    if raw is not None and raw.strip()!=""
]
print(result_data)

# 1.7 String transformation
names = ["alice", "bob", "charlie"]
names_data =[name.upper() for name in names]
print(names_data)

# 2. Advanced Dictionary Comprehensions
# {key_expression: value_expression for item in iterable}

numbers = [1, 2, 3, 4, 5]
data ={x:x*x for x in numbers}
print(data)

employees = {
    "Alice": 50000,
    "Bob": 30000,
    "Charlie": 70000,
    "David": 25000
}

result ={
    name:salary
    for name,salary in employees.items()
    if salary>20000
}

result ={
    name :"High salary "if salary>20000 else "low salary"
    for name,salary in employees.items()
}

print(result)

# Convert two lists into a dictionary

names = ["Alice", "Bob", "Charlie"]
salaries = [50000, 30000, 70000]

result ={
    name:salary
    for name,salary in zip(names,salaries)
}
print(result)
# 2.6 Group data using dictionary comprehension
employees = [
    {"name": "Alice", "department": "IT"},
    {"name": "Bob", "department": "HR"},
    {"name": "Charlie", "department": "IT"},
    {"name": "David", "department": "HR"}
]

departments=set(emp["department"] for emp in employees)

result_dataa = {
    dept :[
        emp["name"]
        for emp in employees
        if emp["department"] =="IT"
    ]
    for dept in departments
}
print(result_dataa)

api_data = [
    {
        "id": 101,
        "name": "Alice",
        "salary": 50000,
        "city": "Hyderabad",
        "status": "Active"
    },
    {
        "id": 102,
        "name": "Bob",
        "salary": 30000,
        "city": "Bangalore",
        "status": "Inactive"
    }
]

active_data =[{
    "employee_id" :data["id"],
    "employee_name" :data["name"],
    "employee_salary" :data["salary"],
    "employee_city":data["city"]
}
    for data in api_data
    if data["status"] =="Active"
]

print(active_data)

# Example 1: Extract completed orders and calculate revenue 

orders = [
    {"order_id": 1, "amount": 1000, "status": "Completed"},
    {"order_id": 2, "amount": 2000, "status": "Pending"},
    {"order_id": 3, "amount": 3000, "status": "Completed"},
    {"order_id": 4, "amount": 4000, "status": "Cancelled"}
]

completed_orders1 =[
    order
    for order in orders
    if order["status"] =="Completed"
]

calculate_revenue = sum(order["amount"] for order in completed_orders1)
print(f"completed_orders {completed_orders1}")
print(calculate_revenue)

