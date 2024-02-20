class Mark:
    def __init__(self, name, rollnumber, score):
        self.name = name
        self.rollnumber = rollnumber
        self.score = score

    def start(self):
        print("The marks are....")

    def print_details(self):
        print(f"Name is {self.name}")
        print(f"Roll number is {self.rollnumber}")
        print(f"Score is {self.score}")  # Corrected the typo from mark to score

mark1 = Mark('basith', 12, 9)
mark2 = Mark('shahanas', 13, 3)

mark1.start()
mark2.start()

mark1.print_details()
mark2.print_details()
