# Iterative Statements (Loops)
# Loops are used to execute code repeatedly.

# Types
# for loop
# while loop

# A) for Loop

# Used when number of iterations is known.
# for variable in sequence:
#     statements

# for i in range(5):
#     print(i)
    
#     range() Function

# Used to generate sequence of numbers.
# 2. range(start, stop)
# for i in range(1,100):
#     print(i)
    # 3. range(start, stop, step)
  
  
for i in range(1, 10, 2):
    print(i)
    
    name = "Python"

for ch in name:
    print(ch)
    
    name = "Python"

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
    
    
#     while Loop

# Used when iterations are unknown.
# while condition:
#     statements

count =0
while count<=5:
    print(count)
    count =count+1
    
    # while True:
    #  print("Running")