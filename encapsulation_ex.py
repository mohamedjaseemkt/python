class bankaccount:
    def __init__(self,a,b):
        self.__a = a
        self._b = b

    def get_a(self):
        return self.__a
        
    def get_balance(self):
        return self._b
    
    def x(self):
         if self._b >0:
            self.__a + self._b
            print(f"add ${self._b}.new balance: ${self.__a}")

            self.__a - self._b
            print(f"subtract {self._b}.balance: {self.__a}")

    def y(self):

        self.__a * self._b
        print(f"divide {self._b}.balance {self.__a}")


account = bankaccount(8,25)

account.x()
account.y()     