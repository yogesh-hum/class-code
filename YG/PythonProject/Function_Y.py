"""whire a program convert to doller to rupees, rupees to doller"""

# def convert_doller(d):
#     print('convert doller to rupees.', d * 88.78)
# d=int(input('Enter your doller.'))
# convert_doller(d)
#
# def convert_rupees(r):
#     print("convert rupees into doller.",r * 0.011)
# r=int(input("Enter your rupees."))
# convert_rupees(r)

"""writr a program to ues reverse number"""

def reversed(n):
    reverse = 0
    while (n > 0):
        digit = n % 10
        reverse = (reverse * 10) + digit
        n = n // 10
    print(reverse)
n = int(input("Enter your number"))
reversed(n)

"""writr a program count in length"""

# def len(name):
#     count = 0
#     for i in name:
#         count+=1
#     print('The Length of my Name is:', count)
# name = input('Enter Your Name:')
# len(name)

"""---------------------------------------------"""

# def len(str):
#     vowel = 0
#     consonant = 0
#     for char in string.lower():
#         if char in "aeiou":
#             vowel += 1
#         else:
#             consonant+=1
#     print("number of vowels:",vowel)
#     print("number of consonant",consonant)
# string = input("Enter a string")
# len(0)

"""------------------------------------"""

# def len(str):
#     vowel = 0
#     consonant = 0
#     symbol = 0
#     int = 0
#     for char in string.lower():
#         if char in "aeiou":
#             vowel += 1
#         elif char in "!@$%^&*":
#             symbol += 1
#         elif char in "1234567890":
#             int +=1
#         else:
#             consonant+=1
#     print("number of vowels:",vowel)
#     print("number of consonant",consonant)
#     print("number of simbol", symbol)
#     print("number of int", int)
# string = input("Enter a string")
# len(0)

"""Write a program to ues function square and cube print"""

# def Sq(n):
#     print("Squere:",n*n)
#     print("Cube:",n*n*n)
# n=int(input("Enter the number:"))
# Sq(n)

"""Write a program to use formula Square"""

# def formula(a,b):
#     return ((a*a)+(2*a*b)+(b*b))
# a=int(input("Enter the number A:"))
# b=int(input("Enter the number B:"))
# print(formula(a,b))

"""Write a program to use formula cub"""

def formula(a,b):
    return ((a*a*a)+3*(a*a*b)+3*(a*b*b)+b*b*b)
a=int(input("Enter the number A:"))
b=int(input("Enter the number B:"))
print(formula(a,b))