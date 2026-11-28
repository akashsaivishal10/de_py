# What is a module?
# A module is simply a Python file (.py) containing reusable code, such as functions, classes, and variables.

# Instead of writing everything in one Python file, we can divide our code into multiple files.

import os

print(os.getcwd())
print(os.listdir())

# 2. Python Packages
# What is a package?
# A package is a collection of related Python modules organized inside a directory.

# data_engineering/
# │
# ├── main.py
# │
# └── utilities/
#     ├── __init__.py
#     ├── file_operations.py
#     ├── database.py
#     └── transformations.py

# - utilities is a package.
# - file_operations.py is a module.
# - database.py is a module.
# - transformations.py is a module.
# - __init__.py marks the directory as a regular Python package.
# Modern Python also supports namespace packages without __init__.py, but learn the regular package structure first.


# 3. Python Virtual Environments
# What is a virtual environment?
# A virtual environment creates an isolated Python environment for an individual project.

# Project	Pandas version
# Project A	2.0
# Project B	2.2

