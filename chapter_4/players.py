players = ['charles', 'martina', 'michael', 'eli']
i  = 0
z = 0

for player in players:
    z = i - len(players)
    print(player + " has index ", i, ".Inverse index ", z)
    i += 1



#Начало диапазона указанный 0-й элемент исх. сп.: последний элемен диапазона  3-1 исх. сп.
print(players[0:3])

#Начало диапазона указанный 1-й элемент исх. сп.:последний элемент диапазона 4-1 элемент исх. сп.
print(players[1:4])

#Начало диапазона неуказанный элемент (по умолчанию 0-й элемент исх. сп.):последний элемент диапазона 4-1 элемент исх. сп.
print(players[:4])


#Начало диапазона указанный 2-й элемент исх. сп.:последний элемент диапазона неуказанный (по умолчанию последний элемент исх. сп.)
print(players[2:])


#Начало диапазона 3-й элемент с конца исх.сп :последний элемент диапазона неуказанный (по умолчанию последний элемент исх. сп.)
print(players[-3:])

#Перебор в обрезанном диапазоне
print("Here is my the first three player on my team:")
for player in players[:3]:
    print(player.title())


