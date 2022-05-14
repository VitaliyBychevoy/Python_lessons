# -*- coding: utf-8 -*-
"""
print("\n\t 8.1 Сообщение.")
def display_message():
    print("def ключевое слово для создания функции.")
display_message()
"""
"""
print("\n\t 8.2")
def favorite_book(title):
    print(f"My favorite book is {title}.")

favorite_book("Незнайка")
"""
"""
print('\n\t 8.3 Футболка')
def make_shirt(size, text):
    print(f"T-shirt's size is {size}. Text on the T-shirt : {text}")

make_shirt("XL","Hello, Jim.")
make_shirt(size="L", text="Yahooo!")
"""
"""
print("\n\t 8.4 Больщие футболки")
def make_shirt( size = 'L' , text = "I love Python!"):
    print(f"T-shirt's size is {size}. Text on the T-shirt : {text}")

make_shirt()
"""
"""
print("\n\t 8.5 Города")
def describe_city(name_city, country ="Ukraine"):
    print(f"{name_city}  is in {country}.")
describe_city("Lviv")
"""
"""
print("\n\t 8.6 Название городов.")
def city_country(city, coutry):
    return f"{city.title()}, {coutry.title()}."

message_1 = city_country("Kyiv", "Ukraine")
print(message_1)

message_2 = city_country("Lviv", "Ukraine")
print(message_2)

message_3 = city_country("Dnipro", "Ukraine")
print(message_3)
"""

"""
print("\n\t 8.7 Альбом")
def make_album( musician , name_album, number_tracks = None):
    music = {}
    music[musician] = name_album
    if number_tracks != None or number_tracks > 0:
        music["number_traks"] = number_tracks
    return music
"""


"""
album_1 = make_album('Queen', 'Jazz', 12)
album_2 = make_album('ACDC', 'TNT')
album_3 = make_album("Metallica", 'Black albom')
"""

"""
print("\n\t 8.8 Пользователькие альбомы.")
my_music = []
while True:
    print("\nPlease enter musician, album  numbers tracks:")
    print("(enter 'q' at any time to quit)")

    musician = input("Enter musician:\n")
    if musician == 'q':
        break

    album = input("Enter album:\n")
    if album == 'q':
        break

    numbers_track = input("Enter number track")
    if numbers_track == 'q':
        break
    elif numbers_track == 0:
        numbers_track = None

    if numbers_track == '>':
        my_music.append(make_album(musician, album))
    else:
        my_music.append(make_album(musician, album, numbers_track))


for item in my_music:
    print(item)
"""

"""
print("\n\t 8.9 Сообщения")


def show_message(messages):
    for message in messages:
        print(message)

messages = ['Hi!', 'How are you?', 'Where are you?', 'Can you tell me?', 'Ok', 'Yep', 'Maybe', "I'm late."]

show_message(messages)
"""
"""
print("\n\t 8.10 Отправка сообщений")
messages_1 = ['Hi!', 'How are you?', 'Where are you?', 'Can you tell me?', 'Ok', 'Yep', 'Maybe', "I'm late."]
sent_messages_1 = []
def show_message(messages):
    for message in messages:
        print(message)


def send_messages(unsended_messages, sent_message):
    while unsended_messages:
        current_message = unsended_messages.pop()
        print(f'Message:"{current_message}"')
        sent_message.append(current_message)

print("\n\t messages_1")
show_message(messages_1 )
print("\n\t sent_messages_1")
show_message(sent_messages_1)
print("Замена")
send_messages(messages_1 , sent_messages_1)
print("\n\t messages_1")
show_message(messages_1 )
print("\n\t sent_messages_1")
show_message(sent_messages_1)
"""

"""
print("\n\t 8.11 Архивированные сообщения.")

def show_message(messages):
    for message in messages:
        print(message)

def send_messages(unsended_messages, sent_message):
    while unsended_messages:
        current_message = unsended_messages.pop()
        print(f'Message:"{current_message}"')
        sent_message.append(current_message)

messages_2 = ['Why?', 'How?', 'What?', 'Where?']
sent_messages_2 = []

print("Перенос из копии messages_2")
send_messages(messages_2[:], sent_messages_2)

print("Список messages_2")
show_message(messages_2)
"""

"""
print("\n\t 8.12 Сэндвичи")
def get_sandwish(*toppings):
    print("\n\t Sandwich with next toppings:")
    for topping in toppings:
        print(f"-{topping}")
    print("\n")


get_sandwish("topping 1")
get_sandwish("topping 9", "topping 3", "topping 6", "topping 4")
get_sandwish("topping 9", "topping 3")
"""
"""
print("\n\t 8.13 Сэндвичи")

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return  user_info

user_1 = build_profile('Vitalii', 'Bychevoi', Age = 31, language = 'ua')
print(user_1)
"""
"""
print("\n\t 8.14 Автомобили.")

def make_car(manufacture, model, **kwargs):
    kwargs['manufacture'] = manufacture,
    kwargs['model'] = model
    return kwargs

car_1 = make_car('subaru', 'outback', color = 'blue', two_package=True)
car_2 = make_car('bmw', 'outback', color = 'red', two_package=False)
car_3 = make_car('audi', 'outback', color = 'Green', two_package=True)

print(car_1)
"""

print("\n\t 8.15 Печать моделей.")