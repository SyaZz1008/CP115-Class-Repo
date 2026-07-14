minutesBefore = int(input())
membership = (input().lower == 'true')
if minutesBefore > 30:
    price = 80 - 15
else:
    if minutesBefore < 0:
        price = 0
    else:
        price = 80
if membership:
    price = price - price * 15 / 100
print(price)
