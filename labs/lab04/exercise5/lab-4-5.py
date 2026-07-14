scoreA = int(input())
scoreB = int(input())
if scoreA == scoreB:
    pointsA = 1
    pointsB = 1
else:
    if scoreA > scoreB:
        pointsA = 3
        pointsB = 0
        if scoreB == 0:
            pointsA = pointsA + 1
    else:
        pointsB = 3
        pointsA = 0
        if scoreA == 0:
            pointsB = pointsB + 1
print(pointsA)
print(pointsB)
