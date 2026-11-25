# 1. if statement
# The if statement executes code only when a condition is True.
# if condition:
#     statement
# 2. if-else statement
# Use else when you want to execute one block if the condition is True
# and another block if it is False.
age = 15
if age > 18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")
# 3. if-elif-else statement
# Use elif when you have multiple conditions to check.

salary = 45000
if salary >= 80000:
    print("High salary")
elif salary >= 45000:
    print("Medium Salary")
else:
    print("low salary")
    
# 4. Multiple elif conditions
# You can use multiple elif statements.

marks = 85
if marks>=80:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60 :
    print("Grade C")
elif marks >=40 :
    print("Grade D")
else :
    print("Fail")
