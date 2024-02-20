class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)
    
    def sub(self):
        print(self.a - self.b)
        
    def division(self):
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("Cannot divide by zero")

    def product(self):
        print(self.a * self.b)

# Taking user input for a and b
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# Creating an instance of the class with user input values
result = Arithmetic(a, b)

# Performing arithmetic operations
result.add()
result.sub()
result.division()
result.product()
