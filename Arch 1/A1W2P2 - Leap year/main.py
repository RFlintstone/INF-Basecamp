# Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that.
# As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years.
# Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.
#
# Criteria:
# Any year that is divisible by 400 is a leap year.
# Of the remaining years, any year that is divisible by 100 is not a leap year.
# Of the remaining years, any year that is divisible by 4 is a leap year.
# All other years are not leap years.
#
# Input examples:
# Year: 2012
# Year: 2011
#
# Output examples:
# Leap year
# Not a leap year

# print casted input
i = float(input())

# leap year dividing by 4
leap = i / 4

# leap year = i
print(i)

# print leap year
print(leap)

# If leap % 2 is uneven, the leap year is uneven. Otherwhise the leap is even.
if leap % 2:
    print("not leap")
else:
    print("leap")
