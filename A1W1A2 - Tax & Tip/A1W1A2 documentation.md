## Assignment: A1W1A2 - Tax & Tip

### Creation Date: 04-09-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
Because I needed decimals and didn't want to write more code than necessary I cast the input to float and force the decimal that way.
Then when printing I use `%.3f` to say I want to print 3 decimals if the outcome of the calculations provide a 3 decimal outcome.

## Code Snippet
```python
# Request input and convert it to a float so we can use it in a formula with decimals
price = float(input())

# Calculate tip, tax and total
tip = price / 100 * 15
tax = price / 100 * 21
total = price + tip + tax

# Print the results - Instead of converting the variable to string we say that we expect a 3 decimal float
print("Tax: %.3f" % tax)
print(", Tip: %.3f" % tip)
print(", Total: %.3f" % total)
```
