class calculation:
    def num1(self):


        a = int(input("Enter your nuber: "))

        if (0 < a):
            print("This number is positive")

        elif (0 > a):
            print("This number is negative")

        else:
            print("This number is zero")

obj = calculation()
obj.num1()