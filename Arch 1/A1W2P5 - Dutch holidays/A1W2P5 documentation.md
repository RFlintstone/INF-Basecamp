## Assignment: A1W2P5 - Dutch holidays

### Creation Date: 11-09-2023

### What did I learn?
I didn't know `json.get(key)` was a build in function in python.

### How did I learn it?
I've looked up how python uses JSON and if I needed a library for it or not.

### Why/how did I solve it?
I request user input, define a table of dutch festivities with the ``month and day`` as key and the name of the festivity as value.
Then I use ``festivities.get(input)`` to see if there is a key based on the provided input. If the input is equal to an existing key it prints the name of the holiday.
If not, it will print "does not exist".

## Code Snippet
```python
i = input()

festivities = {
    "month 1, day 1": "Nieuwjaarsdag",
    "month 4, day 7": "Goede Vrijdag",
    "month 4, day 9": "Eerste Paasdag",
    "month 4, day 10": "Tweede Paasdag",
    "month 4, day 27": "Koningsdag",
    "month 5, day 5 ": "Bevreidingsdag",
    "month 5, day 18": "Hemelvaartsdag",
    "month 5, day 28": "Eerste Pinksterdag",
    "month 5, day 29": "Tweede Pinksterdag",
    "month 12, day 5": "Sinterklaas",
    "month 12, day 25": "Eerste Kerstdag",
    "month 12, day 26": "Tweede Kerstdag",
}

if festivities.get(i) is not None:
    print(festivities[i])
else:
    print("Does not exist")
```