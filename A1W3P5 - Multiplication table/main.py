# In this exercise you will create a program that displays a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10.
#
# Criteria:
# Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10.
# It should also include labels down the left side consisting of the numbers 1 through 10.
# Input:
# No input is given
#
# Output example:
#    1  2  3  4  5  6  7  8  9 10
# 1  1  2  3  4  5  6  7  8  9 10
# 2  2  4  6  8 10 12 14 16 18 20
# ...

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