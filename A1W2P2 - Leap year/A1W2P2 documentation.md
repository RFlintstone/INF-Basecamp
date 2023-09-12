## Assignment: A1W2P2

### Creation Date:
07-09-2023

### What did I learn?
I learned how to calculate a leap year

### How did I learn it?
I looked up the formula

### Why/how did I solve it?
I requested user input and casted it to float. I've casted it to float because the outcome of the leap year can have decimals. 
If we have the float we will divide it by 4 to see kickstart the calculation. Then if that result is odd it can't be a leap year, and if it is even it is (most likely) a leap year.

## Code Snippet
```python
# Get input
i = float(input())

# Divide by for
leap = i / 4

# If year is even after dividing it's a leap year, if not it is not a leap year 
if leap % 2:
    print("not leap")
else:
    print("leap")
```
