# #01_Write a Python Program to print "Hello World".
#
#
# print("Hello World.")
#
# #02_Take two number as input and print their sum.
#
# a=int(input("enter the number"))
# b=int(input("enter the number"))
#
# print(a+b)
#
# #03_check whether a given number is even or odd
#
# a=int(input("enter the number"))
#
# if a % 2 == 0:
#     print("this is a even number")
# else:
#     print("this is a odd number")
#
# #04_Find the largest of three number entered by the user.
#
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
#
# if a > b and a > c:
#     print(a," is largest then",b,a)
#
# elif b > a and b > c:
#     print(b," is largest then",a,c)
#
# else:
#     print(c," is largest then",a,b)
#
#05_Print the multiplication table of a number(e.g.,5)

a=int(input("enter the number"))

for i in range(1,11):
    print(f"{a}x{i}={a*i}")
#
# #06_Count the number of vowels in a given string.
# #
# a=str(input("enter the word"))
# b = "aeiouAEIOU"
#
# count = sum(map(a.count,b))
#
# print("Number of vowels is ",count)
#
# 07_reverse a string entered by user


