def add_contact():
    with open("phonebook.txt", "a") as file:
        name = input("Enter name: ")
        birthday = input("Enter birthday (Month): ")
        gender = input("Enter gender: ")
        age = input("Enter age: ")
        contact_number = input("Enter contact number: ")
        file.write(f"{name} {birthday} {gender} {age} {contact_number}\n")
        print("Contact added successfully.")

def view_contacts():
    try:
        with open("phonebook.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
                return
            for i, contact in enumerate(contacts, start=1):
                print(f"\nContact #{i}\n")
                print(contact.strip())
    except FileNotFoundError:
        print("No contacts found. Please add a contact first.")

def main():
    while True:
        print("\n1) Add Contact")
        print("2) View Contact")
        print("3) Exit")
        option = input("Option: ")

        if option == '1':
            add_contact()
        elif option == '2':
            view_contacts()
        elif option == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose '1', '2', or '3'.")

if __name__ == "__main__":
    main()