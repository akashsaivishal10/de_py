import json

class MyContext:
    def __enter__(self):
        print("1. Enter method called")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("3. Exit method called")


with MyContext() as obj:
    print("2. Inside with block")


with open("employees.json", "r") as file:
 data = json.load(file)

for employee in data:
    print(employee["name"])