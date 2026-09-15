current_reading = int(input())
previous_reading = int(input())

consumption = current_reading - previous_reading

if   consumption == 20:
    water_cost = 0.57 * 20
elif consumption <= 35:
    water_cost = (0.57 * 20) + ((consumption - 20) * 1.03)

print(consumption)
print(water_cost)
print(total_bill)
