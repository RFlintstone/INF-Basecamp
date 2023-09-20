# Write a program that draws “modular rectangles” like the ones below.
# The user specifies the width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from left to right and top to bottom, but are all done mod 10.
#
# Input example:
# Width: 5
# Height: 3
#
# Output example:
# 0 1 2 3 4
# 5 6 7 8 9
# 0 1 2 3 4

# Ask for Input
width = int(input("Width: "))
height = int(input("Height: "))

# Create a list, so we can store the box and output it later on
box = list()

# Create a counter and a loop with the range 0 until width * height
count = 0
for r in range(0, width * height):
    # Put range%10 in the box with a space. This way we'll always get a number from 0-9, with the right spacing.
    box.append(str(r%10) + " ")

    # Check the width, so we'll make an enter every time we reach 'width'
    if count == width-1:
        # Add a newline to the box
        box.append("\n")
        # Reset counter
        count = 0
    else:
        # If we didn't reach the width, just increase the counter
        count += 1

# Convert the list to a box
box = ''.join(box)

# Print the box
print(box)