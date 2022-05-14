magicians = ['alice', 'david', 'carolina']

#Вывод каждого элемента в отдельной строке
for magician in magicians:
    print(magician)


#Вывод каждого элемента в отдельной строке с заглавной буквой
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see you next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show.")