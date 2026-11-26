# 1. What is OOP?
# OOP (Object-Oriented Programming) is a programming approach where we organize code using classes and objects.
# 2. What is a Class?
# A class is a blueprint or template used to create objects.


class Employee:
    def employeedetails(self) :
        print("Employee Name: Akash")
        print("Role: Data Engineer")
        print("Experience: 4 Years")
    # class → Keyword to create a class.
    # Employee → Class name.
    # employee_details() → Method (function inside a class).
    # self → Refers to the current object.

    # 3. What is an Object?
    # An object is an instance of a class.

    # emp = Employee()
    # emp.employeedetails()

    # 4. What is __init__()?
    # __init__() is a special method that initializes an object's attributes when the object is created.

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


def display(self):
    print("Name:", self.name)
    print("Salary:", self.salary)
    print("Department:", self.department)


emp1 = Employee("Akash", 45000, "Data Engineering")
emp2 = Employee("Sai", 55000, "Data Engineering")

emp1.display()
emp2.display()
