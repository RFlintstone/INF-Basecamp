# Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.
#
# Input examples:
# Number: 1
# Number: 4

# Output examples:
# Odd
# Even

# Ask for input and immediately make it an int
i = int(input())

# Modulo to check if the input is even or odd as it will check the remainder
if i % 2:
    print("Odd")
else:
    print("Even")
