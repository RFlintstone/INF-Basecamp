# Write a program that reads a date from the user and computes its immediate successor.
#
# Criteria:
# The date will be entered in YYYY-MM-DD format.
# Assume there is no leap year and February is always 28 days.
# The program must print Input format ERROR. Correct Format: YYYY-MM-DD in case the user enters an incorrect input.
# Some examples of incorrect input: 2013/12/30, 2013_12_30, 0213/12/30, 30-12-2013.
#
# Input examples:
# Input Date: 2013-11-18
# Input Date: 2013-11-30
# Input Date: 2013-12-31
#
# Output examples:
# Next Date: 2013-11-19
# Next Date: 2013-12-01
# Next Date: 2014-01-01

def validate(date_text):
    year = date_text[0:4]
    month = date_text[5:7]
    day = date_text[8:10]
    if int(year.replace('-','')) >= 2000:
        return f'{year}-{month}-{day}'
    elif int(year.replace('-','')) < 1900:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
    else:
        print("What happened?")


def shiftYear(date_text, shift):
    year = int(date_text[0:4]) + shift
    return str(year) + "-01-01"


def shiftMonth(date_text, shift):
    month = int(date_text[5:7]) + shift
    return date_text[0:4] + "-" + str(month) + "-01"


def shiftDay(date_text, shift):
    day = int(date_text[8:10]) + shift
    day_str = str(day)
    if len(day_str) < 2:
        day_str = "0" + day_str
    return date_text[0:7] + "-" + day_str


def dateInput(input):
    i = validate(input)
    if i != None:
        i = shiftDay(i, 1)
        print("Next Date: " + i)
        i = shiftMonth(i, 1)
        print("Next Date: " + i)
        i = shiftYear(i, 1)
        print("Next Date: " + i)


def main():
    date_input = input()
    dateInput(date_input)


main()
