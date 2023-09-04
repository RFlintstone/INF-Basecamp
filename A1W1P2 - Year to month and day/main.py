# Implement a program that given number of years as input prints the number of months and days as output.
#
# Criteria:
# keep the problem simple
# no leap year
# each year is 365 days and 12 months
# Input example:
# Years: 5
#
# Output example:
# Months: 60, Days: 1825

print("Enter amount of years:")
y = int(input())
m = y * 12
d = y * 365

print("Months: " + str(m))
print(", Days: " + str(d))