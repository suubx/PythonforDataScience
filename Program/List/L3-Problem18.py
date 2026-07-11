matrix = []

for i in range(3):
    row = list(map(int, input("Enter 3 numbers: ").split()))
    matrix.append(row)

row_sums = []

for row in matrix:
    row_sums.append(sum(row))

column_sums = []

for column in range(3):
    total = 0

    for row in range(3):
        total = total + matrix[row][column]

    column_sums.append(total)

total_sum = 0

for row in matrix:
    total_sum = total_sum + sum(row)

print("Matrix:", matrix)
print("Row sums:", row_sums)
print("Column sums:", column_sums)
print("Total sum:", total_sum)