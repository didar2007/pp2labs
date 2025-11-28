from db2 import (
    insert_from_console,
    insert_from_csv,
    update_name,
    update_phone,
    show_all,
    search_by_name,
    search_by_phone,
    delete_by_name,
    delete_by_phone
)

def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Add contact (console)")
        print("2. Add contacts (CSV)")
        print("3. Show all")
        print("4. Search by name")
        print("5. Search by phone")
        print("6. Update name")
        print("7. Update phone")
        print("8. Delete by name")
        print("9. Delete by phone")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)
        elif choice == "3":
            show_all()
        elif choice == "4":
            name = input("Enter name to search: ")
            search_by_name(name)
        elif choice == "5":
            phone = input("Enter phone to search: ")
            search_by_phone(phone)
        elif choice == "6":
            old = input("Old name: ")
            new = input("New name: ")
            update_name(old, new)
        elif choice == "7":
            old = input("Old phone: ")
            new = input("New phone: ")
            update_phone(old, new)
        elif choice == "8":
            name = input("Name to delete: ")
            delete_by_name(name)
        elif choice == "9":
            phone = input("Phone to delete: ")
            delete_by_phone(phone)
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
