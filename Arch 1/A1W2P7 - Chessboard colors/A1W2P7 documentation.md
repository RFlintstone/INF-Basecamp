## Assignment: A1W2P7 - Chessboard colors

### Creation Date: 11-09-2023

### What did I learn?
I learned that `.lower()` and `.upper()` work within Python.

### How did I learn it?
I already knew it existed in other programming languages, so I tried it in Python as well and it worked.

### Why/how did I solve it?
I basically solved it by counting columns and rows which basically creates a grid and then because we invert colours each row we can use modulo to see if we have an even or uneven number. The same goes for the columns.

First I do check if the type of column is a string, and the type of row is an integer. This is how we can confirm that we correctly separated the algebraic notation.
When we did it correctly the column part will lower the whole alphabet string, loop through each position of the string and see if the index of the current iteration is equal to the column which we seperated from the algebraic notation.
If the index is equal to the column we exit the loop, otherwise we add one to the column count, so we know we are not in the right column yet.

Almost the same goes for the rows, but this is a bit easier. In this case we enter a while loop instead of a for loop and we add one row (`r_count += 1`) as long as the row count is lower then the row (the number we separate from the algebraic notation).

When we did that we want to print either black or white, or white or black (since we need to invert the colours each time).
The way we could solve this is to see if the colum count, but with an addition of one, is odd. The reason that we add one is that we want to prevent to do modulo on a zero.
Now we did that we just simply check if the row is odd or not and then print the colour.

Now we are able to print black and white correctly based on algebraic notation.
## Code Snippet
```python
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c_count = 0
r_count = 0

i = input()
column = i[0].lower()
row = int(i[1])

if type(column) == str:
    for a in alphabet.lower():
        if a == column:
            break
        else:
            c_count += 1

if type(row) == int:
    while r_count < row:
        r_count += 1

if (c_count + 1) % 2:
    if (r_count % 2):
        print("black")
    else:
        print("white")
else:
    if (r_count % 2):
        print("white")
    else:
        print("black")
```