## Assignment: A1W1P2 - Year to month and day

### Creation Date: 04-09-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
I wanted to have a variable for each calculation and since the input will be the year I've casted that to an int and called the variable 'y'.
When printing I used loose print() methods to prevent one big line and to make the code a bit more readable.

## Code Snippet
```python
# Print what we need
print("Enter amount of years:")

# Request input and convert it to an int so we can use it in a formula
y = int(input())

# Use input to calculate both months and days
m = y * 12
d = y * 365

# Print the result - variable should be string since we concatenate it to a string 
print("Months: " + str(m))
print(", Days: " + str(d))
```
