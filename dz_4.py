USERS = {}
def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner

@ error_handler
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f'User {name} added with number: {phone}'

@ error_handler
def change_phone(args):
    name, phone = args
    USERS[name] = phone
    return f'User {name} changed the phone, his new number: {phone}'

@ error_handler
def show_all(_):
    string = ''
    for k, v in USERS.items():
        string += f'{k}: {v} '
    return(string)

@ error_handler
def show_phone(args):
    name = args[0]
    phone = USERS[name]
    return f'{name}: {phone}'

def hello(_):
    return "How can I help you?"

def exit(_):
    return "Good bye!"

HANDLER = {
        
            "hello": hello,
            "good bye": exit,
            "close": exit,
            "exit": exit,
            "add": add_user,
            "change": change_phone,
            "show all": show_all,
            "phone": show_phone
}

def parser(user_input):
    
    user_input = user_input.split()
    if len(user_input) == 3:
        cmd, *args = user_input
    else:
        cmd, *args = ' '.join(user_input[0:2]), user_input[2:]
        
    try:
        handler = HANDLER[cmd.lower()]
    except KeyError:
        if args:
            cmd = f"{cmd} {args[0]}"
            args = args[1:]
            args = args[2:]
        handler = HANDLER[cmd, "Unknown command"]
    return handler, args

def main():
    while True:
        user_input = input()
        handler, *args = parser(user_input)
        print(len(*args))
        result = handler(*args)
        if not result:
            print("Good bye!")
            break
        print(result)

    
        
if __name__ == "__main__":
      main()
   