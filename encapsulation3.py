class student:
    def __init__(self,name,age):
       self.name = name
       self.__age = age

    #getter method
    def get_age(self):
        return self.__age
    
    #setter method
    def set_age(self,age):
        self.__age = age

stud = student("jessa",15)

#retreiving age using getter
print("name:" , stud.name,stud.get_age())

#changing age using setter
stud.set_age(18)

print("name:" , stud.name,stud.get_age())
