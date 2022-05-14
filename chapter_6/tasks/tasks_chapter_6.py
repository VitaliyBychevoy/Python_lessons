print("\n\t6.1. Человек.")
human = {
    "first_name": 'Vitalii',
    'last_name': 'Bychevii',
    "age": 31,
    "city": "Kyiv",
    }

print(f"My name is {human['first_name']}.")
print(f"My last name is {human['last_name']}.")
print(f"I'm {str(human['age'])}.")
print(f"I'm  from {human['city']}")


print("\n\t6.2 Любимые числа.")
favorite_numbers = {
    'Tom': 54,
    'Bill': 18,
    "Ann": 9,
    "Julia": 23,
    "Philip": 6,
    }

print(favorite_numbers)

for item in favorite_numbers:
    print(item + " likes number " + str(favorite_numbers[item]))


print("\n\t6.3. Глосарий.")
programming_terms = {
    "variable": "A name that refers to a value.",
    "assignment": "A statement that assigns a value to a variable.",
    "interpreter": "A program that reads another program and execute it.",
    "operator": "A special symbol that represents a simple computation like "
                "addition, multiplication, or string concatenation.",
    "parse": "To examine a program and analyze the syntactic structure.",
    }


print(f"Variable. \n {programming_terms['variable']}")
print(f"Assignment. \n {programming_terms['assignment']}")
print(f"Interpreter.\n {programming_terms['interpreter']}")
print(f'Operator.\n {programming_terms["operator"]}')
print(f"Parsing.\n{programming_terms['parse']}")


print("\n\t6.4. Глосарий 2.")
for key, value in programming_terms.items():
    print(f"{key.title()} - {value.lower()}")

programming_terms["Syntax error"] = "\"Syntax\" refers to the structure of a" \
                                "program and the rules about that structure."
programming_terms["Runtime error"] = "error that appears after started running."
programming_terms['Expression'] = 'A combination of variables, operators, and' \
                                  'values that represent a single result.'
programming_terms['evaluate'] = 'To simplify an expression by performing the' \
                                'operations in order to yield a single value.'
programming_terms['semantic'] = "The meaning of a program."
print("\n")
for key, value in programming_terms.items():
    print(f"{key.title()} - {value.lower()}")


print("\n\t6.5. Реки.")
rivers = {
    'Dnipro': 'Ukraine',
    "Volga": 'Russia',
    "Nile": "Egypt",
    }

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

for key in rivers.keys():
    print(f"{key}")

for value in rivers.values():
    print(f"{value}")


print("\n\t6.6. Опрос.")
favorite_languages = {
    "jen": "python",
    'sarah': 'c',
    "edward": 'ruby',
    "phil": 'python',
    }

list_people = ["tom", 'nina', 'sarah', 'linda', 'bob', 'jen']

for programmer in list_people:
    if programmer in favorite_languages.keys():
        print(f"{programmer.title()}, thank you for taking your time to "
              f"respond to our  survey.")
    else:
        print(f"Hi, {programmer.title()}.Do yo want to take part in the survey")

print("\n\t6.7. Люди.")
human_1 = {
    "first_name": 'Polina',
    'last_name': 'Pitrova',
    "age": 23,
    "city": "Boston",
    }

human_2 = {
    "first_name": 'Mahmud',
    'last_name': 'Ali',
    "age": 41,
    "city": "Paris",
    }


people = []


people.append(human)
people.append(human_1)
people.append(human_2)

for name in people:
    print(f"{name['first_name']} {name['last_name']}. {name['age']} years old."
          f" From {name['city']}.")


print("\n\t6.8. Домашние животные.")
jack = {
    "type_animal": "parrot",
    "name_owner": "Vitaliy",
    }

murka = {
    "type_animal": "cat",
    "name_owner": "Nastia",
    }

gena = {
    "type_animal": "crocodile",
    "name_owner": "Cheburashka",
    }


pets = []

pets.append(jack)
pets.append(murka)
pets.append(gena)

for pet in pets:
    print(f"{pet['type_animal'].title()}'s  owner is {pet['name_owner']}.")
    print("\n")

print("\n\t6.10. Любимые места.")
favorite_numbers_1 = {
    'Tom': [43, 76, 73, 2],
    'Bill': [5, 9, 17],
    "Ann": [4, 32, 45],
    "Julia": [90, 7, 22],
    "Philip": [71, 3],
    }

for key, value in favorite_numbers_1.items():
    print(f"{key}'s favorite numbers:")
    for number in value:
        print(str(number))
    print("\n")

print("\n\t6.11 Любимые числа.")
cities = {
    'London': {
        "country": "UK",
        "population": 24_000_000,
        'fact': "Founded 340",
    },
    'Kyiv': {
        "country": "Ukraine",
        "population": 7_500_000,
        "fact": "Founded 450",
    },
    'Minsk': {
        "country": "Belarus",
        "population": 1_200_000,
        "fact": "Founded 1023",
    },
}


for key, value in cities.items():
    print(f"{key.upper()} in {value['country']}."
          f" Population {value['population']}. {value['fact']}.")


