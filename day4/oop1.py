class Employee :
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department =department
    def display_details(self):
        print("name",self.name)
        print("salary",self.salary)
        print("department",self.department)

emp = Employee("Akash",45000,"DE")
emp1 = Employee("Sai",55000,"DE")
emp.display_details()
print("---------")
emp1.display_details()