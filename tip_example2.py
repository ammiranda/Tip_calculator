from optparse import OptionParser
 
parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", type="float", help="base cost of meal")
parser.add_option("-x", "--tax", dest="tax_percent", type="float" )
parser.add_option("-t", "--tip", dest="tip_percent", type="float", 
                    help="percent tip you want to leave", default=0.20)  
                    #let's accrue good karma by defaulting to a decent 20%
                    #tip!
(options, args) = parser.parse_args()
if not options.meal:
    parser.error("You forgot to indicate th base cost of your meal!")
if not options.tax_percent:
    parser.error("You forgot to indicate the tax rate!")
 
tax_value = options.meal * options.tax_percent
meal_with_tax = tax_value + options.meal
tip_value = meal_with_tax * options.tip_percent
total = meal_with_tax + tip_value
 
print "The base cost of your meal was ${0:.2f}.".format(options.meal)
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        int(100*options.tax_percent), tax_value)
print "The grand total of your meal is ${0:.2f}.".format(total)