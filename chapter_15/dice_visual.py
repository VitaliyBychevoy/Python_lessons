from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

#Создание двух кубиков D6
die_1 = Die(6)
die_2 = Die(6)


"""Моделирование серии бросков с сохранением результатов в списке."""
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)


#Анализ результатов.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result + 1): #перечисляем 6 вариантов кубика
    frequency = results.count(value)  #количество каждого варианта
    frequencies.append(frequency)

print(frequencies)

# Визулизация результатов
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequencies of Result'}
my_layout = Layout(title="Result of rolling two D6 dice times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_times.html')
