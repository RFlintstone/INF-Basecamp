# Implement a program that a user enters number of days as input, and the program prints number of hours, minutes and seconds separately as output.
#
# Input example:
# Days: 1
#
# Output example:
# Hours: 24, Minutes: 1440, Seconds: 86400

print("Provide an amount of days")
d = int(input())

hours = d * 24
minutes = hours * 60
seconds = minutes * 60

print("Hours: " + str(hours))
print(", Minutes: " + str(minutes))
print(", Seconds: " + str(seconds))