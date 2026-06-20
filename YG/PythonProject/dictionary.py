dis = {1: "TVS", 2: "BMW"}

while True:
    print(dis)
    print("\n**** MENU ****")
    print("1. Add element")
    print("2. Update element")
    print("3. Delete element")
    print("4. Exit")


    choice = int(input("Enter your choice: "))

    if choice == 1:
        # auto-generate next key
        next_key = max(dis.keys()) + 1
        value = input("Enter value: ")
        dis[next_key] = value
        print("Updated Dictionary:", dis)

    elif choice == 2:
        key = int(input("Enter key to update: "))
        if key in dis:
            dis[key] = input("Enter new value: ")
            print("Updated Dictionary:", dis)
        else:
            print("Key not found!")

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        if key in dis:
            dis.pop(key)
            print("Updated Dictionary:", dis)
        else:
            print("Key not found!")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")

"""dictt = {10 : "BMD" , 20 : "car" }
mult = 1
for i in dictt.keys():
    mult = mult * i
print(mult)"""
#
# dis = {}
#
# while True:
#     # auto-generate numeric key
#     next_key = len(dis) + 1
#     value = input("Enter value (or 'stop' to finish): ")
#     if value.lower() == "stop":
#         break
#     dis[next_key] = value
#     print("Current dictionary:", dis)

'''list '''
# keys = []
# mult = 1
#
# while True:
#     key_input = input("Enter numeric key (or 'stop' to finish): ")
#
#     if key_input.lower() == "stop":
#         break
#
#     try:
#         key = int(key_input)
#     except ValueError:
#         print("Key must be a number!")
#         continue
#
#     keys.append(key)
#
# for k in keys:
#     mult *= k
#
# print("All keys:", keys)
# print("Multiplication of keys:", mult)

"""dis = {}
mult = 1

while True:
    key_input = input("Enter numeric key (or 'stop' to finish): ")

    if key_input.lower() == "stop":
        break
    key = int(key_input)

    dis[key] = "value"   # placeholder value

for k in dis.keys():
    mult *= k

print("Dictionary:", dis)
print("Multiplication of keys:", mult)"""


"""dis1 = {1 : "Valu" , 2 : "Valu" ,3 : "Valu" , 4 : "Valu" , 5 : "Valu"}
dis2 = {6 : "Valu" , 7 : "Valu" ,8 : "Valu" , 9 : "Valu" , 10 : "Valu"}

dis1.update(dis2)
print(dis1)"""

# d = {1: "a", 2: "b", 3: "c", 4: "d"}
#
# even_keys = [k for k in d.keys() if k % 2 == 0]
# odd_keys = [k for k in d.keys() if k % 2 != 0]
#
# print("Even keys:", even_keys)
# print("Odd keys:", odd_keys)

# dis = {1:'Car',2:'tempo',3: 'air'}













