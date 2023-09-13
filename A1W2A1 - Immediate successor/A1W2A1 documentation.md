## Assignment: A1W2A1 - Immediate successor 

### Creation Date: 06-09-2023

### What did I learn?
How Codegrade handles errors - I also overlooked relatively simple solutions in favour of more difficult ones which could be written with fewer lines. This resulted in spending more time on this assignment than I wanted. 

### How did I learn it?
I've looked at the errors which were outputted by Codegrade and compared them to the errors I got from my IDE (PyCharm).

### Why/how did I solve it?
This was an interesting one for me. Not that is was a difficult assessment but because I needed to think simpler than I'm used to.
This is why my first thought was using the ``datetime`` library to get the current date, automatically detect when a month did or didn't have 31 days ect.
Although I did get far with that library Codegrade didn't like the exceptions the library was causing on the website - the issue wasn't present on my latop/pc.
Hence why I switched to my current version of the code (see below, under 'Code Snippet').

**I used methods, why?:** my main reason to use methods was to prevent that the code would become overwhelmingly long. A good example of this is the validation method, validate(). I could have changed the order of the code but since I was able to use methods I had the flexibility and therefore the possibility to validate the input more or somewhere else.
So besides it being useful for fewer lines of code it is also very useful if you are trying to debug quick and easy.

**Considering you used a library first, why would you choose a library over your current solution?:** 
Well, a library tends to be programmed in a way it already checks a lot of edge cases for you which gives you more information when you need to debug your software. The interesting part though is that this reason is also the reason why Codegrade didn't accept it. - The most likely reason is that Codegrade forced certain prints which your local machine doesn't force. And since print() methods are expected to be the actual result of the assignment it didn't work.

**So how does it actually work?:** 
- **main()** triggers the whole program
- **dateInput()** first I'm asking for user input and pass that to the ``dateInput()`` method. 
This method is responsible for triggering the validation and then seeing if the validation succeeded or not. If the validation succeeded and everything is OK it will trigger the shift functions and print the shifted outcome. This would complete the assessment.
- **validate()** the validate method checks if the values which are passed are correct and if not it prints an error and returns ``None``, if it is all good it will actually format the date again to guarantee the year, month and day are in the correct place (``YYYY-MM-DD``) and return it.
- **shiftYear(), shiftMonth() and shiftDay()** are responsible that the year, month or day can be both increased or decreased.

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

### An example of using the datetime library
```python
# Define the dateInput() method
def dateInput(input):
    # Trigger the validate method
    x = validate(input)

    # If the validation is OK
    if x != None:
        # make the validated format a date of type datetime
        datetime.date = x

        # To shift one day into the future replace the current day with current_day+1
        datetime.date = datetime.date.replace(day=datetime.date.day + 1)

        # Print our new date
        print(datetime.date)

        # To shift one month into the future and begin on day one of the month 
        datetime.date = datetime.date.replace(month=datetime.date.month + 1, day=1)

        # Print our new date
        print(datetime.date)
```
