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
    # Variable to store our contact in
    contact_string = ""

    # Format our addressbook
    for contact in addressbook:
        contact_string += "=" * 30 + "\n"
        contact_string += f"Position: {contact[0]}\n"
        contact_string += f"First name: {contact[1]}\n"
        contact_string += f"Last name: {contact[2]}\n"
        contact_string += "Emails: " + ", ".join(contact[3]) + "\n"
        contact_string += "Phone numbers: " + ", ".join(contact[4]) + "\n"
        contact_string += "\n"

    # Return the addressbook so we can print it
    return contact_string


def list_contacts(json, direction):
    # Check if we want to reverse the list (the same as ascending/descending)
    reversed = (direction.upper() == "DESC")

    # Sort the contacts based on the boolean
    sorted_contacts = sorted(json, key=lambda x: x['last_name'], reverse=reversed)

    # Make a list so we can fill the addressbook
    addressbook = []

    # Loop through the sorted contacts
    for i, contact in enumerate(sorted_contacts):
        # Store our new entry in an empty list
        entry = [str(i + 1), contact['first_name'], contact['last_name'], contact['emails'], contact['phone_numbers']]
        addressbook.append(entry)  # Add the entry to the addressbook, which is now sorted

    # Return the sorted list
    return addressbook


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''


def add_contact(new_contact, json_file):
    contacts = read_from_json(json_file)

    id_list = []
    for contact in contacts:
        id_list.append(contact['id'])

    new_contact['id'] = max(id_list) + 1

    contacts.append(new_contact)
    write_to_json(json_file, contacts)

'''
remove contact by ID (integer)
'''


def remove_contact(contact_id, json_file):
    contacts = read_from_json(json_file)

    for contact in contacts:
        if contact['id'] == contact_id:
            contacts.remove(contact)

    write_to_json(json_file, contacts)

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
    # Set action to None as we didn't do anything yet
    action = None

    # If we didn't specify an action, which should be the case, print the command list
    if action is None:
        print("[L] List contacts")
        print("[A] Add contact")
        print("[R] Remove contact")
        print("[M] Merge contacts")
        print("[Q] Quit program")

    while True:
        # Ask for new input and capitalize it
        action = input("").upper()
        action = action.split(" ")

        if action[0] == "L":
            # Read JSON file
            addressbook = read_from_json(json_file)

            # Make our contact list / addressbook
            if len(action) != 2:
                action.append("")
            contact_list = list_contacts(addressbook, direction=action[1])

            # Print our contact list / addressbook
            dis = display(contact_list)
            print(dis)

            # Reset action
            action.clear()
        elif action[0] == "A":
            # Contact to add
            contact = {
                "first_name": "Bob",
                "last_name": "The Builder",
                "emails": [
                    "my@email.com",
                    "my@email.nl"
                ],
                "phone_numbers": [
                    "0881234567",
                    "0101234567"
                ]
            }

            # Add contact
            add_contact(contact, json_file)

            # Reset action
            action.clear()
        elif action[0] == "R":
            # Remove contact
            remove_contact(1, json_file)
        elif action[0] == "Q":
            # Quit script, no need to reset action
            exit(1)


'''
calling main function: 
Do NOT change it.
'''
if __name__ == "__main__":
    main('test_contacts.json')
