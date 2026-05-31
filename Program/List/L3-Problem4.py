list = [2, 4, 8, 10, 15, 17, 23, 37]

evencount = 0
oddcount = 0

for i in list:
    if i%2 == 0:
        evencount += 1
    else:
        oddcount += 1
    
print("Even count:", evencount)
print("Odd count:", oddcount)

    