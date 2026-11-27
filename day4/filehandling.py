# 1. Understanding file handling
# Python provides built-in functions to read, write, and modify files.

# The most commonly used functions are:
# Function	Purpose
# open()	Opens a file
# read()	Reads entire file
# readline()	Reads one line
# readlines()	Reads all lines into a list
# write()	Writes data
# close()	Closes a file
# with open()	Automatically closes the file
# Example 1: Create and write a TXT file
import csv, json, os

with open("employee.txt", "w") as file:
    file.write("Akash,IT,45000\n")
    file.write("Sai,IT,55000\n")
    file.write("Vishal,IT,65000\n")
# Example 2: Read a TXT file

with open("employee.txt", "r") as file1:
    data = file1.read()
print(data)

# Example 3: Read line by line
with open("employee.txt", "r") as file:
    for line in file:
        print(line.strip())

# Example 4: Append data
with open("employee.txt", "a") as file:
    file.write("Raj,IT,89000")

error_message = "Customer ID 105 failed validation"

with open("error_log.txt", "a") as file:
    file.write(error_message + "\n")

# 3. CSV file handling

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Example 2: Read CSV using DictReader
# This is particularly useful because you can access columns by their names.

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["salary"])

# Example 3: Write CSV file

employees = [
    [101, "Alice", "IT", 50000],
    [102, "Bob", "HR", 40000],
    [103, "Charlie", "Finance", 60000],
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["emp_id", "emp_name", "emp_dept", "emp_salary"])
    writer.writerows(employees)
print("example 4 results")
# Example 4: Filter CSV records
with open("output.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["emp_salary"]) > 40000:
            print(row["emp_name"], row["emp_salary"])
# Example 5: Read CSV and calculate department salary

department_salary = {}

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        department = row["department"]
        salary = int(row["salary"])

        department_salary[department] = department_salary.get(department, 0) + salary

print(department_salary)

# 4. JSON file handling
# JSON stands for JavaScript Object Notation.

# In Azure Data Engineering, JSON is frequently used when consuming REST APIs.

# Example 1: Read JSON file

with open("employees.json", "r") as file:
    data = json.load(file)

    for employee in data:
        emp_id = employee["employee_id"]
        emp_name = employee["name"]
    print(emp_id, emp_name)

# Example 3: Filter JSON records
# Find employees whose salary is greater than 50,000.

with open("employees.json", "r") as file:
    data = json.load(file)

result_salary = [emp for emp in data if emp["salary"] > 50000]
print(result_salary)

revenues = {
    "land_revenue_demand": [
        {
            "title_id": "1053468584",
            "total_area": "1.9800",
            "title_no": "72",
            "year_range": "2026-27",
            "is_diverted": "0",
            "agg_land_revenue": "0",
            "panchyat_cess": "0",
            "educational_cess": "0",
            "commerical_tax": "0",
            "total": "0",
        }
    ]
}

with open("output.json", "w") as file:
    json.dump(revenues, file, indent=4)


employee = {"id": 101, "name": "Alice", "salary": 50000}

json_data = json.dumps(employee)
print(json_data)
print(type(json_data))

# 6. Advanced file handling for Data Engineers


try:
    with open("employees.json", "r") as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON format")
except Exception as e:
    print(e)


# B. Check whether a file exists
file_path = "employees.csv"
filesize = os.path.getsize(file_path)
if os.path.exists(file_path):
    print("file exists")
else:
    print("file not exists")
print(filesize)

# D. Process large CSV files in chunks
# For large files, avoid loading everything into memory.

with open("customers.csv", "r") as file:
    reader = csv.DictReader(file)
    batch_size = 1000
    batch = []
    for row in reader:
        batch.append(row)
        if len(batch) == batch_size:
            print("Processing batch:", len(batch))
            batch.clear()
    if batch:
        print("Processing remaining:",len(batch))


# E. Read multiple CSV files from a folder

folder_path="D:\DE\de_py\day4"

for file_name in os.listdir(folder_path):
    if file_name.endswith("csv"):
        file_path =os.path.join(folder_path,file_name)
        print("Processing:", file_name)
    with open(file_path,"r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)