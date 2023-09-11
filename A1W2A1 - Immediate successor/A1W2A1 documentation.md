## Assignment:
A1W2A1

### Creation Date:
06-09-2023

### What did I learn?
How Codegrade handles errors - I also overlooked relatively simple solutions in favour of more difficult ones which could be written with fewer lines. This resulted in spending more time on this assignment than I wanted. 

### How did I learn it?
I've looked at the errors which were outputted by Codegrade and compared them to the errors I got from my IDE (PyCharm).

## Code Snippet
```python
# Validate year format
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

# Function to increase or decrease (aka shift) the year
def shiftYear(date_text, shift):
    year = int(date_text[0:4]) + shift
    return str(year) + "-01-01"

# Function to increase or decrease (aka shift) the month
def shiftMonth(date_text, shift):
    month = int(date_text[5:7]) + shift
    return date_text[0:4] + "-" + str(month) + "-01"

# Function to increase or decrease (aka shift) the day
def shiftDay(date_text, shift):
    day = int(date_text[8:10]) + shift
    day_str = str(day)
    if len(day_str) < 2:
        day_str = "0" + day_str
    return date_text[0:7] + "-" + day_str

# Execute our actions here
def dateInput(input):
    i = validate(input)
    if i != None:
        i = shiftDay(i, 1)
        print("Next Date: " + i)
        i = shiftMonth(i, 1)
        print("Next Date: " + i)
        i = shiftYear(i, 1)
        print("Next Date: " + i)

# Get input and pass it to the dateInput() function
def main():
    date_input = input()
    dateInput(date_input)

# Run the program
main()
```
