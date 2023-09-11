# Positions on a chess board are identified by a letter and a number.
# Usually, the letter identifies the column, while the number identifies the row.
# Write a program that reads a position from the user.
# The program should determine if the column begins with a black square or a white square.
# Then use modular arithmetic (check if you know this concept) to report the color of the square in that row.
#
# Criteria:
# Your program may assume that a valid position will always be entered
#
# Input examples:
# Position: D5
# Position: A1
#
# Output examples:
# White
# Black

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c_count = 0
r_count = 0

i = input()
column = i[0].lower()
row = int(i[1])

if type(column) == str:
    print("colum OK:", column)
    for a in alphabet.lower():
        if a == column:
            break
        else:
            c_count += 1

if type(row) == int:
    print("row OK:", row)
    while r_count < row:
        r_count += 1

# Now we can check with modulo if the spaces are black or white, given we use c_count (column count) and r_count
# (row count) correctly

print(column, c_count)
print(row, r_count)

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