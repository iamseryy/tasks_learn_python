import os
import task7_1.contacts.view as view


def get_all_full_contacts():
    file = 'task7_1/contacts/contacts.txt'

    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as contacts_file:
            return [line.strip() for line in contacts_file]
    except IOError:
        view.print_message("I/O error")


def get_all_shot_contacts():
    file = 'task7_1/contacts/contacts.txt'

    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as contacts_file:

            return [f"{line.split(',')[1].strip()}, {line.split(',')[2].strip()}" for line in contacts_file]
    except IOError:
        view.print_message("I/O error")
