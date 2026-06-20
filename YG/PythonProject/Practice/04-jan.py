#Q1 Create a class Student with private variables __name and __marks.
#   Provide methods to set and get their values.

'''class Student:
    def __init__(self):
        self.__name = ""
        self.__marks = 0

    def set_name(self, name):
        self.__name = name


    def get_name(self):
        return self.__name


    def set_marks(self, marks):
        self.__marks = marks


    def get_marks(self):
        return self.__marks

s1 = Student()

s1.set_name("Rahul")
s1.set_marks(85)

print("Name:", s1.get_name())
print("Marks:", s1.get_marks())'''

# Q2 Write a class BankAccount with private data member __balance.
#    Implement methods deposit(), withdraw(), and get_balance().

'''print('***********ATM***********')

print('1 Balance\n'
      '2 Withdrawal\n'
      '3 Deposit\n')

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
print('Deposit', account.get_balance())'''

num =[1,2,3,4,5,6,7,8,9,10,11,12]
even = []
odd= []
for i in num:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(num)
print("even",even)
print("odd",odd)
