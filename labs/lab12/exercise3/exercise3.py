grade = float(input())
valid_count = 0
total_grade = 0

while grade != -1:
    if grade < 0 or grade > 100:
        continue

    total_grade += grade
    grade = float(input())
    valid_count += 1

average = total_grade/valid_count

print(valid_count)
print(f"{average:.2f}")
