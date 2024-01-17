# Create class in python
class sample:
    def __init__(self):
        pass
    def fun_class(self,name):
        print("Hello " + name)
        
obj = sample()
obj.fun_class("Tiger")

class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def empDetails(employe):
        print("Employee " + employe.name + " is of age " + employe.age)
        
emp = employee("Sathya","13")
emp.empDetails()
print(emp.name)