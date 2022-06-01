import json

fileName = 'username.json'

with open(fileName) as f:
    user_name = json.load(f)
    print(f"Welcome back, {user_name}!")