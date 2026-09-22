num_rounds = int(input())
final_score = 0

for rounds_processed in range (1, num_rounds + 1):
    score = float(input(f"Your score for round {rounds_processed}: "))
    if score > 100:
        score = score + (score * 0.20)
        final_score += score 
    else:
        final_score += score

    rounds_processed += 1
         
print(f"{final_score:.1f}")
print(num_rounds)
