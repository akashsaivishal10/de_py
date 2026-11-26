class Person:
    def __init__(self,f_name,l_name,department,salary):
        self.first_name=f_name
        self.last_name=l_name
        self.department=department
        self.salary=salary
    
    def printName(self):
        print(self.first_name,self.last_name,self.department,self.salary)
    
    
peron =Person("Akash","Sai Vishal","IT",70000)
peron.printName()