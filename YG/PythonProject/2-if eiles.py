a = input("A is ")
b = input("B is ")
c = input("C is ")

if a > b and a > c:
    print(" A is big then B,C")

elif b > a and b > c:
    print("B is big then A,C")

elif a==b==c:
    print("all value is equal")

else:
    print(" C is less then A,B")