import os
import sys
import json


def validate(f_name, l_name, emails, phone,):
    if f_name.isalpha() and l_name.isalpha():
        if any("@" in email for email in emails):
            for phone_number in phone:
                if phone_number.isdigit():
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


def new_id():
    return len(read_from_json("contacts.json")) + 1


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
def list_contacts():
    pass
    # todo: implement this function
    ...

    # return addressbook


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''
def add_contact():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email_adresses = list(input("Emails: ").split(","))
    phone_numbers = list(input("Phone numbers: ").split(","))
    if validate(first_name, last_name, email_adresses, phone_numbers):
        id = new_id()
        new_contact = {"id": id, "first_name": first_name, "last_name":
            last_name, "emails": email_adresses,"phone_numbers": phone_numbers}
        print(new_contact)
        
        print("Contact added to addressbook")
        main("contacts.json")
    else:
        print("idfk")
    # print(first_name, last_name, emails, phone_numbers)

'''
remove contact by ID (integer)
'''
def remove_contact():
    # todo: implement this function
    pass


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


def main(json_file):
    addressbook = read_from_json(json_file)
    print("""
Menu
[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program""")
    while True:
        option = input("").lower()
        if option == "l":
            list_contacts(addressbook)
            break
        elif option == "a":
            add_contact()
            break
        elif option == "r":
            remove_contact()
            break
        elif option == "m":
            merge_contacts()
            break
        elif option == "q":
            quit()
        else:
            print("That is not a valid option")
            continue
    

if __name__ == "__main__":
    main('contacts.json')