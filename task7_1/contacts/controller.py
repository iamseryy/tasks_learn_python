import task7_1.contacts.import_data as import_data
import task7_1.contacts.view as view
import task7_1.contacts.export_data as export_data
import task7_1.contacts.operations as operations


def start():
    while True:
        choice = view.menu_option()

        if choice == 1:
            if import_data.add_contact():
                view.print_message("\nContact added")
            else:
                view.print_message("\nContact not added")
            continue
        elif choice == 2:
            view.print_contacts(export_data.get_all_full_contacts())
            continue
        elif choice == 3:
            view.print_contacts(export_data.get_all_shot_contacts())
            continue
        elif choice == 4:
            contacts = export_data.get_all_full_contacts()
            if contacts:
                contacts = operations.sort_by_id(contacts)
                import_data.remove_all_contacts()
                import_data.save_contacts(contacts)
                view.print_message("\nSorted")
            else:
                view.print_message("\nNothing to sort")
            continue
        elif choice == 5:
            contacts = export_data.get_all_full_contacts()
            if contacts:
                contacts = operations.sort_by_name(contacts)
                import_data.remove_all_contacts()
                import_data.save_contacts(contacts)
                view.print_message("\nSorted")
            else:
                view.print_message("\nNothing to sort")
            continue
        elif choice == 6:
            import_data.remove_all_contacts()
            view.print_message("All contacts deleted")
            continue
        elif choice == 7:
            view.print_message("\nBye")
            quit()
