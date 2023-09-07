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
import datetime

def validate(date_text):
    try:
        return datetime.date.fromisoformat(date_text)
    except:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")


def dateInput(input):
    x = validate(input)
    if x != None:
        datetime.date = x
        datetime.date = datetime.date.replace(day=datetime.date.day + 1)
        print(datetime.date)
        datetime.date = datetime.date.replace(month=datetime.date.month, day=1)
        print(datetime.date)

def main():
    date_input = input("Next Date: ")
    # type_input = "day"
    dateInput(date_input)


main()
