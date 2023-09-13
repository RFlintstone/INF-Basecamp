## Assignment: A1W2P3

### Creation Date: 11-09-2023

### What did I learn?
I already knew it

### How did I learn it?
I already knew it

### Why/how did I solve it?
I requested user input and casted it to int. Once that was done I could use the ``nr`` in ``shapes[]`` as an index.
If that is done we can print ``shapes[nr]`` as ``shape``.

## Code Snippet
```python
# List all kind of shapes
shapes = ["", "", "", "triangle", "quadrilateral", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]

# Get the number of the shape so we can index is later
nr = int(input())

# Request the index of the shapes as variable shape
shape = shapes[nr]

# Print shape
print(shape)
```
