# 2. Recursion in Python
# Recursion means a function calling itself.

# A recursive function needs two important things:
# 1. Base condition – stops the recursion.
# 2. Recursive call – calls the same function again with a smaller or simpler problem.

def count_down(n):
    if n==0:
        return
    print(n)
    
    count_down(n-1)
    
count_down(5)

def factorial(n):
    if n == 1:
     return n
    return n * factorial(n-1)
print(factorial(5))

# 2.3 Recursion in Data Engineering
data = {
    "customer": {
        "name": "Akash",
        "address": {
            "city": "Hyderabad",
            "country": "India"
        }
    }
}

def extract_values(data):
    for key,value in data.items():
        if isinstance(value,dict):
         extract_values(value)
        else:
            print(key,value)
    
extract_values(data)

# 3. Decorators in Python 
# A decorator is a function that modifies or
# extends the behavior of another function without changing its original code.

# For example, imagine you have an ETL pipeline.

# Whenever a pipeline runs, you want to print:
# - Pipeline started
# - Pipeline completed
# - Execution details

def welcome():
    print("Welcome to Python")

welcome()

def my_decorator(func):

    def wrapper():

        print("Before function execution")

        func()

        print("After function execution")

    return wrapper

@my_decorator
def welcome():

    print("Welcome to Python")


welcome()

# 3.3 Decorator with arguments

def my_decorator(func):

    def wrapper(*args, **kwargs):

        print("Function started")

        result = func(*args, **kwargs)

        print("Function completed")

        return result

    return wrapper


@my_decorator
def add(a, b):

    return a + b


result = add(10, 20)

print(result)

def my_decorator(func):

    print("1. Inside my_decorator")

    def wrapper():

        print("3. Inside wrapper")

        func()

        print("4. Wrapper completed")

    return wrapper


@my_decorator
def welcome():

    print("Original function executed")


print("2. Before calling welcome")

welcome()

def login_required(func):

    def wrapper():

        print("Checking user login...")

        is_logged_in = True

        if is_logged_in:
            print("User is logged in")

            func()

        else:
            print("Please login first")

        print("Request completed")

    return wrapper


@login_required
def dashboard():

    print("Welcome to Dashboard")


@login_required
def profile():

    print("Welcome to Profile")


dashboard()

print("----------------")

profile()