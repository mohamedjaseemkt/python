class my_class:
    def __init__(self,name):
        self.name = name

    def __del__(self):
        print(f"destroying the object {self.name}")

obj = my_class("Example")

del obj

 
        