# define function??
# It is a Block of code to perform a specific task.

'''
1) Pre-defined function: print() ,input , int() , etc
2) User Defined: Based on User Requirement


def Sushant(): # Created a Function
   print('Hello I am Sushant')

Sushant() # Called the Function
Sushant() # Called the Function


def AreaofCircle(r):#   r is parameter
    print("Area of Circle:" , 3.14 * r * r)

AreaofCircle(5)



def Areaoftrangle(b, h):
    print('Area of trangle..', 0.5 * b * h)
Areaoftrangle(5, 10)

def Areaofrectangle(l,b):
    print("Area of rectrangle.",l*b)
Areaofrectangle(5, 10)
'''

#whire a program convert to doller to rupees, rupees to doller

# def convert_doller(d):
#     print('convert doller to rupees.',d*88.78)
# d=int(input('Enter your doller.'))
# convert_doller(d)
#
#
# def convert_rupees(r):
#     print('convert  rupees to doller.',r*0.011)
# r = int(input('Enter your rupees.'))
# convert_rupees(r)

#whire a program convert to fahrenheit to celcius, celcius to fahrenheit

def fahrenheit(f):
    print('convert fahrenheit to celcius.',(f-32)*5/9,end="C")

def celcius(c):
    print('\n convert celcius to fahrenheit.',(c*9/5)+32,end="F")

print('\n Enter 1 for Fahrenheit to celcius')
print('Enter 2 for Celcius to Fahrenheit')
val = int(input('Enter Your Choice:'))
if(val == 1):
    print('*** Fahrenheit to celcius ***')
    fah = int(input('Enter Your Fahrenheit:'))
    fahrenheit(fah)
elif(val == 2):
    print('*** Celcius to Fahrenheit ***')
    num = int(input('Enter Your celcius:'))
    celcius(num)



