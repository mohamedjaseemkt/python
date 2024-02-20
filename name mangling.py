class employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

emp = employee("jessa",10005)

print("name: ",emp.name)
print("salary: ",emp._employee__salary)