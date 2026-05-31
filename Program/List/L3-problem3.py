list_of_int = [5, 10, 92, 20, 2, 30, 3, 76, 15, 66]

sumtotal = 0
count = 0
maxvalue = list_of_int[0]
minvalue = list_of_int[0]

for i in list_of_int:
    sumtotal += i
    count += 1
    
    if i > maxvalue:
        maxvalue = i
        
    if i < minvalue:
        minvalue = i

print("Sum:", sumtotal)
print("Count:", count)
print("Maximum value:", maxvalue)
print("Minimum value:", minvalue)