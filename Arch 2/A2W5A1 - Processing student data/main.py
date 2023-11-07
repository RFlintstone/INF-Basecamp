import os
import sys

valid_lines = []
corrupt_lines = []

'''
The validate_data function will check the students.csv line by line for corrupt data.

- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.

Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.

Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:

0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']

In the above example the studentnumber does not start with '08' or '09',
the last name contains a special character and the student program is empty.

Don't forget to put the students.csv file in the same location as this file!
'''


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


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')