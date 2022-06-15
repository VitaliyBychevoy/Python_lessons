import matplotlib.pyplot as plt

from chapter_15.random_walk import RandomWalk

"""
print('\n\t 15.1 Кубы\n\t 15.2 Цветные кубы')

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

#ax.plot(x_values, y_values, linewidth=6)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.brg, s=10)

#назначение заголовка диаграммы и меток осей.
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=24)


ax.axis([0, 6000, 0, 130000000000])
plt.show()
"""

"""
print('\n\t 15.3 Молекулярное движение')

while True:
    
    #Построение случайного блуждания
    rw = RandomWalk()
    rw.fill_walk()

    #Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 7), dpi=96)
    point_number = range(rw.num_points)


    #ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues,
               #edgecolors='none', s=1)
    ax.plot(rw.x_values, rw.y_values, linewidth=2)

    #Выделение первой и последней точек
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)

    #Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()

    keep_running = input("Make another walk? (y, n): ")
    if keep_running == 'n':
        break
"""
