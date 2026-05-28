# What is a String?

# A string is a sequence of characters enclosed inside:
# Single quotes ' '
# Double quotes " "
# Triple quotes ''' ''' or """ """

# 1. Strings are Ordered
text ="Python"
print(text[0])
print(text[1])
print(text[2])

# 2. Strings are Immutable Cannot change characters directly.
# text[0]="J" 
# correct way 
text ="Jython"

# TypeError: 'str' object does not support item assignment

# 2. Reading Data From Strings in Python
text = "Python"

print(text[0])  # P
print(text[1])  # y
print(text[5])  # n
# | Character | P | y | t | h | o | n |
# | --------- | - | - | - | - | - | - |
# | Index     | 0 | 1 | 2 | 3 | 4 | 5 |

# Negative Indexing

# Python supports reverse indexing.

print(text[-1])
print(text[-4])

# | Character      | P  | y  | t  | h  | o  | n  |
# | -------------- | -- | -- | -- | -- | -- | -- |
# | Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |
# 3.String Slicing

# Slicing means extracting part of a string.
# syntax :string[start:end:step]
# start → starting index
# end → ending index (excluded)
# step → jump value

text = "PythonProgramming"

print(text[0:6])

text = "Python"

print(text[0:6:2])
# | Index | Character |
# | ----- | --------- |
# | 0     | P         |
# | 1     | y         |
# | 2     | t         |
# | 3     | h         |
# | 4     | o         |
# | 5     | n         |
# | 6     | P         |
# | 7     | r         |
# | 8     | o         |
# | 9     | g         |
# | 10    | r         |
# | 11    | a         |
# | 12    | m         |
# | 13    | m         |
# | 14    | i         |
# | 15    | n         |
# | 16    | g         |

text = "PythonProgramming"

print(text[6:17])

# text = "Python"

print(text[::-1])

# String Concatenation
# Concatenation means joining strings.
first_name ="Akash"
last_name ="sai vishal"

full_name = first_name + " " + last_name ;
print(full_name)

text = "Hi "

print(text * 3)

# Method 1 — f-string (Recommended)
name = "Akash"
age = 25

print(f"My name is {name} and age is {age}")

# Method 2 — format()

name = "Akash"
salary = 50000

print("Name: {} Salary: {}".format(name, salary))

# Searching Functions
# find()

# Returns index position.

text ="python programming"
print(text.find("program"))

# index()

# Similar to find but throws error if not found.

text = "Python"

print(text.index("t"))

# Replace Function

text ="I like Java"

new_text = text.replace("Java","Python")
print(new_text)

# Split Function

# Converts string into list.
text = "apple,banana,mango"
print(text.split(','))

# Join Function

# Converts list into string.
items =['python','java','js']
print(" | ".join(items))

# Checking Functions
# startswith()
text = "Python"

print(text.startswith("Py"))
# endswith()
text = "report.csv"

print(text.endswith(".csv"))

text = "Python"

print(text.isalpha())