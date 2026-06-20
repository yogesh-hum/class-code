'''
for i in range (5): # It is used to Print Row
    for j in range (i+1): # It is Used to print Column
        print('⭐' , end=' ')
    print()'''

# for i in range (5):
#     for j in range (i+1):
#         print(i+1 , end=' ')
#     print()

# for i in range (6):
#     for j in range (1,i+1):
#         print( j, end=' ')
#     print()

# a=1
# for i in range (6):
#     for j in range (i):
#         print( a , end=' ')
#         a+=1
#     print()


# for i in range(5 , 0 , -1):
#     for j in range(i):
#         print(i , end=' ')
#
#     print()


a=15
for i in range (5 , 0 , -1):
    for j in range (i):
        print( a , end=' ')
        a+=-1
    print()
