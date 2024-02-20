class numbers:
    def num1(self):
        return int(input("Enter your number: "))

    def calculation(self, a):
        if a % 2 == 0:
            print("This number is even")
        else:
            print("This number is odd")

obj = numbers()
number = obj.num1()  # Call num1 to get the number
obj.calculation(number)  # Pass the number to calculation method
