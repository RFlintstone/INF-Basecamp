## Assignment: A1W3P5 - Multiplication table

### Creation Date: 20-09-2023

### What did I learn?
I've learned what the enumerate function does and how I can use it in my code.
It returns a tuple with the first value as the count and the second one as the actual value from the list you're enumerating.
So if you use the following:
```python
# Our list
list = ["item1", "item2", "item3"]
 
# Enumerating list and return a tuple
for count, item in enumerate(list):
    # Then print the count and the item
    print(count, item)
```

The output from the code above would be:
```
0 item1
1 item2
2 item3
```
The count will start at 0 and end when enumerate is finished enumerating through the list.

### How did I learn it?
I've looked up easy and short solutions which I could use in this and future assignments. Then I found what `enumerate()` does and how I could use it.  

### Why/how did I solve it?
I solved the assignment by making three different list and filling these with numbers by using a for loop with a specific range.
The `column(_joined)` variables are responsible for the right numbering while the rows actually does multiplication.
Then, at the end, once all variables are ready (so when all their respected values are added) we can enumerate on the rows (which we put in a list called `tables`).
Because of enumerate we can also count up with each print. This way we get the final output:

```
	1	2	3	4	5	6	7	8	9	10	
1	1	2	3	4	5	6	7	8	9	10	
2	2	4	6	8	10	12	14	16	18	20	
3	3	6	9	12	15	18	21	24	27	30	
4	4	8	12	16	20	24	28	32	36	40	
5	5	10	15	20	25	30	35	40	45	50	
6	6	12	18	24	30	36	42	48	54	60	
7	7	14	21	28	35	42	49	56	63	70	
8	8	16	24	32	40	48	56	64	72	80	
9	9	18	27	36	45	54	63	72	81	90	
10	10	20	30	40	50	60	70	80	90	100	
```

## Code Snippet
```python
# Define lists
column = list()
row = list()
tables = list()

# Create columns
for n in range(0, 11):
    if n != 0:
        column.append(str(n))
    column.append("\t")

# Create rows
for n in range(1, 10):
    row.append(str(n) + "\n")

# Create tables
for i in range(0, 11):
    row = ""
    # Row 1
    if i == 0:
        for j in range(1, 11):
            row += str(j) + "\t"
    # All other rows
    else:
        for j in range(1, 11):
            row += str(j * i) + "\t"
    # Add the row
    tables.append(row)

# Join lists so they both become a string
column_joined = "".join(column)
row_joined = "".join(row)

# Print each index (i) with their value (table) from the list (tables)
for i, table in enumerate(tables):
    if i < 1:
        print(f"\t{table}")
    else:
        print(f"{i}\t{table}")
```