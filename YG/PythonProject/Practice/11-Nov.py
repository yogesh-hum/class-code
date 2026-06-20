# Aritametic operators
"""Write a Python program to calculate the area of a circle given its radius (use ** for exponentiation)."""

# radius = float(input("Enter the radius: "))
# area = 3.14159 * (radius ** 2)
# print("Area of circle =", area)


"""Write a Python expression to convert 5 hours into seconds using only arithmetic operators."""

time = int(input("Time"))
seconds = time * 60 * 60
print(seconds)

'''1. Operator Precedence
What will be the output of the following code?'''

# print(10 + 5 * 2 ** 3)

"""2. Mixed Operations
Predict the result:"""

#x = 20
# y = 5
# z = 2
# result = x / y + x // y - x % y * z
# print(result)

'''4. Floating vs Integer Division'''
# x = 7 / 2
# y = 7 // 2
# print(x, y)

'''comparision opereter Challenging Level  question'''

'''1. Chain Comparison
What will this print?'''

# a = 5
# b = 10
# c = 15
# print(a < b < c)

'''2. Mixed Comparison and Arithmetic
Predict the output:'''

# x = 8
# y = 4
# print(x / 2 == y and x % 3 != 2)

"""if else"""

# num = int(input("Enter the number"))
# if num %2==0:
#     print( " it,s event")
# else:
#     print(" odd")

'''2. Greatest of Three Numbers
Find the largest among three numbers using if...elif...else.'''

a=int(input('Enter the number A :'))
b=int(input('Enter the number B :'))
c=int(input('Enter the number C :'))

if a > b and a > c:
    print("A is Greatest ",a)
elif b > a and b > c:
    print("B is Greatest ",b)
else :
    print("C is Greatest ",c)