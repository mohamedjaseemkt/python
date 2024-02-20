class bankaccount:
    def __init__(self,account_holder,balance):
        self.__account_holder = account_holder
        self._balance = balance

    def get_account_holder(self):
        return self.__account_holder
        
    def get_balance(self):
        return self._balance
    
    def deposite(self,amount):
        if amount >0:
            self._balance += amount
            print(f"deposite ${amount}.new balance: ${self._balance}")
        else:
            print("invalid deposite amount")

    def withdraw(self,amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"withdraw $ {amount}. new balance: {self._balance}")

        else:
            print("invalid withdraw amount or insufficient balance")

account = bankaccount("jaseem",2500)

print(f"account holder: {account.get_account_holder()}")
print(f"initial balance: ${account.get_balance()}")

account.deposite(600)
account.withdraw(250)
