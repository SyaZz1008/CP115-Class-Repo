income = float(input())
if income > 100000.0:
    totalTax = 50000.0 * 0 / 100 + 50000.0 * 1 / 100 + income - 100000.0 * 2 / 100
else:
    if income <= 50000.0:
        totalTax = income * 0 / 100
    else:
        totalTax = 50000.0 * 0 / 100 + income - 50000.0 * 1 / 100
print(totalTax)
