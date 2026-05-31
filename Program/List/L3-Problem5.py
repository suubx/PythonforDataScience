list_of_int = [5, 10, 92, 20, 2, 30, 3, 76, 15, 63]
even_list = []

for i in list_of_int:
    if i%2 == 0:
        even_list.append(i)

print("List:", list_of_int)
print("Even numbers:", even_list)   