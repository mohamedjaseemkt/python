class company:
    def __init__(self):
       self._project = "NLP"

class employee(company):
    def __init__(self,name):
         self.name = name
         company.__init__(self)

    def show(self):
        print("employee name: ",self.name)
        print("working on project : ",self._project)

c = employee("jaseem")
c.show()

print("project: ",c._project)