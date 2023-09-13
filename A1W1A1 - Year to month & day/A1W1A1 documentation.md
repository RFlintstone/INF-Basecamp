## Assignment: A1W1A1 - Year to month & day

### Creation Date: 04-09-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
I wanted to have a variable for each calculation and since the input will be the year I've casted that to an int and called the variable 'y'.
When printing I used 3 loose print() methods to prevent one big line and to make the code a bit more readable. This is how it would have looked when I put everything on one line:
```python
print("Years: " + str(y) + "Months: " + str(m) + ", Days: " + str(d))
```

## Code Snippet
```python
# Print what you need for the input
print("Enter amount of years:")

# Request input and convert it to an int so we can use it in a formula
y = int(input())

# Use the input (y) to calculate months and days
m = y * 12
d = y * 365

# Print the results - variable should be string since we concatenate it to a string 
print("Years: " + str(y))
print("Months: " + str(m) + ",")
print("Days: " + str(d))
```
