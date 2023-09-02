# The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user.
# Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing.
# The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip.
#
# Criteria:
# Tip is 15 percent of meal amount (without the tax)
# Assume a local tax rate of 21 percent
# Round all numbers up to 3 decimals in the output
#
# Input example:
# Cost of the meal: 23.60
#
# Output example:
# Tax: 4.956 , Tip: 3.540 , Total: 32.096

print("Enter costs of the meal:")
price = float(input())
tip = price / 100 * 15
tax = price / 100 * 21
total = price + tip + tax

print("Meal price: %.3f" % price)
print("Meal tip: %.3f" % tip)
print("Meal tax: %.3f" % tax)
print("Meal total: %.3f" % total)
