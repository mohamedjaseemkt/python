class studets:
    def __init__(self):
        self.a = input("enter your name: ")
        self.b = int(input("enter your age: "))

    def details(self):
       print ("name: ",self.a)
       print("age: ",self.b)

result = studets()
result.details()



