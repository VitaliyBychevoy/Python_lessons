import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

"""subplots() - позволяет сгенерировать одну или несколько поддиаграмм
на одной диаграмме.
fig - весь рисунок 
ax - представляет одну диаграмму"""
plt.style.use('seaborn')
fig, ax = plt.subplots()


"""plot() -  строит графическое представление"""
ax.plot(input_values, squares, linewidth=3)

#назначение заголовка диаграммы и меток осей.
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=24)

#Назначение размера шрифта, делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()


