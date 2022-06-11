import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c='red', s=10)
#ax.scatter(x_values, y_values, c=(0.7, 0.4, 0.8), s=10)  #c=(Red, Green, Blue)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.jet, s=10)

#назначение заголовка диаграммы и меток осей.
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=24)

#Назначение размера шрифта, делений на осях
#ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000])
#plt.show()
plt.savefig('square_plot_2.png', bbox_inches='tight')
