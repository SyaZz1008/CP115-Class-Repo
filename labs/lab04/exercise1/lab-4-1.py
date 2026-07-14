kwhConsumed = int(input())
if kwhConsumed > 200:
    totalBill = 100 * 0.3 + 100 * 0.5 + kwhConsumed - 200 * 0.75
else:
    if kwhConsumed <= 100:
        totalBill = kwhConsumed * 0.3
    else:
        totalBill = 100 * 0.3 + kwhConsumed - 100 * 0.5
print(totalBill)
