def get_menu_option():
    while True:
        print("\nPress 1 to add new contact")
        print("Press 2 to print all contacts")
        print("Press 3 to sort contacts by name")
        print("Press 4 to sort contacts by id")
        print("Press 5 to sort contacts by id")
        print("Press 6 to print all first and last names")
        print("Press 7 to Quit\n")

        choice = input("Your choice: ")

        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Invalid! Try Again\n")
            continue

        return int(choice)


def add_contact():
    while True:
        contact = input("Enter id, name, last name, phone number, comment separated by commas or Cancel:\n").split(',')
        contact = [item.strip() for item in contact]
        if contact[0] == 'Cancel':
            return False
        elif len(contact) != 4:
            print("Invalid! Try Again\n")
            continue
        elif not contact[0].isdigit():
            print("Invalid id field, it should contain numbers! Try Again\n")
            continue
        elif not contact[1].isalpha():
            print("Invalid Name field! Try Again\n")
            continue
        elif not contact[2].isalpha():
            print("Invalid Last name field! Try Again\n")
            continue
        elif len(contact[3]) != 12 or contact[3][0] != '+' or not contact[3][1: len(contact[3])].isdigit():
            print("Invalid Phone number field, it should be like +79999999999! Try Again\n")
            continue

        return save(contact)


def save(contact):
    file = 'task7_1/contacts/contacts.txt'

    try:
        with open(file, 'a') as contacts:
            contacts.write(', '.join(contact) + '\n')
    except IOError:
        print("I/O error")
        return False

    return True
