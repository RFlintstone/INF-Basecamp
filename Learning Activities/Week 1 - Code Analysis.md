## Code Analysis

1) Analyze the programming solutions given below and write down in one sentence: what do they do? What problems do they try to solve?

```py
# Code Analysis 1
# Inputs
a = int(input("enter value A: "))
b = int(input("enter value B: "))

# Processing
t = a
a = b
b = t

# Outputs
print("A =", a)
print("B =", b)
```

`Code Analysis 1` asks for input A and B which is imediatly converted to an integer after that the numbers A and B are switched and printed.

```py
# Code Analysis 2

# Inputs
num = int(input("Enter a number: "))

# Processing
dig = num % 10

# Outputs
print(dig)
```
`Code Analysis 2` also asks for an input which is imediatly converted to an integer. After the conversion it will calculate and print the remained of `num` with modulus 10.

2) Implementing a solution for a given problem is challenging for a beginner programmer. It is helpful to have a guideline with some steps. Check [this guideline](https://github.com/hogeschool/basecamp/blob/main/week01/checklist_metacog.pdf) and apply it the Problem 5 of this week. Hint: A template with some examples provided [here](https://github.com/hogeschool/basecamp/blob/main/week01/template.py)

```py
# Format and calculate the sum. Input 3141 should become 3+1+4+1=9 

# Inputs
input = input()
input_to_str = str(input)
input_to_array = [char for char in input_to_str]

# Processing
sum = 0
sum_str = ""
counter = 0
for c in input_to_array:
    if len(sum_str) % 2:
        sum_str += "+" + input_to_array[counter]
    else:
        sum_str += input_to_array[counter]
    sum += int(input_to_array[counter])
    counter += 1
    
# Outputs
print(sum_str + "=" + str(sum))
```

3) One of the students has tried to apply the guideline for a given problem. But, the code does not produce the expected results. Check the code and without executing the code try to find the mistake.

```py
# Ask the user for the name of item X.
# Then ask the user for the price of item X.
# Finally, ask the user for desired quantity of item X.
# Based on input, calculate how much you have to pay.
# Write the message in the form:
#   "To purchase N units of X you must pay M euros."


# Inputs
name = input("Input the name of item X: ")
price = input("What is the price of", name, "? ")
quantity = input("How many units of", name, "do you want to buy? ")

# Processing
total = price * quantity

# Outputs
print("To purchase", quantity, "units of", name, "you must pay", total, "euros.")
```
The issue here is that there are multiple arguments given to the input of price and quantity but input() doesn't expect multiple arguments.
This could most likely be solved by doing this instead:

```py
name = input("Input the name of item X: ")
price = input(f"What is the price of {name}? ")
quantity = input(f"How many units of {name} do you want to buy? ")
```
