## Assignment: A1W1P4 - Weight calculation

### Creation Date: 04-09-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
I've created two variables (being ``widget_height`` and ``gizmo_height``) as these values will never change and will be used globaly (hence why they are at the top).
I then followed up, two times, with the method ``print()`` and the method ``input()`` to determine how many widgets and gizmos we have.
When that's determined we calculate the weight total for the widgets and gizmos (``widget_total_weight`` and ``gizmo_total_weight``). 
Then to fulfill the requirements of the assignment we add both **individual totals** to get the final total. Now if we print ``total`` we have fulfilled the requirements. 

## Code Snippet
```python
# Widget and Gizmo height are static
widget_weight = 75
gizmo_weight = 112

# Print what you need
print("How many widgets do you have?")

# Request input and convert it to an int so we can use it in a formula
widget_amount = int(input())

# Print what you need
print("How many gizmos do you have?")

# Request input and convert it to an int so we can use it in a formula
gizmo_amount = int(input())

# Calculate the total weight from both Widget and Gizmo
widget_total_weight = widget_weight * widget_amount
gizmo_total_weight = gizmo_weight * gizmo_amount

# Now add both weights so we have the total weight
total = widget_total_weight + gizmo_total_weight

# Print the total weight - variable should be string since we concatenate it to a string 
print("The Total Weight of the Order:" + str(total))
```
