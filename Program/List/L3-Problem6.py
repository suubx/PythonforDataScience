list = [2, 4, 8, 10, 15, 17, 23, 37]

user_input = int(input("Enter an inteegr: "))

if user_input in list: 
    print("Found the number in list")
    position = list.index(user_input)
    print("The position of the number is:", position)
else:
    print("Position not found")
    



