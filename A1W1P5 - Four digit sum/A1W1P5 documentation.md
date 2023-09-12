## Assignment: A1W1P5

### Creation Date:
04-09-2023

### What did I learn?
I learned that you can convert a string to an array using

```python
input_to_array = [char for char in input_to_str]
```

### How did I learn it?
Not applicable

### Why/how did I solve it?
To convert a string full of numbers (Ex: 1234) to a sum (1+2+3+4=10) I decided that it might be the best way to program
the software in 'steps'. Meaning that each variable, loop or statement will be limited in function but also always finish one task - an exception being the first variables which are needed to store data and therefore wont be doing any 'tasks' (i.e calculations).
The best way I could think of solving this is to treat the string as an array (in a loop) and then use ``[]`` to index that position. 
I consider this a good approach because this way, again, you only have to do one 'task' to accomplish adding the total of the sum as well as actually 'writing' the formula.

To 'write' the sum we check in each iteration if the storage we are going to write to is odd. If it is odd we'll add a ``+`` sign first and then the number. If it is anything else then odd (that would be even) we only add the number.
This should be done because we never want to begin with a ``+`` sign but always want it after the first number for example.

Then, to actually calculate the final result we do a slight alteration/simplification of the code we made to write the sum and just convert the last number (in string form) to int and add that with ``+=`` to our last total from our previous iteration.
If you do this correctly, which I do, you should get both the right formula, as string, and the right total, as int which we need to convert to string again for the ``print()``.

The way I create an array of the string is like this:

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
