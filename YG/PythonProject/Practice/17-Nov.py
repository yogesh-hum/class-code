# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 18:44:51 2025

@author: Admin
"""

"""loop"""

"""Q1 Print numbers from 1 to 50 using a for loop."""
'''
for i in range(1,51):
    print(i)'''

"""Q2 Print only even numbers from 1 to 100."""
'''
for i in range(1,101):
    if(i % 2 == 0):
        print('even',i)'''
   
"""Q3 Sum all numbers from 1 to 100 usin'g a "loop"."""
'''
total = 0
for i in range(1,101):
    total+=i
print("Sum",total)'''
    
"""Q4 Count how many times the letter "a" appears in a string."""
'''
string = str(input('Enter Your String : '))

Count = 0
for char in string:
    if (char == "a"):
        Count+=1
print(Count)'''
'''
a=[1,2,3,4,5]
b=[6,7,8,9,0]
c=[]
for i in a:
    c.append(i)
    
for i in b:
    c.append(i)
    
print(c)'''

Adj=["red","big","tasty"]
Fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        Print(x,y)








