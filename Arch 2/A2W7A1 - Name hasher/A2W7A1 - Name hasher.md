## Assignment: A2W7A1 - Name hasher

### Creation Date: 10-10-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
As Cigdem Okuyucu said this to me; I won't specify how I solved it or what my code is if I didn't
learn anything new in the assignment/problem.

## Code Snippet
```python
def encode_string(data: str, key: str = None) -> str:
    # a@b.c>d#eA
    # Check if data is a string
    if not isinstance(data, str):
        raise TypeError("data must be a string")

    # Check if key is a string
    if not isinstance(key, str):
        raise TypeError("key must be a string")

    # Replace single quotes with double quotes so the json can be parsed correctly
    key = key.replace("'", '"')

    # Parse string as JSON directly
    key = json.loads(key)

    # Verify if the key was converted to dict
    if not isinstance(key, dict):
        raise ValueError("Unable to convert key to JSON")

    # 'Encode' the data
    for letter in data:
        encoded_values.append(key.get(letter))

    # Return the encoded string
    return ''.join(encoded_values)
```
