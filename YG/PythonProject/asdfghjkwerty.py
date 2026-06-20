#
# n = str(input("Enter your Characters"))
# reverse = 0
# while (n > 0):
#
# prin

str = 'ab'

# print(str[::-1]) #REVERSED SLICING
# print(str[0]) # INDEXING
# print(str[1:4]) # SLICING

'''
if(str == str[::-1]):
    print('It is Palindrome')
else:
    print('It is not Palindrome')
    
    total = 0
    total = even + odd
    print(total)'''
'''    
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

print(list_sum(numbers))'''

from multipledispatch import dispatch
# a = int(input('Enter your number'))
# b = int(input('Enter your number'))
# c = int(input('Enter your number'))
# @dispatch(int , int)
# def dis(a,b):
#     return a + b
# @dispatch(int , int , int)
# def dis(a,b,c):
#     return a * b * c
# print(dis(a,b,c))
# print(dis(a,b))

# print("start program")
# try:
#     a=6
#     print(numbers)
# except(ValueError):
#     print("end program")


# if (a,b):
#     @dispatch(int, int)
#     def dis(a, b):
#         return a + b
# el
#     @dispatch(int, int, int)
#     def dis(a, b, c):
#         return a * b * c
#
#
#     print(dis(a, b, c))

'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdrawal(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


w = int(input('Enter your withdrawal: '))
account = BankAccount(1000)

print('Balance:', account.get_balance())
account.withdrawal(w)
print('Balance after withdrawal:', account.get_balance())
'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdrawal(self, amount):
        self.__balance -= min(amount, self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


w = int(input('Enter your withdrawal: '))
account = BankAccount(1000)

print('Balance:', account.get_balance())
account.withdrawal(w)
print('Balance after withdrawal:', account.get_balance())
