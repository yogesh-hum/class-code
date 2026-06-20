class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdrawal(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
print('***********ATM***********')

print('1 Balance\n'
      '2 Withdrawal\n'
      '3 Deposit\n')
a = int(input('Enter your value'))
account = BankAccount(1000)
if(a==1):
    print('Balance: ', (account.get_balance()))
elif(a==2):
    w = int(input('Enter your withdrawal: '))
    print('Withdrawal', account.get_balance())
    account.withdrawal(w)
elif(a==3):
    d=int(input('Enter your deposit: '))
    account.deposit(d)
    print('Deposit', account.get_balance())

