from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--first", dest="meal", type="float", help="meal amount")
parser.add_option("-s", "--second", dest="tax", type="float", help="tax rate")
parser.add_option("-t", "--third", dest="tip", type="float", help="tip rate", default=0.20)

(options, args) = parser.parse_args()
 
tax_value = options.meal * options.tax
meal_with_tax = tax_value + options.meal
tip_value = meal_with_tax * options.tip
total = meal_with_tax + tip_value
 
print "The base cost of your meal was ${0:.2f}.".format(options.meal)
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                                        int(100*options.tax), tax_value)
#note how we split up the line above across two lines. this is because
#the best practice in Python is to not exceed 80 characterse per line.
#This makes it much easier for you and others to read your code -- you don't have
#to scroll to read!
 
print "The grand total of your meal is ${0:.2f}.".format(total)