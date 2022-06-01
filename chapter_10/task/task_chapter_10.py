"""
print("\n\t 10.1 Изучение Python.")

with open("learning_python.txt") as file_object:
    text = file_object.read()
    print(text)
    print("\n")


with open("learning_python.txt") as file_object_1:
    for line in file_object_1:
        print(line.rstrip())
print("\n")


with open("learning_python.txt") as file_object_2:
    lines = file_object_2.readlines()

for line in lines:
    print(line.rstrip())
"""
"""
print("\n\t 10.2 Изучение C:")
with open("learning_python.txt") as file_obj:
    lines = file_obj.readlines()

for line in lines:

    print(line.rstrip().replace("Python", "C"))
"""
"""
file_location = 'guest.txt'

print("\n\t 10.3 Гость.")

first_name = input("Enter your name:\n")
last_name = input("Enter last name:\n")
with open(file_location, "w") as file_object:
    file_object.write(f"{first_name}  {last_name}")
"""
"""
print("\n\t 10.4 Гостевая книга")
file_name = 'guest_book.txt'
with open(file_name, 'w') as file_object:

    while True:
        last_name = input('Hello.Enter your name.If you want exit press "q".\n')
        if last_name == 'q':
            break
        else :
            last_name += "\n"
            print(f"Hello {last_name}")
            file_object.write(last_name)
"""

"""
print("\n\t 10.5 Опрос.")

file_name = 'poll.txt'
message = ""
with open(file_name, 'w') as file_object:

    while True:
        name = input("Enter name.(For exit press 'q'.)\n")

        if name == 'q':
            break
        else:
            answer = input("Why do you like programming?(For exit press 'q'.)\n")
            if answer == 'q':
                break
            else:
                file_object.write(f"{name.title()} likes programming because {answer.lower()}.\n")
"""

"""
print("\n\t 10.6 Сложение.")
try:
    first_number = int(input("Введите первое число:\n"))
    second_number = int(input("Введите второе число:\n"))
except ValueError:
    print("You enter symbol instead number.")
else:
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
"""
"""
print("\n\t 10.7 Калькулятор")
while True:
    try:
        first_number = int(input("Введите первое число:\n"))
        second_number = int(input("Введите второе число:\n"))
    except ValueError:
        print("You enter symbol instead number.")
    else:
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
"""
"""
print("\n\t 10.8 Кошки и собаки")

filename = ['cats.txt', 'dogs.txt']

for file in filename:
    try:
        with open(file, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry file {file} does not exist.")
    else:
        print(content)
        print("***\n")
"""

"""
print("\n\t 10.9 Ошибки без уведомления.")

filename = ['cats.txt', 'dogs.txt']

for file in filename:
    try:
        with open(file, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
        print("***\n")
"""

"""
print("\n\t 10.10 Частые слова.")

filename = "Alice.txt"

word = "the "
word_counter = 0
with open(filename, encoding='utf-8') as f:
    lane = f.read()
    word_counter += lane.lower().count(word)

print(f'In file {filename} is {word_counter} words "{word}".')
"""


