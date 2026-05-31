list = [2, 4, 8, 10, 10, 4, 23, 37, 23, 23, 4]

frequency = {}

for number in list:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
 
print("Input", list)       
print("Output:")
for key, value in frequency.items():
    print(f"{key} -> {value}")     