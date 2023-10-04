import os
import sys
import json

'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''


def display(addressbook: list):
    ...


'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''


def list_contacts(json, direction):
    if direction.upper() == "DESC":
        reverse = True
    else:
        reverse = False

    sorted_contacts = sorted(json, key=lambda x: x['last_name'], reverse=reverse)

    addressbook = ""

    for i, contact in enumerate(sorted_contacts):
        addressbook += "=" * 30
        addressbook += f"\nPosition: {i + 1}\n"
        addressbook += f"First name: {contact['first_name']}\n"
        addressbook += f"Last name: {contact['last_name']}\n"

        count = 0
        addressbook += "Emails: "
        for email in contact['emails']:
            addressbook += f"{email}"
            if count + 1 != len(contact['emails']):
                addressbook += ", "
            count += 1

        count = 0
        addressbook += "\nPhone numbers: "
        for number in contact['phone_numbers']:
            addressbook += f"{number}"
            if count + 1 != len(contact['phone_numbers']):
                addressbook += ", "
            count += 1
        addressbook += "\n"
    return addressbook


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''


def add_contact(_variable_here):
    print("todo: implement this function")


'''
remove contact by ID (integer)
'''


def remove_contact(contact_id):
    print("todo: implement this function")


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''


def merge_contacts():
    print("todo: implement this function")


'''
read_from_json
Do NOT change this function
'''


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in data:
            addressbook.append(contact)

    return addressbook


'''
write_to_json
Do NOT change this function
'''


def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


'''
main function:
# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [L] List contacts
# [A] Add contact
# [R] Remove contact
# [M] Merge contacts
# [Q] Quit program
Don't forget to put the contacts.json file in the same location as this file!
'''


def main(json_file):
    action = None
    addressbook = read_from_json(json_file)

    if action is None:
        print("[L] List contacts")
        print("[A] Add contact")
        print("[R] Remove contact")
        print("[M] Merge contacts")
        print("[Q] Quit program")

    while True:
        action = input("").upper()

        if action == "L":
            list = list_contacts(addressbook, direction="ASC")
            print(list)
            action = None
        elif action == "Q":
            exit(1)


'''
calling main function: 
Do NOT change it.
'''
if __name__ == "__main__":
    main('contacts.json')
