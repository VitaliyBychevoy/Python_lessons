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