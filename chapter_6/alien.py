alien_0 = {"color": 'green', 'points': 5, }

#print(alien_0['color'])
#print(alien_0['points'])


#new_points = alien_0['points']
#print(f'You just earned {new_points} points!')


#print(alien_0)

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)


alien_1 = {'color': 'green'}
print(f'The alien is {alien_1["color"]}')

alien_1['color'] = 'yellow'
print(f"The alien is now {alien_1['color']}.")

alien_2 = {'x_position': 0, 'y_position': 25, "speed": 'medium'}
print(f'Original position: {alien_2["x_position"]}')

#Пришелец перемещается вправо.
#Вычисляем величину смещения на основании текущей скорости
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец о двигается быстро.
    x_increment = 3


#Новая позиция равна сумме старой позиции и приращения
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")

alien_3 = {"color": "green", "points": 5,}
print(alien_3)

del alien_3["points"]
print(alien_3)

print("\n")

alien_0 = {'color': 'green', 'points': 5, }
alien_1 = {'color': 'yellow', 'points': 10, }
alien_2 = {'color': "red", 'points': 15, }

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n")

#Список для хранения пришельцев
aliens = []

#Создаём 30 зеленыйх пришельцев
for alien_number in range(30):
    new_alien = {"color": 'green', "points": 5, 'speed': 'slow'}
    aliens.append(new_alien)
"""
#Меняем цвет первых 3-х пришельцев
for alien in aliens[0:2]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
"""


#Вывод первых 5 пришельцев.
for alien_number in aliens[:5]:
    print(alien)
print("...")

#Вывод количества созданных пришельцев
print(f"Total number of aliens: {len(aliens)}")

