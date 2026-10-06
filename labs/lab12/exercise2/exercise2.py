for number in range (1, 100 + 1):
    if number % 7 == 0 and number % 13 == 0:
        found_number = number
        break

print(found_number)
