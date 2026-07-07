income = float(input())
if income > 100000.0:
    taxPercent = float(2) / 100
else:
    if income == 50000.0:
        taxPercent = float(0) / 100
    else:
        taxPercent = float(1) / 100
totalTax = income + income * taxPercent
print(totalTax)
