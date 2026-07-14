totalHours = int(input())
if totalHours > 5:
    parkingFee = 2 * 0 + 3 * 2.0 + totalHours - 5 * 3.0
    if parkingFee > 30.0:
        parkingFee = 30.0
else:
    if totalHours <= 2:
        parkingFee = 0
    else:
        parkingFee = 2 * 0 + totalHours - 2 * 2.0
print(parkingFee)
