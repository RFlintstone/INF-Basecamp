# Arch 2

## [In Arch 2 I stopped doing problems, hence why this document is much shorter]

## Assignment: A2W5A1 - Processing student data

### Creation Date: 04-10-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
As Cigdem Okuyucu said this to me; I won't specify how I solved it or what my code is if I didn't
learn anything new in the assignment/problem.

## Code Snippet
```python
def validate_data(line):
    # Init basic variables
    corrupt = False
    invalid_data = []

    # Split the line we are given from the csv file
    studentnr, firstname, surname, birthdate, study = line.split(",")

    # Make a set of the special characters we want to filter out
    special_characters = set("!@#$%^&*()-+?_=,<>/0123456789")

    # Check if our studentnr doesn't start on a '08' or '09'
    if not studentnr.startswith(("08", "09")):
        invalid_data.append(studentnr)
        corrupt = True

    # Check if we have special characters in our firstname
    if any(sc in special_characters for sc in firstname) or firstname == "":
        invalid_data.append(firstname)
        corrupt = True

    # Check if we have special characters in our surname
    if any(sc in special_characters for sc in surname) or surname == "":
        invalid_data.append(surname)
        corrupt = True

    if not birthdate[:4] or int(birthdate[:4]) not in range(1960, 2004):
        invalid_data.append(birthdate)
        corrupt = True

    # If a study is not provided
    if not study or study.upper() not in ["INF", "TINF", "CMD", "AI"]:
        invalid_data.append(study)
        corrupt = True

    # Now, after filtering, we put them in the correct list
    if corrupt:
        line = f"{line} => INVALID DATA: {invalid_data}"
        corrupt_lines.append(line)
    else:
        valid_lines.append(line)
```
