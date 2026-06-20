# listt = [1 , 'Aneesh' , 'a' , True]
# print(listt)
# print(listt[1]) #indexing
#
# print(listt[1:4]) #Slicing
#
# listt.append('Yogesh')  # Inserting at last posititon
# print(listt)
#
# listt.insert(2, 'Aditya')
# print(listt)
#
# listt[1] = 'Niranjan' #Updating at specific Position
# print(listt)
#
# listt.pop(1)
# print(listt)
#

'''Q2 list declare' 1234 SUM'''
from idlelib.replace import replace

'''
numbers = [1, 2, 3, 4, 5]

def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

print(list_sum(numbers))'''

'''Q3 find even and odd
        add even and odd'''
       
# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# even = []
# odd= []
# for i in a:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(a)
# print("even",even)
# print("odd",odd)
#
#
# num = 0
# for i in a:
#     num+=i
# print('Total:',num)
#
# Enum = 0
# for i in even:
#     Enum+=i
# print('Even:',Enum)
#
# Onum = 0
# for i in odd:
#     Onum+=i
# print('Odd:',Onum)
#
# if num == (Enum+Onum):
#     print(' its ok')
# else:
#     print('Not ok')
    
'''Q3 '''
'''
a=[1,2,3,4,5]

num = 1
for i in a:
    num *= i
print(num)'''

#####list####
# list=[]
# print(list)
# while(True):
#     print('****element list****')
#     print('press 1 for add list:')
#     print('press 2 for update:')
#     print('press 3 delete:')
#     choice = int(input("Enter your choice1:"))
#     if(choice==1):
#         add=int(input("enter add list:"))
#         list.append(add)
#         print(list)
#     elif choice==2:
#         index = int(input('Enter Your Index Posistion:'))
#         update = int (input('Enter Your Element to be update'))
#         list[index] = update
#         print(list)
#     elif choice==3:
#         dele =int(input("enter add delete:"))
#         list.remove(dele)
#         print(list)


listt = [1 , 'Aneesh' , 'a' , True]
print(listt)
 #Updating at specific Position

a = listt[1]
to_replace = input('Enter the Charctarte to Replce:')
to_replace_with = input('Enter the Charctarte to Replced:')
ab = a.replace( to_replace , to_replace_with)
listt[1] = ab
print(listt)





