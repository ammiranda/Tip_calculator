meal = 44.50
tax = 0.0675
tip = 0.15
tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print("Base cost of the meal: %r" % meal)
print("Tax amount on the meal: %r" % tax_value)
print("Tip amount on the meal: %r" % tip_value)
print("Total meal cost: %r" % total)