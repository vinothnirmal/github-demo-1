class car:
    def __init__(self,name,year):
        self.name = name
        self.year = year
        
    class engine:
        def __init__(self,number):
            self.number = number
        def start(self):
            print("Engine started")

c = car("BMW","1988")
e = c.engine("True")
e.start()

c = car("Maruthi","1998")
e = c.engine("False")
e.start()

            