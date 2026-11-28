# import calculations
from calculations import add,multiply
# 3. Import with an alias
import calculations as calc
# 4. Import everything (not recommended)
from calculations import *
result = add(5,10)
result1 = multiply(5,10)

print(result)
print(result1)