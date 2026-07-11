matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

last_column = []
total = 0

for row in matrix:
    last_column.append(row[2])

    for number in row:
        total = total + number

print("Entire matrix:", matrix)
print("First row:", matrix[0])
print("Last column:", last_column)
print("Sum of all elements:", total)