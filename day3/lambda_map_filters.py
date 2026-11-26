from functools import reduce

# What is Lambda?
# A lambda is a small anonymous function (a function without a name).


# normal function
def square(num):
    return num * num


print(square(5))

# lambda function
# syntax :lambda arguments: expression
square = lambda num: num * num
print(square(5))

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
even = lambda num: num % 2 == 0
print(add(10, 20))  # 30
print(sub(10, 20))
print(mul(10, 20))
numbers = [10, 20, 30, 40]
print(list(map(even, numbers)))
salaries = [25000, 35000, 45000, 55000, 65000]

updates_salaries = list(map(lambda salary: salary * 1.10, salaries))
print(updates_salaries)

# 3. Topic 2: map()
# map() applies a function to every element in an iterable.
# map(function, iterable)

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)

# Convert string values into integers.

raw_data = ["100", "200", "300", "400"]
int_data = list(map(int, raw_data))
print(int_data)

[100, 200, 300, 400]


# 4. Topic 3: filter()
# filter() selects elements based on a condition.

numbers = [10, 15, 20, 25, 30, 35]
filter_numbers = list(filter(lambda x: x >= 20, numbers))
print(filter_numbers)
# Filter employees whose salaries are greater than 40,000.
employees = [
    {"name": "Alice", "salary": 25000},
    {"name": "Bob", "salary": 45000},
    {"name": "Charlie", "salary": 55000},
    {"name": "David", "salary": 35000},
]

salaries = list(filter(lambda emp: emp["salary"] > 40000, employees))
print(salaries)


# 5. Topic 4: reduce()
# reduce() repeatedly applies a function to accumulate values into a single result.
# It is available in the functools module.
numbers = [10, 20, 30, 40, 50]
result = reduce(lambda a, b: a + b, numbers)
print(result)

orders = [1000, 2000, 1500, 3000, 2500]
total_revenue = reduce(lambda a, b: a + b, orders)
print(total_revenue)
# Create a lambda function to calculate the cube of a number.

cube = (lambda a: a * a * a)(5)
print(cube)
# Use map() and lambda to add 5 to every number.
numbers = [10, 20, 30, 40, 50]
result1 = list(map(lambda a: a + 5, numbers))
print(result1)
# Use filter() to get only even numbers.
numbers = [12, 15, 20, 25, 30, 35, 40]
even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print(even_numbers)

numbers = [10, 20, 30, 40, 50]
print(reduce(lambda a, b: a + b, numbers))
# Use filter() to select employees with salary greater than 40,000.
# Use map() to extract their salaries.
# Use reduce() to calculate their total salary.
# Print the final result.
employees = [
    {"name": "Alice", "salary": 25000},
    {"name": "Bob", "salary": 45000},
    {"name": "Charlie", "salary": 55000},
    {"name": "David", "salary": 35000},
    {"name": "Emma", "salary": 65000},
]

filtered_employees = list(filter(lambda emp: emp["salary"] > 40000, employees))

salaries = list(map(lambda emp: emp["salary"], filtered_employees))

total_salary = reduce(lambda a, b: a + b, salaries)

print(total_salary)

employees = [
    {"name": "Alice", "salary": 25000, "department": "IT"},
    {"name": "Bob", "salary": 45000, "department": "HR"},
    {"name": "Charlie", "salary": 55000, "department": "IT"},
    {"name": "David", "salary": 35000, "department": "Finance"},
    {"name": "Emma", "salary": 65000, "department": "IT"},
]

# Filter employees belonging to the IT department.
# Filter employees whose salary is greater than 30,000.
# Use map() to extract employee names.
# Print the final names

employee_data = list(filter(lambda emp: emp["department"] == "IT", employees))
emp_salaries =list(filter(lambda emp_salary:emp_salary["salary"]>30000,employee_data))
names = list(map(lambda names:names["name"],emp_salaries))
print(names)

orders = [
    {"order_id": 101, "amount": 5000, "status": "Completed"},
    {"order_id": 102, "amount": 3000, "status": "Pending"},
    {"order_id": 103, "amount": 7000, "status": "Completed"},
    {"order_id": 104, "amount": 2000, "status": "Cancelled"},
    {"order_id": 105, "amount": 6000, "status": "Completed"}
]
# Filter only Completed orders.
# Extract their amounts using map().
# Calculate total revenue using reduce().
# Calculate the average order amount.

orders_data = list(filter(lambda order: order["status"] == "Completed", orders))
data =list(map(lambda orders_data:orders_data["amount"],orders_data))
total_revenue = reduce(lambda a, b :a + b,data,0)
average = total_revenue/len(data)if total_revenue else 0
print(total_revenue)
print(average)