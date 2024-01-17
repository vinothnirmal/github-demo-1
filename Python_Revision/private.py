class employee:
    def __init__(self):
        self.__id = "123"
        self.name = "Vinoth"
        
    def display(self):
        print("From method",self.__id,self.name)
    

emp = employee()
print(emp._employee__id)   #private variables can be accessed through name mangling syntax
print(emp.name)
emp.display()