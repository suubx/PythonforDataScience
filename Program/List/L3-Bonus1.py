numbers = [10, 40, 20, 40, 30]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

unique_numbers.sort(reverse=True)

print("Second largest:", unique_numbers[1])