import task7_1.contacts.view as view


def add_contact():
    contact = view.input_contact()
    if contact:
        contacts = [", ".join(contact)]
        return save_contacts(contacts)
    else:
        return False


def save_contacts(contacts):
    file = 'task7_1/contacts/contacts.txt'

    try:
        with open(file, 'a') as contacts_file:
            for contact in contacts:
                contacts_file.write(contact + '\n')
    except IOError:
        view.print_message("I/O error")
        return False

    return True


def remove_all_contacts():
    file = "task7_1/contacts/contacts.txt"
    open(file, 'w').close()
