prime_numbers = [
    number
    for number in range(2, 101)
    if len([
        divisor
        for divisor in range(2, number)
        if number % divisor == 0
    ]) == 0
]

print(prime_numbers)