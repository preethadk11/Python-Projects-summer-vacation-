#contact book
contacts = {
    "Alice": "9876543210",
    "Bob": "9123456789"
}
def add_contact():
    contact=input("Enter the contact name: ").capitalize()
    if contact in contacts:
        print("Contact already exists")
    else:
        while True:
            phone=input("Enter the phone number: ")
            if phone.isdigit() and len(phone)==10:
                contacts[contact]=phone
                print("Contact added successfully!")
                break
            else:
                print("Phone number must contain only digits\nAnd must be exactly 10 digits")
def search_contact():
    search=input("Enter contact name: ")
    for name in contacts:
        if search.lower()==name.lower():
            print(f'Phone number: {contacts[name]}')
            break
    else:
        print("Contact not found")
def update_contact():
    update=input("Enter contact name: ")
    flag=False
    for name in contacts:
        if update.lower() == name.lower():
            flag=True
            break
    if flag:
        while True:
            new_phone=input("Enter new phone number: ")
            if new_phone.isdigit() and len(new_phone)==10:
                contacts[name]=new_phone
                print("Contact updated successfully")
                break
            else:
                print("Phone number must be exactly digits\nAnd must have 10 digits")
    else:
        print("Contact not found")
def delete_contact():
    del_contact=input("Enter contact name: ")
    for name in contacts:
        if del_contact.lower()==name.lower():
            confirm=input("Are you sure? (yes/no): ").lower()
            if confirm=="yes":
                del contacts[name]
                print("Contact deleted successfully")
                break
            else:
                print("Contact not deleted")
    else:
        print("Contact not found")
def view_contact():
    if contacts:
        sorted_key=sorted(contacts.keys())
        for name in sorted_key:
            print(name,":",contacts[name])
    else:
        print("No contacts available")
def total_contact():
    print(f'Total contacts: {len(contacts)}')
def search_phone():
    while True:
        num=input("Enter phone number: ")
        if num.isdigit() and len(num)==10:
            for name,phone in contacts.items():
                if num==phone:
                    print(f'Contact name: {name}')
                    break
            else:
                print("Number not found")
            break
        else:
            print("Enter correct phone number")
def partial_search():
    partial=input("Enter contact name: ")
    found=False
    for name in contacts:
        if partial.lower() in name.lower():
            print(name)
            found=True
    if not found:
        print("Contact not found")

menu="\n\t\t====Contanct Book====\n\n1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact\n5. View all Contact\n6. Total contacts\n7.Search by phone number\n8.Partial search\n9.Exit"
while True:
    print(menu)
    choice=input("Enter your choice: ")
    if choice.isdigit():
        choice=int(choice)
        if choice==1:
            add_contact()
        elif choice==2:
            search_contact()
        elif choice==3:
            update_contact()
        elif choice==4:
            delete_contact()
        elif choice==5:
            view_contact()
        elif choice==6:
            total_contact()
        elif choice==7:
            search_phone()
        elif choice==8:
            partial_search()
        elif choice==9:
            print("Thank you for using contact book")
            break
        else:
            print("Enter correct choice!")
            continue
    else:
        print("The choice should be of digit")


