numbers = [100, 200, 300]

numbers.append(400)
print("After append:", numbers)

numbers.insert(1, 150)
print("After insert:", numbers)

numbers.remove(200)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

copied_numbers = numbers.copy()
print("Copied list:", copied_numbers)

numbers.clear()
print("After clear:", numbers)