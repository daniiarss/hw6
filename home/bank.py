class Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key
    def set_name(self,name):...
    def get_name(self):...
# bank.py
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    def display(self):
        print(f"Bank: {self._name}, Balance: {self._balance}")
class NewBank(Bank):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
class BigBank(NewBank):
    def __init__(self, name, balance):
        super().__init__(name, balance)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
from bank import BigBank
bank_instance = BigBank("My Bank", 1000)
bank_instance.name = "New Bank Name "
bank_instance.balance = 2000
print(bank_instance.name)
print(bank_instance.balance)
