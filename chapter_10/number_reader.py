import json

fileName = 'numbers.json'

with open(fileName)as f:
    number = json.load(f)

print(number)