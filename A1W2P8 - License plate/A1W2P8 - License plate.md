## Assignment: A1W2P8 - Lincese plate

### Creation Date: 13-09-2023

### What did I learn?
I've learned how `license.split()` and `.isnumeric` works in Python.

### How did I learn it?
I looked up potential solutions to easily get the data from the license plate number, without retrieving the dashes.

### Why/how did I solve it?
Since there is a whole list of patterns which needed to be marked as valid I began with a few patterns and seeing if my solutions worked. I constantly checked my changes as well, so I exactly knew when the script did or didn't know when a pattern was valid.

In the beginning, before I used methods, to mark if the license plate was correct I made use of a variable called `good` which would be set to `1` (true) so I could call the variable later and check if the license plate was in fact passing the validation.
The code would look something like this:

```python
# Checking if the license plate is the length it should be
if license_plate_length == 8:
    # Are there dashes as 3rd and 6th character?
    if license_plate[2] == "-" and license_plate[5] == "-":
        # Are the first two characters the same as the 4th and 5th character?
        if (license_plate[0] + license_plate[1]) == (license_plate[3] + license_plate[4]):
            # Are the last two characters NOT the same as the 4th and 5th character?
            if (license_plate[6] + license_plate[7]) != (license_plate[3] + license_plate[4]):
                # Then this license plater pattern is valid
                good = 1

    # Print if the lincese plate is valid
    if good:
        print("Valid")
    else:
        print("Not Valid")
```

Eventually I switched to methods and made life a bit easier to validate license patterns. I think I've cut my code in half with using the ``.split()`` and `.isnumeric` method.

The `split("-")` method was  a true lifesaver because it removes the dashes and makes a list for you. The dash basically says where the comma should go for the list. (So `XX-XX-99` becomes `[XX, XX, 99]`). When you can call them with an index and use `.isnumeric` you cal also see if that stored string *only* contains numbers. This is really useful to because we can now detect where the '99' is from 'XX-XX-99'. If you make variations on this with the `len()` method as well we suddenly can detect variations as 'XXX-99-X' as well.
See the final code below.

## Code Snippet
```python
def validate_license(license):
    # Split into parts
    parts = license.split("-")

    # Validate format
    # Check if the license plate is long enough
    if len(parts) != 3:
        return False

    # We need to have a numeric value in our first and last 'part' if there are any numerics
    if parts[2].isnumeric() != parts[0].isnumeric():
        return False

    # Checks for patterns:
    # XX-99-99 and 99-XX-XX
    if parts[1] == parts[2] and parts[0] != parts[1]:
        return True

    # Checks for patterns:
    # 99-99-XX and XX-XX-99
    if parts[0] == parts[1] and parts[0] != parts[2]:
        return True

    # Checks for patterns:
    # 99-XX-99 and XX-99-XX
    if parts[0] == parts[2] and parts[0] != parts[1]:
        return True

    # If every part is unique
    if parts[0] != parts[1] and parts[0] != parts[2]:
        # Checks for patterns:
        # 99-XXX-9, XX-999-X and XXX-99-X
        if (len(parts[0]) + len(parts[1])) == 5 and len(parts[2]) == 1:
            return True

        # Or check for (the reversed) patterns:
        # 9-XXX-99, X-999-XX, 9-XX-999
        if (len(parts[1]) + len(parts[2])) == 5 and len(parts[0]) == 1:
            return True


def _main_():
    # Request user input
    license = input("License: ")
    
    # Pass the user input to the method, so we can validate it and immediately check  if we get True or False back. 
    if validate_license(license):
        print("Valid")      # True
    else:
        print("Invalid")    # False

# Run the script
_main_() 
```