import json
import os

CONTACT_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f, indent= 4)

def add_contacts(contacts):
    name = input("Enter Name: ").strip().lower()
    phone = input("Enter phone: ").strip().lower()
    email = input("Enter email: ").strip().lower()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added.")

def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()
    if name in contacts:
        print(f"{name} - {contacts[name]['phone']} | {contacts[name]['email']}")
    else:
        print("Contact not found.")
    
def update_contact(contacts):
    name = input("Enter name to update: ").strip().lower()
    if name in contacts:
        phone = input("New Phone: ").strip()
        email = input("New Email: ").strip()
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated.")
    else:
        print("Contacts not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contacts deleted.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu")
        print("\nAdd Contact")
        print("\nSearch Menu")
        print("\nUpdate Contact")
        print("\nDelete Contact")
        print("\nExit")

        choice  = input("Choose an option: ").strip()
        if choice == '1':
            add_contacts(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice =='3':
            update_contact(contacts)
        elif choice =='4':
            delete_contact(contacts)
        elif choice =='5':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice.")
        
if __name__ == "__main__":
    main()