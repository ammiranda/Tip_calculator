import sys
from tip_calculator_as_functions import calculate_rate, calculate_meal_costs

def grab_data():
	while True:
		try:
			meal = float(raw_input("Meal cost: "))
			tax = float(raw_input("Tax rate: "))
			tip = float(raw_input("Tip rate: "))
			break
		except ValueError:
			print "All values should be numbers!"
		return meal, tax, tip
		
def main():
	try:
		meal = float(sys.argv[1])
		tax = float(sys.argv[2])
		tip = float(sys.argv[3])
	except ValueError:
		print "All values should be numbers!"
		meal, tax, tip = grab_data()
	except IndexError:
		print "You didn't enter all of the needed values!"
		meal, tax, tip = grab_data()
	
	tax_value = meal * tax
	meal_with_tax = meal + tax_value
	tip_value = meal_with_tax * tip
	total = meal_with_tax + tip_value
	
	print "The untaxed cost of the meal is ${0:.2f}".format(meal)
	print "The tax on the meal is ${0:.2f}".format(tax_value)
	print "To tip at the rate of {0:.2%}, leave ${1:.2f}".format(tax, tip_value)
	print "The combined total for the meal is ${0:.2f}".format(total)
	
if __name__ == "__main__":
	main()