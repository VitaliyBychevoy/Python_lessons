my_food = ['pizza', 'falafel', 'carrot cake']
#Копирование списка
friend_food = my_food[:]


"""
print("ID my_food is ", id(my_food))
for my_f in my_food:
    print(f"id {my_f} is ", id(my_f))
print("\n")
print("ID friend_food is ", id(friend_food))
for fr_f in friend_food:
    print(f"id {fr_f} is ", id(fr_f) )
"""
my_food.append("cannoli")
friend_food.append("ice cream")


print("My favorite foods are:")
print(my_food)
for item in my_food:
    print(item)

print("\nMy friend's favorite foods are:")
print(friend_food)
for food in friend_food:
    print(food)

friend_food = my_food
print("friend_food ", friend_food, id(friend_food))
print("my_food ", my_food, id(my_food))

