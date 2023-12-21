## Assignment: A2W6A1 - Addressbook

### Creation Date: 10-10-2023

### What did I learn?
I learned that you can use dict.extend() to merge multiple dictionaries.

### How did I learn it?
I looked up how I could merge multiple dictionaries cause I knew it must be possible with a build in method.

### Why/how did I solve it?
As Cigdem Okuyucu said this to me; I won't specify how I solved it or what my code is if I didn't
learn anything new in the assignment/problem.

## Code Snippet
```python
def list_contacts(json, direction):
    # Check if we want to reverse the list (the same as ascending/descending)
    reversed = (direction.upper() == "DESC")

    # Sort the contacts based on the boolean
    sorted_contacts = sorted(json, key=lambda x: x['id'], reverse=reversed)

    # Make a list so we can fill the addressbook
    addressbook = []

    # Loop through the sorted contacts
    for i, contact in enumerate(sorted_contacts):
        # Store our new entry in an empty list
        entry = [str(i + 1), contact['first_name'], contact['last_name'], contact['emails'], contact['phone_numbers']]
        addressbook.append(entry)  # Add the entry to the addressbook, which is now sorted

    # Return the sorted list
    return addressbook
```
