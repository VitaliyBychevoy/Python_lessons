from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

#Создание кубика
die = Die()

"""Моделирование серии бросков с сохранением результатов в списке."""
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


#Анализ результатов.
frequencies = []
for value in range(1, die.num_sides + 1): #перечисляем 6 вариантов кубика
    frequency = results.count(value)  #количество каждого варианта
    frequencies.append(frequency)

print(frequencies)

# Визулизация результатов
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequencies of Result'}
my_layout = Layout(title="Result of rolling one D6 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
