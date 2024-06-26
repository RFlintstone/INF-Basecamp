# Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user and then report the appropriate name as part of a meaningful message.
#
# Criteria: Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of
# sides outside of this range is entered then your program should display the error message: Amount of sides is out
# of range.
#
# Input examples:
# Sides: 3
# Sides: 4
#
# Output examples:
# Triangle
# Square

shapes = ["", "", "", "triangle", "quadrilateral", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]
nr = int(input())
shape = shapes[nr]
print(shape)

