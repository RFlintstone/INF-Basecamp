# An online retailer sells two products: widgets and gizmos.
# Write a program that reads the number of widgets and the number of gizmos in an order from the user.
# Then your program should compute and display the total weight of the order.
#
# Criteria:
# Each widget weighs 75 grams
# Each gizmo weighs 112 grams
# Input example:
# Number of widgets: 10
# Number of gizmos: 1
#
# Output example:
# The Total Weight of the Order: 862 grams

widget_weight = 75
gizmo_weight = 112

print("How many widgets do you have?")
widget_amount = int(input())

print("How many gizmos do you have?")
gizmo_amount = int(input())

widget_total_weight = widget_weight * widget_amount
gizmo_total_weight = gizmo_weight * gizmo_amount

total = widget_total_weight + gizmo_total_weight

print("The Total Weight of the Order:" + str(total))