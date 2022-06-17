import interface as inter
import print_contacts as contacts
import find_phonebook

command = True
while command:
    command = inter.main_menu()
    if command == 1: contacts.print_all_contacts()
    elif command == 2:
        contact = find_phonebook(inter())
        contacts.print_contact(contact)
        