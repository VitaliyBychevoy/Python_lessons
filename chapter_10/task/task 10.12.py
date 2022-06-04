import json

print('\n\t 10.12 Сохранённое любимое число.')


file_name_number = 'my_favorite_number.json'

with open(file_name_number) as f:

    try:
        num = json.load(f)
    except json.JSONDecodeError:
        print("Фаил пуст или имеет некорректную структуру")
        with open(file_name_number, 'w') as g:
            number = input("Введите ваше любимое число:\n")
            json.dump(number, g)
    else:
        print(f"Я знаю ваше любимое число - {num}")


def empty_list_json_file(file):
    with open(file, 'w') as f:
        empty = []
        json.dump(empty, f)

#empty_list_json_file(file_name_number)