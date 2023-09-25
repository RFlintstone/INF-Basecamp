# Do some research regarding truth tables.
# Write down truth tables for and and or. Implement a program that prints these two truth tables.
#
# Criteria:
# Use 4 states: True + True, True + False, False + True, False + False
# Input example:
# No input is given
#
# Output example:
# AND
# True + True = True
# ...
#
# OR
# ...

inputs = []
<<<<<<< HEAD
=======
# Put values in like this: [(True, True), (True, False), (False, True), (False, False)]
>>>>>>> 4a85935fb4e4c39362d9c7eeb007dbdeaec2c70f
for a in [True, False]:
    for b in [True, False]:
        inputs.append((a, b))

print("AND")
for a, b in inputs:
    print(f"{a} + {b} = {a and b}")

print("\nOR")
for a, b in inputs:
    print(f"{a} + {b} = {a or b}")