# 1. What is a String?
# A string is a sequence of characters enclosed in quotes.

employee_name = "Akash"
city = "Hyderabad"
project = """Enterprise Retail Data Engineering"""

print(employee_name)
print(city)
print(project)

print(type(employee_name))

# 2. Important String Operations
# These are the fundamental operations you must know.
# 2.1 String indexing
# Access individual characters using their positions.

customer_name = "AKASH"
print(customer_name[0])
print(customer_name[1])
print(customer_name[2])
print(customer_name[3])
print(customer_name[4])
# print(customer_name[5]) IndexError: string index out of range
print(customer_name[-1])

order_id = "ORD202600123"
prefix = order_id[:5]
print(prefix)

# 2.2 String slicing
# Slicing extracts part of a string. string[start:end:step]


order_id = "ORD202600123"
print(order_id[0:3])
print(order_id[3:7])
print(order_id[-3:])
# 3. Important Python String Methods
# These are the methods you should practise deeply.
# 3.1 Case conversion methods
# Method	Purpose	Example
# upper()	Convert to uppercase	"akash".upper()
# lower()	Convert to lowercase	"AKASH".lower()
# title()	Capitalize each word	"data engineer".title()
# capitalize()	Capitalize first character	"akash".capitalize()
# casefold()	Stronger case normalization	"HELLO".casefold()

customers = ["akash", "AKASH", "Akash", "aKaSh"]
cleaned_customers = []

for name in customers:
    cleaned_name = name.strip().title()
    cleaned_customers.append(cleaned_name)
    print(cleaned_customers)
# 3.2 Whitespace removal methods
# Method	Purpose
# strip()	Remove spaces from both ends
# lstrip()	Remove spaces from left
# rstrip()	Remove spaces from right

customer_name = "   Akash Sai   "
print(customer_name.strip())
print(customer_name.lstrip())
print(customer_name.rstrip())

api_data = [" Hyderabad ", " Bangalore  ", "  Chennai", " Pune "]
cleaned_Data = []
for data in api_data:
    cleaned_Data.append(data.strip())
    print(cleaned_Data)
# 3.3 Replace method
# replace() replaces a particular substring with another substring. string.replace(old, new)

phone_number = "987+654+3210"
cleaned_number = phone_number.replace("+", "")
print(cleaned_number)

# Real-world ETL example:

prices = ["₹1,500", "₹2,500", "₹3,000"]
cleaned_price = []
for price in prices:
    cleaned_price.append(price.replace("₹", "").replace(",", ""))
    print(cleaned_price)

# 3.4 Split method
# split() divides a string into a list.

employee_details = "Akash,27,Data Engineer,Hyderabad"
data = employee_details.split(",")
print(data)
# Production example: Processing delimited source data

record = "101|Akash|Data Engineering|45000"

column_data = record.split("|")
employee_id = column_data[0]
employee_name = column_data[1]
employee_role = column_data[2]
employee_salary = column_data[3]


print(employee_id, employee_name, employee_role, employee_salary)

# 3.5 Join method
# join() combines multiple strings into one string.
columns = ["employee_id", "employee_name", "salary"]

result = ",".join(columns)
print(result)

# Production example: Generating dynamic SQL column lists

columns1 = ["customer_id", "customer_name", "city", "total_sales"]

column_list = ", ".join(columns1)

query = f"SELECT {column_list} FROM customers"

print(query)

# 3.6 Startswith and endswith
# These methods check how a string begins or ends.

file_name = "sales_2026.csv"
print(file_name.startswith("sales"))
print(file_name.endswith("csv"))

files = [
    "sales_2026.csv",
    "customer_2026.json",
    "orders_2026.parquet",
    "sales_backup.txt",
]


for file in files:
    if file.startswith("sales") and file.endswith("csv"):
        print(f"File processing {file}")
# 3.7 Find and index
# Both methods search for a substring.

message = "Azure Data Engineering Project"
print(message.find("Data"))
print(message.index("Engineering"))


# 3.8 isdigit, isalpha, isalnum
# These are validation methods.
# Method	Meaning
# isdigit()	Checks whether all characters are digits
# isalpha()	Checks whether all characters are letters
# isalnum()	Checks whether all characters are letters or digits
# isspace()	Checks whether all characters are whitespace
# islower()	Checks whether all cased characters are lowercase
# isupper()	Checks whether all cased characters are uppercase

employee_id = "12345"
employee_name = "Akash"
product_code = "PRD123"

print(employee_id.isdigit())
print(employee_name.isalpha())
print(product_code.isalnum())


customer_id = "123456"

if customer_id.isdigit():
    print("Valid customer ID")
else:
    print("Invalid customer ID")

# 4.1 String formatting – f-strings
# Used to dynamically create strings.

customer_name = "Akash"
total_sales = 45000

message = f"Customer {customer_name} generated sales of {total_sales}"
print(message)

pipeline_name = "sales_ingestion"
status = "SUCCESS"
records_processed = 150000

log_message = (
    f"Pipeline={pipeline_name}",
    f"Status ={status}",
    f"RecordsProcessed ={records_processed}",
)

print(log_message)

# 4.2 String immutability
# This is an important interview concept.

# Strings in Python are immutable.

# That means you cannot modify an individual character in the original string.

name = "akash"
print(name)

# name[0] ="V" TypeError: 'str' object does not support item assignment
name = "akash"
name = "V" + name[3:]
print(name)


# 4.3 Handling None and empty strings
# This is extremely important in real-world data.

customers = ["Akash", "", None, "  Ravi  ", "Sandeep"]


cleaned_customers1 = []

for name in customers:
    if name is None:
        cleaned_customers1.append(None)
    elif name.strip() == "":
        cleaned_customers1.append(None)
    else:
        cleaned_customers1.append(name.strip())
print(cleaned_customers1)


# 9. Parsing Patterns — Real DE Usage
log = "2024-01-15 ERROR user=john action=login status=failed"
# split() separates a string into a list.
parts = log.split()
date = parts[0]
level = parts[1]

fields = {}
for part in parts[
    2:
]:  # parts[2:]->It means extract all elements starting from index 2 until the end.
    if "=" in part:
        key, value = part.split("=", 1)
        fields[key] = value
# The second argument is maxsplit.
# It tells Python to split only once.

result = {"date": date, "level": level, **fields}
print(result)
# Parse CSV row into dict
# Parse CSV row into a dictionary – Convert raw CSV records into structured records.


def parse_csv_row(header_line, data_line):
    headers = [h.strip() for h in header_line.split(",")]
    values = [v.strip() for v in data_line.split(",")]
    return dict(zip(headers, values))


header = "customer_id, full_name, email, city"
data = "101, Alice Johnson , alice@gmail.com , Mumbai"

record = parse_csv_row(header, data)
print(record)

# Domain extraction from emails

emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "carol@gmail.com",
    "dave@hotmail.com"
]
domain_counts = {}

for email in emails :
    domain= email.split("@")[1]
    print(domain)
    if domain in domain_counts:
        domain_counts[domain]= domain_counts[domain]+1
    else :
        domain_counts[domain] =1
print(domain_counts)