# 1.ZeroDivisionError

""""print('Start Program')
try:
    a=int(input("enter a first number:"))
    b=int(input("enter a second number:"))
    print(a/b)
except(ZeroDivisionError):
    print("zero cant be used to dinominator")
print('END Program')"""



# 2.NameError

"""print("start program")
try:
    a=6
    print(numbers)
except(NameError):
    print("end program")"""

# 3.ValueError

"""print("start program")
try:
    a=int(input("enter a first number:"))
    b=int(input("enter a second number:"))
    print(a*b)
except(ValueError):
    print("plese check input")
print("end program")
"""

# 4.IndexError
"""print("start program")
try:
    list=[1,2,3,4,5]
    print(list[8])
except(IndexError):
    print("cant define the position of index")
print("end program")"""

# 5.TypeError
# print("start program")
# try:
#     dict={1:'BMW',2:'farari' , 3:'audi',4:'honda'}
#     print(dict)
# except(TypeError):
#     print("dict cant define type")
# print("end program")

# 6.KeyError

"""print("start program")
try:
    my_dict = {"name": "Aneesh", "age": 30, "course": "BCA"}
    print(my_dict["state"])
except(KeyError):
    print(" cant define the input")
print("end program")"""

#print(***********************YG***********************)
# 7.


'''print('start program')
try:
    list=[1,2,3,4,5,6]
    print(list[8])
except(IndexError):
    print('pagal hai tu')
print('program end')'''

'''print("start program")
try:
    a=int(input('enter your 1st number'))
    b=int(input('enter your 2nd number'))
    print(a / b)
except(ZeroDivisionError):
    print('zero cant be used to dinominator')
except(ValueError):
    print('Input canot be decimal')
print("end program")'''


'''print("start program")
try:
    end = int(input('Enter Your End Value:'))
    i= 1
    while(i<=end):
        if(i%2==0):
          print(i , 'EVEN')
        else:
            print(i , 'ODD')
        i+=1
except(ValueError):
    print('Input canot be literal')
print('program end')'''

# ********File Handling********
'''print("start program")
try:
    filename = input("Enter file name: ")

    # File ko read mode me open karna
    file = open(filename, "r")

    # File ka content print karna
    print("\n--- File Content ---")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: Ye file exist nahi karti! Please correct file name enter karein.")

except Exception as e:
    print("Kuch unexpected error aa gaya:", e)
print('program end')'''


# f1 = open('Aneesh.mp4' , 'w') # 'W' for write
# f1.write("print('Hello Anneesh!!')")
# f1.close()

# f1 = open('Aneesh.jpg' , 'r') # 'r' for Reade
# print(f1.read())
# f1.close()

'''input file save'''
# f1 = open('input.txt', 'w') # 'W' for write
# f1.write(input("store in file"))
# f1.close()

'''cread fill even and odd by uers'''
#

# f1 = open('Even.txt', 'w')
# f2 = open('Odd.txt', 'w')
#
# while True:
#     a = int(input('Enter the number (0 to stop): '))
#
#     if a == 0:   # stop condition
#         break
#
#     if a % 2 == 0:
#         f1.write(str(a) + "\n")
#     else:
#         f2.write(str(a) + "\n")
#
# f1.close()
# f2.close()
#
#
# print("Numbers written successfully!")


"""2 code"""
# f1 = open('Even.txt', 'w')
# f2 = open('Odd.txt', 'w')
#
# # multiple numbers lene ke liye
# a = []
# n = int(input("How many numbers you want to enter? "))
#
# for _ in range(n):
#     num = int(input("Enter the number: "))
#     a.append(num)
#
# even = []
# odd = []
#
# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# # Lists ko string me convert karke write karna
# f1.write(str(even))
# f2.write(str(odd))
#
# f1.close()
# f2.close()
#
# print("Data written to Even.txt and Odd.txt successfully!")

# print('start program')
#
# f1 = open('Even.txt', 'w')
# f2 = open('Odd.txt', 'w')
#
# while True:
#     try:
#         a = int(input('Enter the number (0 to stop): '))
#         if a == 0:  # stop condition
#             break
#
#         if a % 2 == 0:
#             f1.write(str(a) + "\n")
#         else:
#             f2.write(str(a) + "\n")
#     except(ValueError):
#         print('Alphabet canot be save')
# f1.close()
# f2.close()
# print("Numbers written successfully!")
# print('program end')

#create file

'''f1 = open('create file' , 'w' ) # 
f1.write("")
f1.close()'''

#write file

'''f1 = open('write file.txt' , 'w') # 'W' for write
f1.write("With decades of maintenance of way expertise and experience, no one knows the rail like Loram. Today, we’re leveraging our accumulated data, analytics and maintenance algorithms with advanced inspection technologies to provide you actionable intelligence with real-time monitoring and the most precise application of maintenance of way activities. In this new era of digital insight, interval-based maintenance is a thing of the past. Loram delivers on the promise of truly targeted, agile and data-driven solutions, offering unsurpassed efficiency, predictability and return on your maintenance investment.")
f1.close()'''

#Reade file

'''f1 = open('Reade file' , 'r') # 'r' for Reade
print(f1.read('With decades of maintenance of way expertise and experience, no one knows the rail like Loram. Today, we’re leveraging our accumulated data, analytics and maintenance algorithms with advanced inspection technologies to provide you actionable intelligence with real-time monitoring and the most precise application of maintenance of way activities. In this new era of digital insight, interval-based maintenance is a thing of the past. Loram delivers on the promise of truly targeted, agile and data-driven solutions, offering unsurpassed efficiency, predictability and return on your maintenance investment.'))
f1.close()'''

f1 = open(' file.txt' , 'w') # 'W' for write
f1.write("With decades of maintenance of way expertise and experience, no one knows the rail like Loram. Today, we’re leveraging our accumulated data, analytics and maintenance algorithms with advanced inspection technologies to provide you actionable intelligence with real-time monitoring and the most precise application of maintenance of way activities. In this new era of digital insight, interval-based maintenance is a thing of the past. Loram delivers on the promise of truly targeted, agile and data-driven solutions, offering unsurpassed efficiency, predictability and return on your maintenance investment.")
print("With decades of maintenance of way expertise and experience, no one knows the rail like Loram. Today, we’re leveraging our accumulated data, analytics and maintenance algorithms with advanced inspection technologies to provide you actionable intelligence with real-time monitoring and the most precise application of maintenance of way activities. In this new era of digital insight, interval-based maintenance is a thing of the past. Loram delivers on the promise of truly targeted, agile and data-driven solutions, offering unsurpassed efficiency, predictability and return on your maintenance investment.")
f1.close()
