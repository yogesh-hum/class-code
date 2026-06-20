

# list=[1,'aneesh', 'a','true']
# print(list)
# print(list[1])# indexing
# print(list[1:4])# slicing
# list.append("SAHANI")#inserting at last position
# print(list)
# list.pop(1)
# print(list)
# list.reverse()
# print(list)

# """# 2.write a program of list declare(1,2,3,4,5)calculate the sum
# """list=[1,2,3,4,5]
# total=sum(list)
# print('sum:',total)"""
# from random import choice
#
# # 3.for looop
# """numbers= [1,2,3,4,56]
# total=0
#
# for num in numbers:
#     total += num
# print("sum:",total)"""
# # 4.take 5 numbersfrom user
# """nums = []
# for i in range(5):
#     n = int(input("Enter a number: "))
#     nums.append(n)
# print("List:", nums)"""
#
# # 5.largest and smallest number
# """nums=[20,30,45,67,8]
# print("Largest:", max(nums))
# print("Smallest:", min(nums))""""""


#####list####
list=[]
print(list)
while(True):
    print('****element list****')
    print('press 1 for add list:')
    print('press 2 for update:')
    print('press 3 delete:')
    choice = int(input("Enter your choice1:"))
    if(choice==1):
        add=int(input("enter add list:"))
        list.append(add)
        print(list)
    elif choice==2:
        index = int(input('Enter Your Index Posistion:'))
        update = int (input('Enter Your Element to be update'))
        list[index] = update
        print(list)
    elif choice==3:
        dele =int(input("enter add delete:"))
        list.remove(dele)
        print(list)














