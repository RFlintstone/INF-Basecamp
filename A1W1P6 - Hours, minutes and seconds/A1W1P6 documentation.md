## Assignment:
A1W1P6

### Creation Date:
04-09-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

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
