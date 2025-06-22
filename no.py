import json
import os

CONTACT_FILE = 'contacts.json'

# Load existing contacts from file
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save updated contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add contact
def add_contacts(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    key = name.lower()
    contacts[key] = {"original_name": name, "phone": phone, "email": email}
    print("Contact added.")

# Search contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()
    if name in contacts:
        data = contacts[name]
        print(f"{data['original_name']} - 📞 {data['phone']} | 📧 {data['email']}")
    else:
        print("Contact not found.")

# Update contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip().lower()
    if name in contacts:
        phone = input("New Phone: ").strip()
        email = input("New Email: ").strip()
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        print("Contact updated.")
    else:
        print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().lower()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main program loop
def main():
    contacts = load_contacts()
    while True:
        print("\n📒 Contact Book Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            add_contacts(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")

if __name__ == "__main__":
    main()