digit = [2, "rty", 56]
print(digit)

numbers = [2,"r", 56]
print(numbers)

for item in digit:
    print(str(item), id(item))

for item in numbers:
    print(str(item), id(item))


