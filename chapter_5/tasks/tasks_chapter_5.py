print("\n\t 5.1. Проверка условй.")
cars = ['audi', 'bmw', 'subaru', 'toyota']

car = 'subaru'
print("1.Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\n2.Is car == 'audi'? I predict False.")
print(car == "audi")

print("\n3.Is 'opel' in the list? I predict False.")
if 'opel' in cars:
    print("True.")
else:
    print("False.")

print("\n4.Is 'audi' in the list? I predict True.")
if 'audi' in cars:
    print("True.")
else:
    print("False.")

wheel = 4
print("\n5. 4 wheels. I predict true.")
if wheel >= 4:
    print("True")
else:
    print("False")

wheel = 12
print("\n6. 7 wheel. I predict false.")
if wheel <= 7:
    print("True")
else:
    print("False")

print("\n7. Work 5 days.I predict true.")
work_days = 5
if work_days > 3 and work_days < 12:
    print("True.")
else:
    print("False.")

print("\n8. 5 days off.I predict false.")
work_days = 2
if work_days > 4 and work_days < 6:
    print("True.")
else:
    print("False.")

print("\n9. 76. I perdict True")
number =  14
if number != 0:
    print("True")
else:
    print("False")

print("\n10. Audi. I predict false.")
my_car = 'audi'
if my_car.title() == "Audi":
    print("True")
else:
    print("False")


print("\n\t 5.2. Больше словий.")
customer = ["Tom", "Greg", "Bob", "Alice", "rita", "alex"]
circle = [50, 3.15, 79]

print("\nРавенство строк.")
name = 'bob'
if name == customer[2]:
    print("True")
else:
    print("False")

print("\nНеравенство строк.")
name_1 = 'Jim'
if name_1 != customer[2]:
    print("True")
else:
    print("False")

print("\nПроверка с использованием функции lower()")
name_2 = 'Rita'
if name_2.lower() == customer[4]:
    print(f"{name_2} is our customer.")
else:
    print(f"{name_2} isn`t in our customer.")

print("\nПроверка ключевыми словами and и or")
name_3 = "Tim"
name_4 = "Bob"
if name_3 not in customer and name_4 in customer:
    print(f"{name_3} is not in list. {name_4} in list.")
else:
    print("Condition is not met.")


print("\n\t5.3. Цвета 1.")
alien_color = 'green'
if alien_color == "green":
    print("You have 5 points.")
if alien_color == "red":
    print("You have 5 points.")


print("\n\t5.4. Цвета 2.")
if alien_color == "green":
    print("You have 5 points.")
else:
    print("You get 10 points.")


print("\n\t5.5. Цвета 3.")
alien_color = "green"
if alien_color == "green":
    print("You get 5 points.")
elif alien_color == "yellow":
    print("You get 10 points.")
elif alien_color == "red":
    print("You get 15 points.")
else:
    pass


print("\n\t5.6. Периоды жизни.")
age = 64
if age < 2:
    print("Младенец")
elif age >= 2 and age < 4:
    print("Малыш")
elif age >=4 and age < 13:
    print("Ребенок")
elif age >= 13 and age < 20:
    print("Подросток")
elif age >= 20 and age < 65:
    print("Взрослый")
else:
    print("Пожилой человек.")


print("\n\t5.7. Любимый фрукт.")
favorite_fruits = ["Персик", "Банан", "Яблоко"]
if "Манго" in favorite_fruits:
    print(f"Манго мой любимый фрукт.")
if "Гранат" in favorite_fruits:
    print("Гранат мой любмый фрук")
if "Банан" in favorite_fruits:
    print("Банан мой любимый фрукт")
if "Слива" in favorite_fruits:
    print("Слива мой любимый фрукт")
if "Персик" in favorite_fruits:
    print("Персик мой любимый фрукт")


print("\n\t5.8. Hello Admin.")
#users = ['tom', 'jim', 'ann', 'pit', 'admin', 'tina']
users = []

if not users:
    print("We need to ind some users!")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")


print("\n\t5.10. Проверка имен пользователей:")
current_users = ['Andy', 'Leo', 'Ron', 'Ada', 'Tom']
new_users = ['Paula', "Randy", "Leo", "Jack", "ADA"]
current_users_2 = current_users[:]

for user in new_users:
    if user in current_users or user.capitalize() in current_users:
        print(f"{user} is already used, enter another name.")
    else:
        print(f"{user} is available name.")


print("\n\t5.11. Порядковые числительные.")
digits = [number for number in range(1, 10)]

for digit in digits:
    if digit == 1:
        print(f"{digit}st")
    elif digit == 2:
        print(f"{digit}nd")
    elif digit == 3:
        print(f"{digit}rd")
    elif digit > 3:
        print(f"{digit}th")

