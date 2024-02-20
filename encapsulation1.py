class vehicle:
    def __init__(self,name,model):
        self.__model = model
        self._name = name

    def get_model(self):
        return self.__model
    
    def get_name(self):
        return self._name
    def output(self):
        print(self._name,self.__model)

class vehicle_type(vehicle):

    def __init__(self, model, name):
        super().__init__(model, name)


x = vehicle_type("DUKE",2023)

y = vehicle("pulser",2012)

x.output()
y.output()

print("name of the bike: ",x.__model)