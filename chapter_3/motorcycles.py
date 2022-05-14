print("\tИсходный список.")
motorcycles = ["honda", "yamaha", 'suzuki']
print(motorcycles)


#Изменение элемента
print("\n\tИзменение элемента по номеру в списке.")
motorcycles[0] = 'ducati'
print(motorcycles)


#Добавление элемента
print("\n\tДобавление элемента в конец списка методом append(значение).")
motorcycles.append('МТ')
print(motorcycles)


#Вставка элемента
print("\n\tВставка элемента по указанному номеру списка методом insert(номер, значение).")
motorcycles.insert(0,'Kawasaki')
print(motorcycles)


#Удаление элемента
print("\n\t Удаление элемента по номеру в списке методом del имя_списка[номер].")
print("Удаляем первый элемент (имя_списка[0])")
del motorcycles[0]
print(motorcycles)
print("Удаляем третий элемент (имя_списка[2])")
del motorcycles[2]
print(motorcycles)


#Удаленного последнего элемента и запись этого элемента в отдельную переменную
print("\n\tУдаленного последнего элемента и запись этого элемента в отдельную переменную.")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"Переменная с удаленный элементом popped_motorcycle = {popped_motorcycle}")


#Удаление элемента по значениею
print("\n\tУдаление элемента по значениею.")
print("Исходный список.")
motorcycles = ["honda", "yamaha", 'suzuki', 'ducati']
print(motorcycles)
print("Удаляем элемент 'ducati'.")
motorcycles.remove('ducati')
print(motorcycles)

#Удаление элемента по переменной
print("\n\tУдаление элемента по переменной.")
print("Исходный список.")
motorcycles = ["honda", "yamaha", 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
print(f"id переменной too_expensive = {too_expensive}, id = {id(too_expensive)} ")
print(f"id последнего элемента списка  motorcycles[3] = {motorcycles[3]}, id = {id(motorcycles[3])}")
print("\nУдалили методом список.remove(too_expensive)")
motorcycles.remove(too_expensive)
print(motorcycles)