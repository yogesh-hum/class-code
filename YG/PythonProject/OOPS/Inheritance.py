# 1. Single Inheritance

class Father:
    def FatherProperty(self):
        print('This is Fathers Property')
class Child(Father):
    def ChildProperty(self):
        print('This is Child Property')
C1 = Child()
C1.ChildProperty()
C1.FatherProperty()

'''
class Money:
    def convert_doller(self,d):
        print('convert doller to rupees.', d * 88.78)
ps = Money()
d = int(input('Enter your dollars: '))
ps.convert_doller(d)
class Paisa(Money):
    def convert_rupees(self,r):
        print("convert rupees into doller.", r * 0.011)
rs = Paisa()
r = int(input("Enter your rupees."))
rs.convert_rupees(r)'''

#2.Multilevel Inheritance in Python

'''class A:
    def methodA(self):
        print("A class")

class B(A):
    def methodB(self):
        print("B class")

class C(B):
    def methodC(self):
        print("C class")

c = C()
c.methodA()
c.methodB()
c.methodC()'''

# 3. Multiple Inheritance
'''
class GrandFather:
    def GrandFatherProperty(self):
        print('This is GrandFather Property')
class GrandMother:
    def  GrandMotherProperty(self):
        print('This is GrandMother Property')
class Child(GrandMother,GrandFather):
    def ChildProperty(self):
        print('This is Child Property')
C1 = Child()
C1.ChildProperty()
C1.GrandFatherProperty()
C1.GrandMotherProperty()'''

# 4. Hierarchical Inheritance

'''class GrandFather:
    def GrandFatherProperty(self):
        print('This is GrandFather Property')
class GrandMother:
    def  GrandMotherProperty(self):
        print('This is GrandMother Property')
class Child(GrandMother,GrandFather):
    def GrandMotherProperty(self):
        print('This is Child Property')

m = GrandMother()
c = Child()

m.GrandMotherProperty()
c.GrandMotherProperty()'''