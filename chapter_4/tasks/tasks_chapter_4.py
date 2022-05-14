print('\n\t4.1. Пицца.')
pizzas = ['Гавайская', 'Карбонара', 'Шахтерская']
for pizza in pizzas:
    print(f"Моя любимая пицца {pizza}.")
print("Я очень люблю пиццу.")


print("\n\t4.2. Животные.")
animals = ['Папугай', "Канарейка", "Ворона", "Воробей"]
for animal in animals:
    print(f"{animal} умеет летать.")
print("Я люблю птиц.")


print("\n\t4.3. Считаем до 20.")
my_list = [value for value in range(1,21)]
for item in my_list:
    print(item)
for val in range(1,21):
    print(val)


print("\n\t4.4. Миллион.")
"""
m = list(range(1, 1000001))
for i in m:
    print(i)
"""

print("\n\t4.5. Суммирование миллиона чисел.")
mil = list(range(1, 1000001))
print(min(mil))
print(max(mil))
print(sum(mil))


print("\n\t4.6. Нечетные числа.")
#odd_numbers = [number for number in range(1,21,2)]
odd_numbers = list(range(1, 21, 2))
for num in odd_numbers:
    print(num)


print("\n\t4.7. Тройки.")
three_list = list(range(3,31,3))
for i in three_list:
    print(i)


print("\n\t4.8. Кубы")
cubes = []

for item in range(1,11):
    cubes.append(item**3)

for item in cubes:
    print(item)


print("\n\t 4.9.Генератор кубов.")
cube_list =  [value**3 for value in range(1,11)]
for number in cube_list:
    print(number)

print("\n\t 4.10. Сегменты")
my_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', "brauning", "salat"]


print("The first three items in list are:")
for item in my_food[:3]:
    print(item)

print("The items from the middle of the list are:")
start = int(len(my_food) / 2)
finish = start + 3
for item in my_food[start:finish]:
    print(item)

print("The last three items in the list are:")
for item in my_food[-3:]:
    print(item)


print("\n\t 4.11. Моя пицца, твоя пицца.")
friend_pizzas = pizzas[:]
pizzas.append("Баварская")
friend_pizzas.append("4 сыра")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)


print("\n\t 4.13.Шведский стол.")
dishes = ("Пюре", "Катлета по-киевски", "Салат цезарь", "Жульен", "Узвар")
print("Старый список блюд:")
for dish in dishes:
    print(dish)


dishes = ("Пюре", "Катлета по-киевски", "Оливье", "Жульен", "Квас")
print("\nНовый список блюд:")
for dish in dishes:
    print(dish)