class numbers:

    def num1(self):
       a = int(input("Enter your number: "))
       if a%2 == 0:
          print("this number is even")
       else:
          print("this nuber is odd")


obj = numbers()

obj.num1()