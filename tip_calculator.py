import sys

meal = float(sys.argv[1])
tax = float(sys.argv[2])
tip = float(sys.argv[3])

percent_tip = tip / 100
tax_value = meal * (tax / 100)
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * percent_tip
total = meal_with_tax + tip_value

print "The base cost of your meal was $%.2f" % meal
print "You need to pay $%.2f for tax" % tax_value
print "Tipping at a rate of %.0f%%, you should leave $%.2f for a tip." % (tip , tip_value)
print "The grand total of your meal is $%.2f" % (total)