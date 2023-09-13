## Assignment: A1W2P5 - Dog years

### Creation Date: 11-09-2023

### What did I learn?
Nothing I already knew

### How did I learn it?
Not applicable

### Why/how did I solve it?
First of all I define (global) variables with one of them requesting user input.
Then I check if the user input is a negative number. If it is lower then a 0 it will print an error and exit the program.

If it is a positive number it will enter a while loop and only exit once the iteration value (which is initially 0). In the loop we check if the iteration is smaller then 2 which, in other words, checks if the dog is younger than 2. If it is younger it will add 4 dog years, if it is either equal or bigger than 2 it will add 10.5 dog years. When the additions are done we'll increment the iteration value with `+= 1` so we won't stay in the loop forever.
Once the loop is done we'll print the final age.

## Code Snippet
```python
i = int(input())
iteration = 0
age = 0
year = 0
dog_years_normal = 4
dog_years_first_two = 10.5

if i < 0:
    print("Only positive numbers are allowed")
    exit(1)
else:
    while iteration < i:
        if iteration < 2:
            age += dog_years_first_two
        else:
            age += dog_years_normal
        iteration += 1
print(age)
```