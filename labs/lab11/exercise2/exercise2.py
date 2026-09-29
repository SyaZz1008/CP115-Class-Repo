score = int(input("Enter score (-1 to stop): "))
round = 0
total_a = 0
total_b = 0

while score != -1:
    round += 1

    if round % 2 == 0:
        total_b += score
    else:
        total_a += score

    score = int(input("Enter score (-1 to stop): "))

if total_a > total_b:
    winner = "A"
elif total_b > total_a:
    winner = "B"
else:
    winner = "Tie"
    
print(total_a)
print(total_b)
print(winner)
