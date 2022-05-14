squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

squares1 = []
for value in range(1,11):
    squares1.append(value**2)
print(squares1)

print(min(squares))
print(max(squares))


squares2 = []
#Генератор
squares2 = [value**2 for value in range(1, 11)]
print(squares2)