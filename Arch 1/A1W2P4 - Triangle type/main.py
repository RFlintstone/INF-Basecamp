# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type of the
# triangle.
#
# Criteria:
# Input is given as a comma seperated string: a=5, b=6, c=5
# All 3 sides of an equilateral triangle have the same length.
# An isosceles triangle has two sides that are the same length, and a third side that is a different length.
# If all of the sides have different lengths then the triangle is scalene.
#
# Input example:
# Sides: a=5, b=6, c=5
#
# Output example:
# Isosceles triangle

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
