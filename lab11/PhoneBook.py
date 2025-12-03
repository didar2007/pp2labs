from db2 import (
    insert_from_console,
    insert_from_csv,
    update_name,
    update_phone,
    show_all,
    search_by_name,
    search_by_phone,
    delete_by_name,
    delete_by_phone,
    get_page
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
        print("10. Pagination")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            filename = input("CSV filename: ")
            insert_from_csv(filename)
        elif choice == "3":
            show_all()
        elif choice == "4":
            search_by_name(input("Name: "))
        elif choice == "5":
            search_by_phone(input("Phone: "))
        elif choice == "6":
            update_name(input("Old name: "), input("New name: "))
        elif choice == "7":
            update_phone(input("Old phone: "), input("New phone: "))
        elif choice == "8":
            delete_by_name(input("Name: "))
        elif choice == "9":
            delete_by_phone(input("Phone: "))
        elif choice == "10":
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            rows = get_page(limit, offset)
            for r in rows:
                print(r)
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
