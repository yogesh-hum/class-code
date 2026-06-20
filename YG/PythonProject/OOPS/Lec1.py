'''
OOPS: Object oriented programming system

CLASS:it is the Blue Print of Program
OBJECT: It is the Instance of Class

how to define class??
1) Always 1st Character should Alpha
2) Class Name cant use a Predefined Keyword
3) Class Name can't be Dublicate in the program
4) Class Defines using "class" keyword
'''


'''
class Lec1: # Defined Cass
    a='Hello' #Property of Class
L1 = Lec1() # Cretad Object for the Class
print(L1.a) # Called the Property using object'''

'''
from datetime import date
class Date:
    def Birday(self):
        age = int(input("Enter your age: "))

        current_year = date.today().year
        birth_year = current_year - age

        print("Your date of birth year is:", birth_year)


by = Date() # Create object
by.Birday() # Call method

ty = Date() # Create object
ty.Birday()'''



'''class Money:
    def convert_doller(self,d):
        print('convert doller to rupees.', d * 88.78)
ps = Money()
d = int(input('Enter your dollars: '))
ps.convert_doller(d)'''


'''class Money:
    def convert_rupees(self,r):
        print("convert rupees into doller.", r * 0.011)
rs = Money()
r = int(input("Enter your rupees."))
rs.convert_rupees(r)'''




'''
1) INHERITANCE
2) POLYMORPHISM
3) ABSTRACTION
4) ENCAPSULATION

'''