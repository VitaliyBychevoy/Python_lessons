import json

fileName = 'username.json'

user_name = input("What is your name?\n")

with open(fileName, 'w') as f:
    json.dump(user_name, f)
    print(f"We'll remember you when you come back, {user_name}!")