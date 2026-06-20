'''
➡️ __balance private hai

🔑 Encapsulation ke 2 main rules
1.Data hiding → variables private banao (__)
2.Controlled access → public methods (get/set)
'''
'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
d=int(input('Enter your deposit: '))

account = BankAccount(1000)
print(account.get_balance())
account.deposit(d)
print(account.get_balance())'''


# from abc import ABC, abstractmethod

# -----------------------------
# 1️⃣ Abstraction + Encapsulation
# -----------------------------
'''class Vehicle(ABC):  # Abstraction
    def __init__(self, speed):
        self.__speed = speed   # Encapsulation (private variable)

    @abstractmethod
    def drive(self):
        pass

    def get_speed(self):      # Encapsulation → getter
        return self.__speed'''

# -----------------------------
# 2️⃣ Inheritance + Polymorphism
# -----------------------------
'''class Car(Vehicle):          # Inheritance
    def drive(self):          # Polymorphism → override
        print(f"Car is driving at {self.get_speed()} km/h")

class Bike(Vehicle):         # Inheritance
    def drive(self):          # Polymorphism → override
        print(f"Bike is riding at {self.get_speed()} km/h")'''

# -----------------------------
# Use karna
# -----------------------------
'''my_car = Car(120)
my_bike = Bike(80)

my_car.drive()   # Polymorphism
my_bike.drive()  # Polymorphism


class Encp:
    __a = 1000

E = Encp()
print(E.__a)'''

'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdrawal(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
w=int(input('Enter your withdrawal: '))
d=int(input('Enter your deposit: '))
account = BankAccount(1000)
print('Balance:', account.get_balance())
account.withdrawal(w)
print('Balance after withdrawal:', account.get_balance())

account.deposit(d)
print('Deposit', account.get_balance())





