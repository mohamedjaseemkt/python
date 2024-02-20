class vehicle:
    def __init__(self,model,name):
     self.model = model
     self.name = name

    def output(self):
        print(self.model,self.name)

class two_wheeler(vehicle):
    def __init__(self, model, name):
        super().__init__(model, name)

class four_wheeler(vehicle):
    def __init__(self, model, name):
        super().__init__(model, name)

x = two_wheeler("DUKE",2023)
y = four_wheeler("PAJERO",2014)

x.output()
y.output()


        