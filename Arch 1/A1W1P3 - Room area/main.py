# Write a program that asks the user to enter the width and length of a room.
# Once the values have been read, your program should compute and display the area of the room.
#
# Criteria:
# The length and the width will be entered as floating point numbers
# Round output up to 1 decimal
# Input example:
# Width: 5
# Length: 5.5
#
# Output example:
# The Area of the Room: 27.5


print("Enter Width:")
w = int(input())
print("Enter Length:")
h = int(input())

a = w*h

print("The Area of the Room: " + str(a))