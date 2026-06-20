'''
Characters:
1) Letters
2) Digits
3) Special Symbol

String: It is Set of Character

str = admin@123
name = 'Aneesh'

num = '123456'

'''


#
# name = input('Enter Your Name:')
# #print(name.upper())
# #print(name.lower())
# r1 = name.islower()
# print(r1)
# rep = r1.replace('A','$')
# print(rep)




"""Write a program use to string of all length"""

# string = input("Enter a string")
# lower = 0
# upper = 0
# symbol = 0
# int = 0
# for char in string:
#     if char.islower():
#         lower += 1
#     elif char.isupper():
#         upper += 1
#     elif char in "!@$%^&*":
#         symbol += 1
#     elif char.isdigit():
#         int +=1
#
# print("number of lower", lower)
# print("number of upper", upper)
# print("number of simbol", symbol)
# print("number of int", int)

"""Write a program to used string replace"""

# name = input('Enter Your Name:')
# a=input('Enter the Character to be Replace:')
# b=input('Enter the Character to be replace With:')
# r1 = name.replace(a,b)
# print(r1)

"""Write a program to revers Character"""

# r = str(input("Enter your Character: "))
# print(''.join(reversed(r)))

"""Write a program """

char = input("Enter your Character")
print(char[::-1])
if (char == char[::1] ):
    print('it,s a palindrome')
else:
    print('it,s not palindrome')
