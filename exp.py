
#My first program in Python. Im still learning this programing language.

running = True

while running:
    print("1 = Find Hypotenuse")
    print("2 = Find Base or Height")

    cmd = int(input("Enter number : "))
    if cmd == 1:
        print("Find Hypotenuse")
        first = int(input("Enter Base :"))
        second = int(input("Enter Height :"))
        result = first**2 + second**2
        print(first ,'+' ,second ,'=' , result)
    elif cmd == 2:
        print("Find Base or Height")
        first = int(input("Enter Hypotenuse :"))
        second = int(input("Enter the other Base or Height you know:"))
        result = (first**2 - second**2)**0.5
        print(first ,"-" ,second ,"=" , result)