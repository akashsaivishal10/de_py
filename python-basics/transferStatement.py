# 2)Transfer Statements

# Transfer statements change the normal flow of execution.
# Types :
# break
# continue
# pass

# break Statement

# Stops the loop completely.

for i in range(1,10):
    if i ==5:
        break 
    print(i)
    
# continue Statement

# Skips current iteration and moves to next iteration.

for i in range(1,10):
    if i==3 :
        continue
    print(f"continue {i}")