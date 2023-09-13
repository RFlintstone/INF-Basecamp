## Assignment: A1W1P3

### Creation Date: 04-09-2023

### What did I learn?
I learned nothing with this assignment.

### Why/how did I solve it?
I wanted to print what I needed separately from the input() method so I basically repeat the first `print()` and `int(input())` lines.
Then, since I want to calculate the area I just do `a = l*w` (meaning `area = length * width`) and print the result (`a`)

## Code Snippet
```python
# Print what you need
print("Enter Width:")

# Request input and convert it to an int so we can use it in a formula
w = int(input())

# Print what you need
print("Enter Length:")

# Request input and convert it to an int so we can use it in a formula
l = int(input())

# Calculate area with the width and height input we just gathered
a = l*w

# Print the result - variable should be string since we concatenate it to a string 
print("The Area of the Room: " + str(a))
```
