class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname,self.lname)
    
class student(person):
    def __init__ (self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

x = student("mike","olsen",2019)
print(x.graduationyear)
x.printname()
