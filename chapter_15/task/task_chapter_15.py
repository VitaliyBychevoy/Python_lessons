import matplotlib.pyplot as plt

""""""
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