weight = float(input())
ticketPrice = float(input())
if weight == 0:
    finalPrice = ticketPrice - 10.0
else:
    if weight > 15:
        finalPrice = ticketPrice + weight - 15 * 4.0
    else:
        finalPrice = ticketPrice
print(finalPrice)
