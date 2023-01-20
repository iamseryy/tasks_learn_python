import task7_1.contacts.import_data as import_data


def start():
    while True:
        choice = import_data.get_menu_option()

        if choice == 1:
            if import_data.add_contact():
                print("Contact added")
            else:
                print("Contact not added")
            continue
        elif choice == 7:
            print("Bye")
            quit("Bye")

