## Assignment: A4W14A1 - Name hasher 2

### Creation Date: 11-14-2023

### What did I learn?
I didn't really learn anything as this assessment was almost a copy and paste from the first name hasher assessment.  

### How did I learn it?
Not applicable

### Why/how did I solve it?
As Cigdem Okuyucu said this to me; I won't specify how I solved it or what my code is if I didn't
learn anything new in the assignment/problem.

## Code Snippet
```python
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    if key is None:
        key = "A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@"

    # Check if encoded and decoded are both strings
    if not all(isinstance(item, str) for item in (encoded, decoded)):
        raise TypeError("Both `encoded` and `decoded` must be strings")

    # If key is provided, check if it's a string
    if key and not isinstance(key, str):
        raise TypeError("`key` must be a string")

        # Use the decoding function
    resolved = decode_string(encoded, key)

    # Return True if the decoded value matches the given decoded string, False otherwise
    return resolved == decoded
```
