def input_error(func):
    def check(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print( "Enter  right user name")
            return main()
        except ValueError:
            print ("Give me name and phone please")
            return main()
        except IndexError:
            print ("Contact not found")
            return main()
    return check

phone_book={}
Status =True
def hello():
    return "How can I help you?"

def adder(name,phone):
    phone_book[name] = phone
    return f"Contact {name} added with phone {phone}"


def change_contact(name,phone):
    del phone_book[name]
    phone_book[name] = phone
    return f"Phone number for {name} changed to {phone}"

def found_contact(name):
        return f"Phone number for {name}: {phone_book[name]}"


def show_all():
    result = "Contacts:\n"
    for name, phone in phone_book.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def stop():
    global Status 
    Status = False
    return 'Good bye!'


def split(user_input):
    if len(user_input.split()) == 3:
        _, name, phone = user_input.split()
        return name,phone
    else: 
        _, name= user_input.split()
        return name

    

@input_error
def main():
    while Status:
        user_input = input("Enter a command: ").lower()
        if user_input.startswith('hello'):
            print(hello())
        elif user_input.startswith('add'):
            name,phone = split(user_input)
            print(adder(name,phone))
        elif user_input.startswith('change'):
            name,phone = split(user_input)
            print(change_contact(name, phone))
        elif user_input.startswith('phone'):
            name= split(user_input)
            print(found_contact(name))
        elif user_input == 'show all':
            print(show_all())
        elif user_input in ["good bye", "close", "exit"]:
            print(stop())
            break
        else: print('Command not found, check input')

main()