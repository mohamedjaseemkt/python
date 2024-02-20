
class arithametic:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("Sum is :", self.num1 + self.num2) 

    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 !=0:
            return self.num1 / self.num2 
        else:
            return"cannot devided by zero"
        
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

calculator = arithametic(num1,num2)

 
calculator.add()
print("differevce",calculator.subtract())
print("product",calculator.multiply()) 
print("quotient",calculator.divide())     