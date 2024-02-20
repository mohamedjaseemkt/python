class  car:
    def __init__(self,name,year):
        self.name = name
        self.year = year

    def start(self):
        print("car started")

    def print_details(self):
        print(f"name is {self.name}")
        print(f"year is {self.year}")

c1 = car("swift","2020")
c2 = car("alto",'2017')

c1.start()
c2.start()

c1.print_details()
c2.print_details()

