kwhConsumed = int(input())
if kwhConsumed > 200:
    usageCharges = 0.75
else:
    if kwhConsumed == 100:
        usageCharges = 0.3
    else:
        usageCharges = 0.5
totalBill = kwhConsumed * usageCharges
print(totalBill)
