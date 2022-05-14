"""
print("\n\t7.1. Прокат машин.")
car = input("Hello! Choose a car.")
print(f"Let me see if I car find you a {car}.")
"""
"""
print("\n\t7.2. Заказ стола.")
place = input("How many places you want to book?\n")
place = int(place)

if place > 8:
    print("You need wait.")
else:
    print(f"Your table for {place} person  is ready.")
"""
"""
print("\n\t7.3. Числа, кратные 10.")
number = int(input("Enter number."))

if number % 10 == 0:
    print(f"Number {number} is a multiple of 10.")
else:
    print(f"Number {number} is not a multiple of 10.")
"""
"""
print("\n\t7.4. Топпинг для пиццы:")
message = ""

flag = True
while flag:
    topping = input("Enter topping for pizza.\n(Enter 'quit' for exit)\n")

    if topping == "quit":
        flag = False
        print("Your toppings")
        print(message)
    else:
        message += topping
        message += "\n"
        print("Your toppings")
        print(message)
"""
"""
print("\n\t7.5. Билеты в кино:")
flag = True

while flag:
    age = int(input("Enter your age:\n"))
    if age < 3:
        print("Free tickets.")
        flag = False

    elif 3 <= age < 12:
        print("Price ticket is 10$.")
        flag = False
    elif age > 15:
        print("Price ticket is 15$.")
        flag = False
    else:
        print(f"You entered {age}. Enter integer number.")
"""
"""
print("\n\t7.6. Три выхода.")
active = True
message = ""

while active:
    topping = input("Enter topping for pizza.\n(Enter 'quit' for exit)\n")
    if topping == "quit":
        print("Your toppings")
        print(message)
        break
    else:
        message += topping
        message += "\n"
        print("Your toppings")
        print(message)
"""
"""
print("\n\t7.7 Бесконечный цикл.")

while True:
    print("Бесконечный цикл.")

"""
"""
print("\n\t7.8. Сеэндвичи:")
sandwich_orders = ["Донер Кебаб", "Сэндвич Веджимайт", "Чемита", ]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

print("\nFinished sandwich:")
for sandwich in sorted(finished_sandwiches):
    print(f"{sandwich}")
"""
"""
print("\n\t7.9 Без пастрами.")
sandwich_orders = ["Донер Кебаб", 'pastrami', "Сэндвич Веджимайт", 'pastrami',
                   "Чемита", 'pastrami']
print(id(sandwich_orders))
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('We have not pastrami.')
for item in sandwich_orders:
    print(item)
print(id(sandwich_orders))
"""

print("\n\t7.10 Отпуск мечты")
responses = {}

while True:
    name = input("What is your name?")
    location = input("Where do you want to spend vocation?")
    responses [name] = location
    action = input("Would you like to let another person respond?(yes/ no)")
    if action == 'no':
        break

for name, location in responses.items():
    print(f"{name} wants to spend vocation in {location}")