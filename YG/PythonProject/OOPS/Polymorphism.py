# Polymorphism:
# Poly : More than One
# Morphism : Forms

# 1) Overriding: Same Function but Different Parameter
# a) We call the Function based on their Parameter itself
# b) pip install multipledispatch
"""from multipledispatch import dispatch
@dispatch(int , int)
def Add(a,b):
    return a+b
@dispatch(int , int , int)
def Add(a,b,c):
    return a*b*c
print(Add(5,5))"""

#
# class Father:
#     def Property(self):
#         print("This is FatherProperty")
# class Son(Father):
#     def Property(self):
#         print("This is SonProperty")
# C1 = Son()
# C1.Property()
# A1 = Father()
# A1.Property()
from multipledispatch import dispatch
@dispatch(int , int)
def Add(a,b):
    return a+b
@dispatch(int , int , int)
def Add(a,b,c):
    return a*b*c
print(Add(5,5 , 45))