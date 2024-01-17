class course:
    def __init__(self,name,rating):
        self.name = name
        self.rating = rating
        
    def avgrating(self):
        avg = sum(self.rating)/len(self.rating)
        print("Average rating of {} is {}".format(self.name,avg))
        

s1 = course("c#",[4,4,4,5,3])
s1.avgrating()

s2 = course("Python",[5,5,4,4,3])
s2.avgrating()