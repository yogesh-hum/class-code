from itertools import count

# end = int(input('Enter Your End Value:'))
# i= 1
# while(i<=end):
#     if(i%2==0):
#         print(i , 'EVEN')
#     else:
#         print(i , 'ODD')
#     i+=1

#  FIBONACCI SERIES
# '''
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
#
# '''

# n=10
# a,b=0,1
# d=0
#
# while d < n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     d+=1

'''

a=0
b=1
c=0
d=0

while d <= 10:
    print(c)
    a=b
    b=c
    c=a+b
    d+=1
'''
# while(True):
#     val = int(input("Enter Your Number:"))
#     if(val%2==0):
#         print('It is a Even Number:')
#     else:
#         print('It is a Odd  Number')


















# a = int(input("enter the valu of A",)) #Aditya
# b = int(input("enter the valu of B")) #Anish
# c = 0 #Sushant
#
# print('Before Swapping')
# print('A:',a)
# print('B:',b)
# c=a
# a=b
# b=c
# print('After Swapping')
# print('A:',a)
# print('B:',b)


for i in range(1 , 101):
    for j in range(2 , i):
        if i % j ==0:
            break
    else:
        print(i)
