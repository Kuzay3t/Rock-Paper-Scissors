# Building a Contact Book using python
contact_book = {}
print("Welcome to the Contact Book")

def display():
    print("Name:Phone Number")
    for key in contact_book:
        print(f"{key}:{contact_book[key]}")
while True:
    user_activity = int(input("""What operation do you want to perform? \n
                            1. Add contact
                            2. Delete contact
                            3. Update contact
                            4. View contact
                            5. Quit \n
                             >>> """))

    if user_activity == 1:
        # Add contact
        name = input("Enter the contacts name: \n")
        phone_number = int(input("Enter the mobile number: \n"))
        contact_book[name] = phone_number
    elif user_activity == 2:
        # Delete Contact
        del_contact = input("Enter the contact to be deleted: \n")
        if del_contact in contact_book:
            confirm = input("Do you want to delete this contact(yes or no): \n").lower()
            if confirm == 'yes':
                contact_book.pop(del_contact)
        else:
            print("Name is not found in contact book")
    elif user_activity == 3:
        # update contact
        edit_contact = input("Enter the contact name to be edited: \n")
        if edit_contact in contact_book:
            phone = input("Enter mobile number")
            contact_book[edit_contact] = phone
        else:
            print("Name is not found in contact book. ")
    elif user_activity == 4:
        # view contact
        if not contact_book:
            print("Your Contact Book is Empty")
        else:
            display()
    elif user_activity == 5:
        break
    else:
        print("Invalid Operation! Try Again!")