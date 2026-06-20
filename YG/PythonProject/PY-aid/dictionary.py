# dis ={1:"chai", 2:"tea"}
# dis[1] = 'Gane ka juice'
# print(dis)
# dis.pop(1)
# print(dis)
# dis[3]= "mosambi KA JUICE"
# print(dis)
dis = {1: "TVS", 2: "BMW"}

while True:
    print(dis)
    print("\n**** MENU ****")
    print("1. Add element")
    print("2. Update element")
    print("3. Delete element")
    print("4. Exit")
    choice =int(input("enter your choice"))
    if choice ==1:
        index= int(input("enter a key"))
        value=input("enter value to insert:")
        dis[index] = value
        print(dis)
    elif choice == 2:
        key = int(input("enter a key to update"))
        value=input("enter a value to update")
        dis[key] = value
        print(dis)
    elif choice == 3:
        key = int(input("enter a key to delete"))
        dis.pop(key)
    elif choice == 4:
        print("bye")
        break






