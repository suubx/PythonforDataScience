marks = []

for i in range(10):
    mark = int(input("Enter mark: "))
    marks.append(mark)

highest_mark = max(marks)
lowest_mark = min(marks)
average_mark = sum(marks) / len(marks)

above_average = 0

for mark in marks:
    if mark > average_mark:
        above_average = above_average + 1

print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)
print("Average mark:", average_mark)
print("Students above average:", above_average)