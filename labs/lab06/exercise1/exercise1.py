# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

coffee_price = 3.50 * 2
muffin_price = 2.10 * 3
water_price  = 1.05 * 4
subtotal     = coffee_price + muffin_price + water_price
tax          = subtotal * 6/100
total        = subtotal + tax

print(f"========== RECEIPT ==========\nItem\tPrice\tQty\tTotal\nCoffee\t$3.20\t2\t${coffee_price}\nMuffin\t$2.10\t3\t${muffin_price}\nWater\t$1.50\t4\t${water_price}\n------------------------------\nSubtotal\t\t${subtotal}\nTax (6%)\t\t${tax}\nTotal\t\t\t${total}\n==============================")