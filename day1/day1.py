# A for loop iterates over any iterable (list, tuple, string, range, dict, generator).
# Example 1: Print numbers
for i in range(1, 6):
    print(i)
# Example 2: Iterate over a list
products = ["Laptop", "Mouse", "Keyboard"]

for product in products:
    print(product)

# Example 3: Data Engineering use case
tables = [
    "t_tax_collection",
    "t_tax_transaction",
    "t_pm_transaction",
    "t_pm_parcel",
    "t_pm_remarks",
]

for table in tables:
    print(f"Processing tables :{table}")

# 2. Break Statement
# break immediately terminates the loop when a particular condition is satisfied.

for j in range(1, 10):
    if j == 5:
        break
    print(f"j values {j}")

files = [
    "customers.csv",
    "orders.csv",
    "payments.csv",
    "invalid_file.csv",
    "products.csv",
]

for file in files:
    if file == "invalid_file.csv":
        print("Critical error! Stopping pipeline")
        break

    print(f"{file}")
# Continue Statement
# continue skips the current iteration and moves to the next iteration.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

customers = [
    {"id": 101, "name": "Akash"},
    {"id": None, "name": "Ravi"},
    {"id": 103, "name": "Kiran"},
    {"id": None, "name": "Sai"},
]

for customer in customers:
    if customer["id"] is None:
        continue
    print(customer)
# Enumerate()
# enumerate() returns both the index and value while iterating over a sequence.

tables1 = [
    "t_tax_collection",
    "t_tax_transaction",
    "t_pm_transaction",
    "t_pm_parcel",
    "t_pm_remarks",
]

for index, table1 in enumerate(tables1, start=1):
    print(f"File {index}: Processing {table1}")


# Zip()
# zip() combines multiple iterables element by element.

names = ["Akash", "Ravi", "Kiran"]
salaries = [50000, 60000, 70000]

for name, salary in zip(names, salaries):
    print(name, salary)


tables = ["customers", "orders", "invalid_table", "payments", "products"]

statuses = ["SUCCESS", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]

for index, (table, status) in enumerate(zip(tables, statuses), start=1):
    if table is "invalid_table":
        print(f"error {table} stopping the pipeline")

    if status is "FAILED":
        continue
    print(f"{index} processing {table}")


raw_records = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": None},
    {"id": 3, "amount": 1200},
    {"id": 4, "amount": 800},
    {"id": 5, "amount": 300},
]

max = 3

good = []

for record in raw_records:
    if record["amount"] is None:
        continue
    good.append(record)
    if len(good) >= max:
        break
print(good)


# Question 1 Print numbers from 1 to 20 using a for loop.

for i in range(1, 20):
    print(i)
# Question 2. Print numbers from 1 to 10, but stop when the number reaches 7.

for i in range(1, 10):
    if i == 7:
        break
    print(i)

# Question 3 Print numbers from 1 to 10, but skip all even numbers.

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)


# Question 4. Print employee names with their index starting from 1.

employee_names = ["akash", "sai", "vishal"]

for index, name in enumerate(employee_names, start=1):
    print(index, name)

# Question 5. Combine two lists: employee names and salaries using zip().
employee_names = ["akash", "sai", "vishal"]
employee_salaries = [50000, 60000, 80000]

for data in zip(employee_names, employee_salaries):
    print(data)


dates = ["Nov-01", "Nov-02", "Nov-03", "Nov-04", "Nov-05"]

sales = [2000, 0, 3500, 4100, 2500]
total = 0

for index, (date, sale) in enumerate(zip(dates, sales), start=1):
    if sales == 0:
        continue
    total = total + sale

    if total > 10000:
        print(f"Day{index} |{date} | Sales :{sale} |Total :{total}")
        break
    print(f"Day {index} | {date} | Sales: {sale} | Total: {total}")