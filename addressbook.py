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
def list_contacts(...):
    # todo: implement this function
    ...

    return addressbook


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''
def add_contact(...):
    # todo: implement this function
    ...


'''
remove contact by ID (integer)
'''
def remove_contact(...):
    # todo: implement this function
    ...


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''
def merge_contacts():
    # todo: implement this function
    ...


'''
read_from_json
Do NOT change this function
'''
def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            addressbook.append(contact)

    return addressbook


'''
write_to_json
Do NOT change this function
'''
def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent = 4)

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
    addressbook = read_from_json(json_file)

    # todo: implement this function.
    

'''
calling main function: 
Do NOT change it.
'''
if __name__ == "__main__":
    main('contacts.json')
