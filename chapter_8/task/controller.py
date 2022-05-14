def create_user_name(name):
    print(f"User name: {name.title()}.")
    return name.title()


def age_user(age:int):
    print(f"Age user: {age}")
    return age


def create_user(name, age):
    print("\n Creating new user with:")
    user={}
    user['user_name'] = name
    user['age user'] = age
    return user

def show_user(user):
    print(user['user_name'])
    print(user['age user'])
