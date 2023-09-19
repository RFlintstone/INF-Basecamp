## Assignment: A1W3P1 - Simple palindrome

### Creation Date: 18-09-2023

### What did I learn?
I learned that you can join a list like this: `x = ''.join(myDict)`.

### How did I learn it?
I've looked up easy and short solutions and wanted to do this with a list. 
And, in my case, I needed to convert the list back to a string with join. 
I didn't want to use something like this `x = mySeparator.join(myDict)` so I looked up a solution which is a tiny bit shorter and 'easier' to use.
I found and settled on `''.join(reversed_i)`. This is actually a really obvious solution as you replace the variable `mySeperator` with a string. So in core it basically works the same. 

### Why/how did I solve it?
The list is reached by casting the input (string) to a list like this:
```python
i = input()
reversed_i = list(i)
```

And then reversing and stringifying the list like this:
```python
reversed_i.reverse()
reversed_i = ''.join(reversed_i)
```

## Code Snippet
```python
# Ask for user input
i = input()

# characters to filter.
punct_marks = ",.?!;"

# Remove all characters listed in 'puct_marks'.
count = 0
for p in punct_marks:
    i = i.replace(p, "")
    count += 1

# Reverse filtered input
reversed_i = list(i)
reversed_i.reverse()
reversed_i = ''.join(reversed_i)

# Check if the input is the same as the reversed input
result = ""
result = f'{i} is '
if i == reversed_i:
    result += "a palindrome"
else:
    result += "not a palindrome"

# Print if the input is a palindrome or not
print(result)
```