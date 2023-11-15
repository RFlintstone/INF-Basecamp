## Code Analysis

1) Analyze the two given codes below without executing them. What will be the result of the programs?

```py
a_tuple = ('Never', 'gonna', 'give', 'you', 'up')
counter = 0
for x in a_tuple:
    if x[0] ==  'g':
        counter = counter + 1
    else:
        counter = counter + 2
print(counter)
```
This will most likely result in `8` as it will increase the counter by `1` if the word starts with 'g', else it will increase the counter by 2.

```py 
def do_something(x):
    rtuple = x,
    for i in range(2,11):
        rtuple = rtuple + ((x*i),)
    return rtuple
print(do_something(6))
```
The function will use the following formula. Since it uses a range in a for loop it will start with `rtuple = 6 + ((6*2))` and end with `rtuple = 6 + ((6*11))`. So it is adding the current result to the previous result, but as a new item in the tuple. The tuple is complete when the end of the range is reached.

```py 
def process_strings(strings):
    processed_strings = []
    for string in strings:
        processed_string = ""
        for char in reversed(string):
            processed_string += char
        processed_strings.append(processed_string)
    return processed_strings

def main():
    names = ["Alice", "Bob", "Charlie", "Dave"]
    processed_names = process_strings(names)
    for name in processed_names:
        print(name)

main()
```
In short, we pass a list full of names into a function and then call a function we called to reverses each name. An example being that `Alice` would become `ecilA`.
When we did that to all names in the list we return the now full array with reversed names and print it in main().


