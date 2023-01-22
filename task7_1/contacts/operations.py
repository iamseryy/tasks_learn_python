def sort_by_id(contacts):
    return sorted(contacts, key=lambda contact: int(contact.split(',')[0].strip()))


def sort_by_name(contacts):
    return sorted(contacts, key=lambda contact: contact.split()[1].strip())
