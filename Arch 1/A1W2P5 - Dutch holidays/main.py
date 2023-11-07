# Make a list of national holidays in The Netherlands (assume current year).
# Write a program that reads a month and day from the user.
# If the month and day match one of the holidays in the list then your program should display the holiday’s name.
# Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.
#
# Criteria:
# Input is given as a comma seperated string: month: 12, Day: 5
# If no holiday is found, print error message: No holiday found on given input
#
# Input example:
# Date: month: 12, Day: 5
#
# Output example:
# Sinterklaas


# Nieuwjaarsdag = month 1, day 1
# Goede Vrijdag = month 4, day 7
# Pasen (eerste en tweede paasdag): month 4, day 9 and 10
# Koningsdag: month 4, day 27 
# Bevrijdingsdag: month 5, day 5 
# Hemelvaartsdag: month 5, day 18 
# Pinksteren (eerste en tweede pinksterdag): month 5, day 28 and 29
# Sinterklaas (avond): month 12, day 5
# Kerstmis (eerste en tweede kerstdag): month 12, day 25 and 26

i = input()

festivities = {
    "month 1, day 1": "Nieuwjaarsdag",
    "month 4, day 7": "Goede Vrijdag",
    "month 4, day 9": "Eerste Paasdag",
    "month 4, day 10": "Tweede Paasdag",
    "month 4, day 27": "Koningsdag",
    "month 5, day 5 ": "Bevreidingsdag",
    "month 5, day 18": "Hemelvaartsdag",
    "month 5, day 28": "Eerste Pinksterdag",
    "month 5, day 29": "Tweede Pinksterdag",
    "month 12, day 5": "Sinterklaas",
    "month 12, day 25": "Eerste Kerstdag",
    "month 12, day 26": "Tweede Kerstdag",
}

if festivities.get(i) is not None:
    print(festivities[i])
else:
    print("Does not exist")
