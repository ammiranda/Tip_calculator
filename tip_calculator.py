meal = raw_input("Enter the cost of your meal before tax: ")
tax = raw_input("Enter the tax on your meal as a percent: ")
tip = raw_input("Enter the tip percentage you want to pay: ")
percent_tip = float(tip) / 100
tax_value = float(meal) * (float(tax) / 100)
meal_with_tax = float(meal) + tax_value
tip_value = meal_with_tax * percent_tip
total = meal_with_tax + tip_value

print "The base cost of your meal was $%.2f" % float(meal)
print "You need to pay $%.2f for tax" % tax_value
print "Tipping at a rate of %.0f, you should leave $%.2f for a tip." % (float(tip) , tip_value)
print "The grand total of your meal is $%.2f" % (total)