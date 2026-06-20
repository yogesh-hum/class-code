"""Q1 Write a program Display first n 
numbers of a Fibonacci series"""
'''
n = int(input("Enter your fist number : "))
a,b = 0,1

print('Fibonacci series') 
for i in range(n):
    print(a , end=" ")
    a, b = b, a+ b'''
    
"""Q2 Write a program to store seven fruits in a list entered by the user. ."""

fruits = []

f1 = input("Enter marks name: ")
fruits.append(f1)
f2 = input("Enter marks name: ")
fruits.append(f2)
f3 = input("Enter marks name: ")
fruits.append(f3)
f4 = input("Enter marks name: ")
fruits.append(f4)
f5 = input("Enter marks name: ")
fruits.append(f5)
f6 = input("Enter marks name: ")
fruits.append(f6)
f7 = input("Enter marks name: ")
fruits.append(f7)

print(fruits)