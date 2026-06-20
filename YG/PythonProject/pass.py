# Name=input("Enter your name")
# Password=int(input("Enter Your Password"))


# if Password=="6069":
#     print("loging sucessfull")
#
# else:
#     print("incorrect your Password")

#__________________________________________________________

# if Name=="yg":
#     print("enter your pass")
#     if Password == "6069":
#         print("loging sucessfull")
#
#     else:
#         print("incorrect your Password")
#
# else:
#     print(" loging fail")

#__________________________________________________________

# if Name=="yg" and Password==12:
#     print("loging Sucessfull")
#
#
# # elif Name=="yg" and Password!= 12:
# #     print("incorrect your Name")
#
# elif Name=="yg" and Password!= 12:
#     print("incorrect your Password")
#     print("loging fail")
# else:
#     print("incorrect your Name")
#     print("loging fail")

#__________________________________________________________

# a = int(input("enter the number"))
# # b = input("enter the number")
#
# user=2004
# # user1=5
#
# if (a %2==0 and  a % 100!=0) or (a %400 == 0):
#     print("leap year")
#
# else:
#     print("not leap yera")


#__________________________________________________________
#
a=input("enter the number")

if a.isdigit():
    num=int(a)
    if a==0:
        print("It is not even and odd")

    elif num%2==0 :
        print("this is a even number")

    else :
        print("this is a odd number")
else:
    print("it is a straing")

#
# num%2==0 :
#         print("this is a even number")
#
# num%0==0:
#         print("It is not even and odd")