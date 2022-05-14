bicycles = ['trek','cannondale', 'redline', 'specialized']
print(bicycles)


#Обращение к элеметам списка
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1].upper())
print(bicycles[3].capitalize())

#Последний элемент списка указывается с индекса -1
print(bicycles[-1])


message = f"My first bicycle was a {bicycles[0].title()}."
print(message)