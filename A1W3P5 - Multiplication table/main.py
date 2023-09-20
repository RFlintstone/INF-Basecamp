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

m_1 = list()
m_2 = list()
r = list()

column = list()
row = list()
tables = [[] for _ in range(11)]  # 11 inner lists

# Create rows and columns
for n in range(0, 11):
    if n != 0:
        column.append(str(n))
        column.append("\t")
        row.append(str(n))
        row.append("\n")
    else:
        column.append("\t")

for i in range(1, 11):
    for j in range(1, 11):
        tables[j - 1].append(str(j * i))
        tables[j - 1].append("\t")

column_joined = "".join(column)
row_joined = "".join(row)

print(column_joined)
print(row_joined)

for table in tables:
    for x in range(len(table)):
        print(f"{x}\t{''.join(table)}")