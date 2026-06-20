'''
for i in range( 0 , 100 , 10):
    print(i)

'''
from unicodedata import digit

'''
a=int(input('Enter the number:'))
for i in range(a, 1, -1):
    print(i)
'''

'''
a=int(input('Enter the number:'))
for i in range(11):
    print(f'{a} X {i} = {a*i}')
'''

#Q1 Stop
''''
b=0
while (True):
    a=int(input('Enter number'))
    if a ==0:
        break
    b += a
print('Total sum',b)
'''

# sum = 0
# for i in range(100):
#     a = int(input('Enter number'))
#     if(a==0):
#         print('On Zero it Will Stop')
#         break
#     else:
#         sum+=a
# print('Sum of Numbers are:',sum)
#
#
# # It will Sum the Number until 0 is press

# num = int(input("Enter Your Value:"))
# digits = 0
# reverse = 0
# original = num
# for i in range(len(str(digits))):
#     digits = num % 10  #Last Value
#     reverse = (reverse * 10)  + digits # To Store the Value in Reverse
#     num = num // 10
# if(reverse == original):
#     print('It is Palindrome')
# else:
#     print('It is Not a Palindrome')


# for i in range(100):
#     if i%2==0:
#         print("even Sum is",i)

# num = int(input("Enter your number"))
# sum_even = 0
# for i in range(100):
#     a = num % 2 == 0
#     if num % 2 == 0:
#         sum_even += a
#         num = num // 10
#         print("even Sum is", sum_even)

val = int(input('Enter Your Number'))
sum = 0
for i in range(val):
    if i%2==0:
        sum+=i
print(sum)

