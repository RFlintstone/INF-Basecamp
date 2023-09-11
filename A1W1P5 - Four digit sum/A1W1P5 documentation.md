## Assignment:
A1W1P5

### Creation Date:
04-09-2023

### What did I learn?
I learned that you can convert a string to an array using

### How did I learn it?
Not applicable

```python
input_to_array = [char for char in input_to_str]
```
## Code Snippet
```python
# Request an input
input = input()

# Convert the input to string
input_to_str = str(input)

# Now we can convert the string to an array
input_to_array = [char for char in input_to_str]

# Create a variable so we can get the result of the sum later on
sum = 0

# Create a variable so we can store the formula (1+2+3+4)
sum_str = ""

# We create a counter so we know at which position in the string we are
counter = 0

# Loop through the formula which we converted to an array
for c in input_to_array:
	# If length of the formula we pass is odd we make sure to add a "+" and then the next number 
    if len(sum_str) % 2:
        sum_str += "+" + input_to_array[counter]

	# If the length of the formula is anything but odd we only put the next number in
    else:
        sum_str += input_to_array[counter]

    # We always add the next number to the last total of sum until
    sum += int(input_to_array[counter])

	# Move one up so we can actually get the next number
    counter += 1

# Now that we are done with the loop we print both the formula and the sum as one whole string
print(sum_str + "=" + str(sum))```
