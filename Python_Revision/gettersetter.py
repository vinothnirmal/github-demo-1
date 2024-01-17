class employee:
    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setSalary(self,sal):
        self.salary = sal
        
    def getSalary(self):
        return self.salary
    
    def setTechnologies(self,tech):
        self.tech = tech
        
    def getTechnologies(self):
        return self.tech
    

emp = employee()

emp.setName("Vinoth")
emp.setSalary("10000")
emp.setTechnologies(["C#","Biztalk","Python"])

print(emp.getName())
print(emp.getSalary())
print(emp.getTechnologies())
    
    