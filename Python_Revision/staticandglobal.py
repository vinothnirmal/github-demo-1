class students:
    dept = "EEE"  # Static or global variable
    
    # Varibales inside the init method are called instance variables
    def __init__(self,name = "NIL",status = "NIL"):
        self.name = name 
        self.status = status
        
    def display(self):
        print("{} of {} department has {} in all the subjects".format(self.name,self.dept,self.status))
        

s1 = students("Vinoth","Failed")
s1.display()

s2 = students()
s2.display()

s1 = students("Sathya","Passed")
s1.display()