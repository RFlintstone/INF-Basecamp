## Assignment: A1W2P4 - Triangle type

### Creation Date: 11-09-2023

### What did I learn?
Nothing I already knew

### How did I learn it?
Not applicable

### Why/how did I solve it?
I requested user input and then checked through if and else if, if the sides are, or are not, equal to each other.
Based on if and how much sides are equal it will print what kind of triangle it is.

## Code Snippet
```python
i = input()

a = i[2]
b = i[7]
c = i[12]

if a == b and a == c:
    print("equilateral triangle")
elif (a == b and not a == c) or (a == c and not a == b):
    print("isosceles triangle")
elif (a != b) and (a != c):
    print("scalene triangle")
```