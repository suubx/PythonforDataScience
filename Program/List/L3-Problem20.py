runs = []

for i in range(15):
    score = int(input("Enter runs: "))
    runs.append(score)

total_runs = sum(runs)
average_runs = total_runs / len(runs)
highest_score = max(runs)
lowest_score = min(runs)

half_centuries = 0
centuries = 0

for score in runs:
    if score >= 50:
        half_centuries = half_centuries + 1

    if score >= 100:
        centuries = centuries + 1

print("Total runs:", total_runs)
print("Average runs:", average_runs)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Half-centuries:", half_centuries)
print("Centuries:", centuries)