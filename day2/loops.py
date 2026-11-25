# 1. What is a Loop?
# A loop is used to execute a block of code repeatedly.

# 2. For Loop
# A for loop is used when we want to iterate over a sequence or collection of items.
# Example 1: Print numbers
for i in range(1, 6):
    print(i)
# Example 2: Iterate over a list

employees = ["Akash", "Rahul", "Priya", "John"]
for emp in employees:
    print(emp)
# Example 3: Calculate total sales 
sales = [1000, 2000, 3000, 4000, 5000]
total =0 
for sales_data in sales :
    total =total+sales_data 
    print(total)

# Example 4: For loop with if condition

numbers = [10, 15, 20, 25, 30]
for num in numbers :
    if num % 2==0 :
        print(num)
        
# 3. While Loop
# A while loop executes repeatedly as long as a condition is True.

# Example 1: Print numbers from 1 to 5 

i=1 
while i<=5 :
    print(i)
    i=i+1
    
# Example 2: Calculate total

numbers = [10, 20, 30, 40, 50]

i=0
total=0
while i<len(numbers):
    total = total +numbers[i]
    i=i+1 
    print(total)