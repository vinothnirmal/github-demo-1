class patient:
    def setID(self,iD):
        self.__ID = iD
    
    def getID(self):
        return self.__ID
        
    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setSSN(self,ssn):
        self.ssn = ssn
    
    def getssn(self):
        return self.ssn
    
pt = patient()

pt.setID("123")
pt.setName("Vinoth")
pt.setSSN("123")

print(pt.getID())
print(pt.getName())
print(pt.getssn())