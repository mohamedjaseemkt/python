class caculator:
    def enter_variable(self):
        self.num1 = float(input("Enter your first number: "))
        self.num2 = float(input("Enter your second number: "))

    def calculate_variables(self):
        self.sum_result = self.num1 + self.num2
        self.product_result = self.num1 * self.num2

    def display_result(self):
        print("Result:")
        print("sum: ",self.sum_result)
        print("product: ",self.product_result)

caculator_intence = caculator()

caculator_intence.enter_variable()

caculator_intence.calculate_variables()

caculator_intence.display_result()