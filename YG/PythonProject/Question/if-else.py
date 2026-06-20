# Writea program to display given character is vowel or consonan
from idlelib.mainmenu import menudefs

# a=input("enter the word")
#
#
# if a in ("aieouAIEOU"):
#     print("its vowels")
#
# else:
#     print("its consonan")

while(True):
    print("*********** YG Cafe *********")

    print('Press 1 for Dining:')
    print('Press 2 for Home Delivery:')
    choice = int(input('Enter Your Choice:'))
    if (choice == 1):
        print('*** Dining  Mode ***')
        print('Press 1 for Menu:')
        print('Press 2 for Order:')
        print('Press 3 for Payment:')
        choice1 = int(input('Enter Your Choice:'))

        if (choice1 == 1):
            print('*** Menu ***')
            print('1. CHAI     500rs')
            print('2. COFFE     1000rs')
        elif (choice1 == 2):
            print('*** Order ***')
            print('Please give order to waiter..')

        elif (choice1 == 3):
            print('Your payment was successfull')

    elif (choice == 2):
        print('Home deliver is coming soon')
    else:
        print('invalid choice')

# ******dining*****
# press 1 menudefs
# press 2 for oder
# press 3 for paymenet















