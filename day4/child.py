from inheritance import Person


class Employee(Person):
    def __init__(self, f_name, l_name,department,salary):
        super().__init__(f_name, l_name,department,salary)
        
emp =Employee("rahul","More","IT",800000)
emp.printName()
        
    