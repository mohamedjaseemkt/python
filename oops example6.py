class arithemetic:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("sum is: ",num1 + num2)

    def subtract(self):
        print("subtract :",num1 - num2)

    def multiply(self):
        print("product is: ",num1 * num2)

    def devide(self):
        if self.num2 !=0:
           print("quotent: ",num1 / num2)
        else:
             return"cannot devided by zero"
        
num1 = float(input("enter first number: "))
num2 = float(input("enter your second number: "))

calculator = arithemetic(num1,num2)

calculator.add()
calculator.subtract()
calculator.multiply()
calculator.devide()

        