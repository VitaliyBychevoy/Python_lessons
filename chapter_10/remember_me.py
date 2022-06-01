import json
"""
def greet_user():
    fileName = 'username.json'
    try:
        with open(fileName) as f:
            user_name = json.load(f)
    except FileNotFoundError:
        user_name = input("What is your name?")
        with open(fileName, 'w') as f:
            json.dump(user_name, f)
            print(f"We`ll remember you, {user_name}")
    else:
        print(f"Welcome back, {user_name}!")

greet_user()
"""
"""
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    user_name = get_stored_username()
    if user_name:
        print(f"Welcome back, {user_name}")
    else:
        user_name = input("What is you name?")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(user_name, f)
            print(f"We will remember you when you come back, {user_name}!")

greet_user()
"""

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    user_name = get_stored_username()
    if user_name:
        print(f"Welcome back, {user_name}")
    else:
        user_name = get_new_username()
        print(f"We will remember you when you come back, {user_name}!")


greet_user()