## Assignment: A1W1P6 - Hours, minutes and seconds

### Creation Date: 04-09-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
I wanted to have a variable for each calculation and since the input will be the amount of days I've casted that to an int and called the variable 'd' to calculate the hours.
Once you have the hours you can calculate the minutes and once you have your minutes you can calculate the seconds.
After the calculations are done I simply printed the outcome with the variables casted to a string so concatenation is possible.

## Code Snippet
```python
# Print what we need
print("Provide an amount of days")

# Request an input and convert it as int so we can use it in a formula
d = int(input())

# Calculate the hours, minutes and seconds with the input
hours = d * 24
minutes = hours * 60
seconds = minutes * 60

# Print the results as strings. Variables need to be string because we otherwhise concatenate an integer to a string
print("Hours: " + str(hours))
print(", Minutes: " + str(minutes))
print(", Seconds: " + str(seconds))
```
