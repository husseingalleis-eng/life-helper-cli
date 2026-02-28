import json
all_contact = []
path = 'C:\\Users\\HUSSEIN MUHAMED\\.vscode\\codes\\Python\\tools\\' + ("records.json")


def json_data_manager():
    print("\nWelcome to JSON Data Manager\n")
    
    global all_contact
    
    def write_list(record):
        with open(path, 'w') as f:
            record = json.dump(record, f,indent= 3)
    try:
        f = open(path)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(path, 'w') as f:
            all_contact = []
            write_list(all_contact)
    with open(path, 'r') as f:
        all_contact =  json.load(f)
        write_list(all_contact)
        
    i = 1
    for record in all_contact:
        print(   str(i) + " - " + str(record)  )
        i +=1

    while True:
        try:
            print("The operations are: ")
            print("1- Create contact\n2- View contacts\n3- Update contact\n4- Delete contact\n ")
            your_operation = int(input("Select your operation please: "))
            break
        except ValueError:
            print("You must enter a number? ")

    match your_operation:
        case 1:
            your_operation = 'create contact'
            name = input("Enter your name:")
            while True:
                try:
                    phone = int(input("Enter your phone number: "))
                    break
                except ValueError:
                        print("please enter a number")
            email = input("Enter your eamil: ")
            contact = {
                "name": name,
                "phone": phone,
                "email": email
            }
            all_contact.append(contact)
            write_list(all_contact)
        
        case 2:
            your_operation = 'view contact'
            print(f"Your contact is: {all_contact}")
            write_list(all_contact) 
    
        case 3:
            your_operation = 'update contact'
            while True:
                if not all_contact:
                    print("Wearning: You don't have contact to update! create a contact first? ")
                    break
            while True:    
                try:
                    
                    update_contact = int(input("Enter the number of the contact you want to update: "))
                    
                    break
                except ValueError:
                    print("You must enter a number? (Try again)")
        
            if update_contact <= 0:
                print("You must enter a number greater then zero!")
            else:
                update_name = input("Enter the update name:")
                while True:
                    try:
                        update_phone = int(input("Enter your phone number: "))
                        break
                    except ValueError:
                            print("please enter a number")
                update_email = input("Enter your eamil: ")
                all_contact.pop(update_contact - 1)
                contact = {
                    "name" : update_name,
                    "phone": update_phone,
                    "email": update_email
                    
                    }
                all_contact.append(contact)
                write_list(all_contact)
                
        case 4:
            your_operation = 'delete contact'
            while True:
                if not all_contact:
                    print("Wearning: You don't have contact to remove! create a contact first? ")
                    break
            while True:
                try:
                    delete_contact = int(input("Enter the number of the contact you want to delete: "))
                    if delete_contact <= 0:
                        print("You must enter a number greater then zero!")
                    else:
                        all_contact.pop(delete_contact - 1)
                        write_list(all_contact)
                    break
                except ValueError:
                    print("please enter a number")
      
        case _:
            print("You must enter a number between 1 to 4? (try again):")
            


