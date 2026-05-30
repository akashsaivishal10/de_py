# 1. Conditional Statements

# Conditional statements are used to execute code based on conditions.

# A) if Statement

# Executes block only if condition is True.
# syntax :
#     if condition:
#     statements

age =20
if(age>18):
    print("Eligible to vote")
    
# B) if-else Statement

# Used when we have two choices.
# if condition :
#     statements 
# else :
#     statements

num =5 
if num %2 ==0 :
    print("num is even")
else :
    print("num is odd")
    
# C) if-elif-else Statement

# Used for multiple conditions.

# if condition1 :
#     statement 
# elif condition2 :
#     statement
# elif condition3:
#     statement
# else :
#     statement

marks =75 

if marks >=90 :
    print("A grade")
elif marks >=70 :
    print("Grade B")
elif marks >=50 :
    print("Grade C")
else :
    print("Grade D")
    
# D) Nested if

# if statement inside another if statement.

age =25
citizen =True

if age >18:
    if citizen :
        print("eligible for vote")
        
        
        
user_name = "akash123"
password = "test@123"

if user_name == "akash123" and password == "test@123" :
    print ("login success")
else:
    print("login failed")
    