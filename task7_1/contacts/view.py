def print_contacts(contacts):
    print("\nContact list:")
    if contacts:
        print('\n'.join(contacts))
    else:
        print("Empty")


def print_message(message):
    print(message)


def get_input_line(message):
    return input(message)


def menu_option():
    while True:
        print("\nPress 1 to add new contact")
        print("Press 2 to print all full contacts")
        print("Press 3 to print all first and last name of contacts")
        print("Press 4 to sort contacts by id")
        print("Press 5 to sort contacts by name")
        print("Press 6 to remove all contacts")
        print("Press 7 to Quit\n")

        choice = input("Your choice: ")

        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Invalid! Try Again\n")
            continue

        return int(choice)


def input_contact():
    while True:
        line = input("Enter id, name, last name, phone number, comment separated by commas or empty line to cancel:\n")
        if not line:
            return ''
        contact = [item.strip() for item in line.split(',')]
        if len(contact) != 4:
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
        return contact
