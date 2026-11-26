# 1. What is Exception Handling?
# Exception handling means managing runtime errors without unexpectedly terminating your program.

# num1 = 10
# num2 = 0

# result = num1 / num2 #ZeroDivisionError: division by zero

# print(result)
# print("Program completed")

# 2. try and except
# - try: Contains code that might generate an exception.
# - except: Handles the exception if it occurs.

try:
    num1 =10
    num2=2
    result = num1/num2
    print(result)
except ZeroDivisionError :
    print("cannot divide by zero")
    
print("python program completed")

# 3. Multiple except blocks

try:
    num1 = int(input("Enter a number 1 :"))
    num2 = int(input("Enter a number 2 :"))
    result = num1/num2
    print(result)
except  ValueError:
    print("Enter Valid Numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e :
    print("Unexpected error:", e)


# 4. Exception object – as e

numbers =[10,20,30]
try:
    print(numbers[5])
except Exception as e :
    print("Unexpected error",e)
    
# 5. finally block
# The finally block executes whether an exception occurs or not (including when an exception is handled).


try:
    file=open("employee.csv","r")
    data = file.read()
    print(data)
except Exception as e:
    print("File not found Error",e)
finally :
    print("Exceution is completed")
    
# 6. else block
# The else block executes only when the try block completes without an exception.
try:
    num1 = 100
    num2 = 10

    result = num1 / num2

except ZeroDivisionError:
    print("Division error")

else:
    print("Result:", result)

finally:
    print("Process completed")
    
# 7. Raising exceptions – raise
# Sometimes you need to generate an exception manually when business conditions are not satisfied.

salary =-5000
try:
    if salary<0:
        raise ValueError("salary cannot be negative")
    print("valid salary")
except ValueError as e:
 print(e)