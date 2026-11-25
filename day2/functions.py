# 1. What is a function?
# A function is a reusable block of code that performs a particular task.


def add_numbers():
    print(10 + 20)


add_numbers()

# 4. Function with parameters
# Parameters allow us to pass values into a function.


def greet(name):
    print(f"hii {name}")


greet("Akash")


# 5 Multiple parameters
def employee_details(name, age, salary):
    print(name, age, salary)


employee_details("Akash", 27, 42000)

# 6. Return statement
# return sends a result back from a function.


def add_numbers(a, b):
    result = a + b
    return result


output = add_numbers(10, 20)
print(output)

# 7. Default parameters
# If the caller does not provide a value, Python uses the default value.


def employee_details(name, domain="data engineering"):
    print(name, domain)


employee_details("akash")

# 8. Keyword arguments
# You can pass arguments using parameter names.


def student(name, age, course):
    print(name, age, course)


student(name="Akash", age=27, course="DE")

# 9. *args – Multiple positional arguments
# Use *args when you don't know how many positional arguments will be passed.


def calculate_numbers(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


print(calculate_numbers(10, 20))
print(calculate_numbers(10, 20, 30, 40))
print(calculate_numbers(10, 20, 40, 50))

# 10. **kwargs – Multiple keyword arguments
# Use **kwargs when you don't know how many keyword arguments will be passed.


def employee_details(**details):

    for key, value in details.items():
        print(key, ":", value)


employee_details(name="Akash", age=27, department="Data Engineering", salary=45000)

# 11. Lambda functions
# A lambda is a small anonymous function.

square = lambda x: x * x

print(square(5))

# Example 1: Data cleaning


def clean_name(name):
    return name.strip().title()


names = [" akash ", " rahul ", " john "]
cleaned_names = []
for name in names:
    cleaned_names.append(clean_name(name))
print(cleaned_names)


def calculate_sales(price, quantity):
    total = price * quantity
    return total


sales = calculate_sales(100, 200)
sales1 = calculate_sales(1000, 2000)
print(sales)
print(sales1)
def validate_employee(employee_id, salary):

    if employee_id is None:
        return "Invalid Employee ID"

    elif salary <= 0:
        return "Invalid Salary"

    else:
        return "Valid Record"

print(validate_employee(101, 45000))
print(validate_employee(None, 45000))
print(validate_employee(102, -500))