#Q1 to 50 print in loop

'''for i in range(1,51):
    print(i)'''
#Q2 1 to 100 only even umber in loops

'''for i in range(1,101):
    if i %2==0:
        print(i , " is even number")'''

#Q3 1 to 100 only odd number in loops

'''for i in range(1,101):
    if i %2!=0:
        print(i , " is odd number")'''

#Q4 1 to 10 reverse print in loop

'''for i in range(10, 0, -1):
    print(i)'''

#Q5 print 5 table in format

'''for i in range(1,11):
    print(f"{5}x{i}={5*i}")'''

#Q6 sum 1 to 50 loop

"""sum = 0
for i in range (1 , 51):
    sum+= i
    print("Sum =", sum)
    """
#Q7 print 1 to 10 squares

'''for i in range (1,11):
    print(i*i)'''

#Q8. 1 to 10 tak cubes print karo.

'''for i in range (1,11):
    print(i*i*i)'''

#9. 1 to 100 me kitne even aur odd numbers hain — count karo.
'''e=0
o=0

for i in range(1,101):
    if i %2==0:
        e+=1
    else:
        o+=1
print("Total even number is",e)

print("Total odd number is",o )'''

#10. 1 to 100 ka sum of even aur sum of odd alag alag nikal

'''even_sum = 0
odd_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)'''

#11. Kisi number ka factorial nikal (input se).

'''num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is =", fact)'''

#12. Kisi number ke factors print kro.

'''num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)'''

#13 Fibonacci series (10 numbers).

n=10
a,b=0,1
d=0

while d < n:
    print(a)
    c=a+b
    a=b
    b=c
    d+=1



