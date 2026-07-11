numbers = [x for x in range(1, 21)]
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
squares = [x * x for x in range(1, 11)]

print("Numbers from 1 to 20:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Squares:", squares)