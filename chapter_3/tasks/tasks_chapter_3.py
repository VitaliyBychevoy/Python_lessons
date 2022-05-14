print("\n\t3.1. Имена.")
name = ['Андрей', 'Алексей', 'Евгений', 'Максим']
print(name[0])
print(name[1])
print(name[2])
print(name[3])


print("\n\t3.2. Cообщения.")
print(f"Привет, {name[0]}!")
print(f"Привет, {name[1]}!")
print(f"Привет, {name[2]}!")
print(f"Привет, {name[3]}!")


print("\n\t3.3. Собственный список.")
car = ["BMW", "AUDI", "Lexus"]
print(f"Я бы хотел купить себе {car[0]}.")
print(f"Я бы хотел купить себе {car[1]}.")
print(f"Я бы хотел купить себе {car[2]}.")


print("\n\t3.4 Список гостей.")
guests = ["Шрек", "Фиона", "Осел", "Пипокио", "Чебурашка", "Крокодил Гена", "Незнайка"]
print(f"{guests[0]}, приглашаем вас на обед.")
print(f"{guests[1]}, приглашаем вас на обед.")
print(f"{guests[2]}, приглашаем вас на обед.")
print(f"{guests[3]}, приглашаем вас на обед.")
print(f"{guests[4]}, приглашаем вас на обед.")
print(f"{guests[5]}, приглашаем вас на обед.")
print(f"{guests[6]}, приглашаем вас на обед.")


print("\n\t3.5 Изменение списка гостей.")
print(f"К сожалению {guests[3]}, не сможет прийти.")
guests[3] = "Чепалино"
print(f"{guests[0]}, приглашаем вас на обед.")
print(f"{guests[1]}, приглашаем вас на обед.")
print(f"{guests[2]}, приглашаем вас на обед.")
print(f"{guests[3]}, приглашаем вас на обед.")
print(f"{guests[4]}, приглашаем вас на обед.")
print(f"{guests[5]}, приглашаем вас на обед.")
print(f"{guests[6]}, приглашаем вас на обед.")


print("\n\t3.6 Больше гостей.")
print("Мы расширяем список гостей на три персоны.")
guests.insert(0, "Робин Гуд")
guests.insert(4, "Петрик")
guests.append("Карлсон")
print(f"{guests[0]}, приглашаем вас на обед.")
print(f"{guests[1]}, приглашаем вас на обед.")
print(f"{guests[2]}, приглашаем вас на обед.")
print(f"{guests[3]}, приглашаем вас на обед.")
print(f"{guests[4]}, приглашаем вас на обед.")
print(f"{guests[5]}, приглашаем вас на обед.")
print(f"{guests[6]}, приглашаем вас на обед.")
print(f"{guests[7]}, приглашаем вас на обед.")
print(f"{guests[8]}, приглашаем вас на обед.")
print(f"{guests[9]}, приглашаем вас на обед.")


print("\n\t3.7 На обед приглашаются всего два гостя.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests.pop()}, к сожалению вынуждены отменить ваше приглашение на обед.")
print(f"{guests[0]}, приглашаем вас на обед.")
print(f"{guests[1]}, приглашаем вас на обед.")
del guests[1]
del guests[0]
print(guests)


print("\n\t3.8. Повидать мир.")
country = ["Новая Зеландия", "Швейария", "Япония", "Куба", "Израиль"]
print(country)
print(sorted(country))
print(country)
print(sorted(country, reverse=True))
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
country.sort(reverse=True)
print(country)


print("\n\t3.9. Количество гостей.")
guests = ["Шрек", "Фиона", "Осел", "Пипокио", "Чебурашка", "Крокодил Гена", "Незнайка"]
print(guests)
print(f"Число гостей {len(guests)}.")


print("\n\t3.10. Все функции.")
city_ukraine = [
    'Киев',
    'Харьков',
    'Одесса',
    'Закарпаття',
    'Николаев',
    'Краматорск'
]
print(city_ukraine)
print("\nИзменение списка.")
city_ukraine[3] = "Львов"
print(city_ukraine)


print("\nДобавление элемента в конец списка.")
city_ukraine.append("Чернигов")
print(city_ukraine)


print("\nДобавление элемента в указанное место в списке insert()")
city_ukraine.insert(5, "Суммы")
print(city_ukraine)


print("\nУдаление города по индексу")
del city_ukraine[2]
print(city_ukraine)


print("\nУдаление города по индексу с сохранением удаленного элемента в другой переменной.")
city = city_ukraine.pop(5)
print(city_ukraine)
print(f"Удаленный город {city}.")


print("\nУдаление города по названию города (по значению в списке)")
city_ukraine.remove("Николаев")
print(city_ukraine)


print("\nСортировка в обратном порядке методом reverse()")
print("Исходный список")
print(city_ukraine)
print("Обратный порядок исходного списка")
city_ukraine.reverse()
print(city_ukraine)

print("\nСортировка в алфавитном порядке методом sort()")
city_ukraine.sort()
print(city_ukraine)

print("\nСортировка в порядке обратном алфавитному методом sort()")
city_ukraine.sort(reverse=True)
print(city_ukraine)

print("\nСортировка (не изменяемая) в алфавитном порядке методом sorted()")
сity_of_ukraine = [
    'Киев',
    'Харьков',
    'Одесса',
    'Закарпаття',
    'Николаев',
    'Краматорск'
]
print("Исходный список")
print(сity_of_ukraine)
print("Отсортированный список")
print(sorted(сity_of_ukraine))
print("Исходный список")
print(сity_of_ukraine)

print("\nСортировка (не изменяемая) в порядке обратом алфавитному методом sorted()")
сity_of_ukraine = [
    'Киев',
    'Харьков',
    'Одесса',
    'Закарпаття',
    'Николаев',
    'Краматорск'
]
print("Исходный список")
print(сity_of_ukraine)
print("Отсортированный список")
print(sorted(сity_of_ukraine, reverse=True))
print("Исходный список")
print(сity_of_ukraine)