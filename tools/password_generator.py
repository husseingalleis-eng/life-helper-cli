import string
import random
def password_generator():
    print("\nWelcome to Password Generator\n")
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    
    password = True
    while password:
        while True:
            try:
                password_length =int(input("Enter the length of your password: "))
                if password_length > 0:
                    break
                else:
                    print("You must enter a Number > Zero? try again")
            except ValueError:
                print("You must enter a number? try again")
        
        print("\nSelect the password types you want: ")
        print("1- Do you want letters?\n2- Do you want numbers?\n3- Do you want symbols?")
        print("4- Do you watn letters with numbers?\n5- Do you watn letters with symbols?")
        print("6- Do you watn letters with symbols with numbers?\n")

        while True:
            try:
                your_password = ""
                choice = int(input("Select your choice please: "))
                match choice:   
                    case 1:
                        for i in range(password_length):
                            your_password += random.choice(letters)
                        print(f"Your password is {your_password}")
                        break                  
                    case 2:
                        for i in range(password_length):
                            your_password += random.choice(numbers)
                        print(f"Your password is {your_password}")
                        break
                    case 3:
                        for i in range(password_length):
                            your_password += random.choice(symbols)
                        print(f"Your password is {your_password}")
                        break
                    case 4:
                        for i in range(password_length):
                            your_password += random.choice(letters + numbers)
                        print(f"Your password is {your_password}")
                        break  
                    case 5:
                        for i in range(password_length):
                            your_password += random.choice(letters + symbols)
                        print(f"Your password is {your_password}")
                        break  
                    case 6:
                        for i in range(password_length):
                            your_password += random.choice(letters + numbers + symbols)
                        print(f"Your password is {your_password}")
                        break
                    case _:
                        print("Invalid selection! Try between 1 to 6?")
            except ValueError:
                print("You must select a number? Try again please")
        password = False

