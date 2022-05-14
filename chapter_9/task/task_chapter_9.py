"""
print("\n\t 9.1 Ресторан")
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}. {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("Restaurant is open.")

restaurant = Restaurant('Cherry','Belarus')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n\t 9.2 Три ресторана")

rest_1 = Restaurant('Shavuha', 'Uzbekistan')
rest_2 = Restaurant('Dacha', 'Moldovs')
rest_3 = Restaurant('Ikar', 'Greece')


rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()

"""
"""
print("\n\t 9.3 Пользователи")
class User():

    def __init__(self, first_name, last_name, age):
        #Инициируем атрибуты first_name и last_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def describe_user(self):
        #вывод описания пользователя
        print(f"User name : {self.first_name}.")
        print(f"User last name: {self.last_name}.")
        print(f"Age {self.age}")

    def greet_user(self):
        #Приветствие пользователя
        print(f"Hello, {self.first_name}!!!")


user_1 = User('Alibaba', "Faris", 42)
user_2 = User('Kurt', "Olsen", 52)
user_3 = User('Goggi', "Rumatsvilli", 52)


user_1.describe_user()
"""

"""
print("\n\t 9.4 Посетители.")

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}. {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open.")

    def set_number_served(self, number):
        #количество обслуженных постителей
        self.number_served = number

    def increment_number_served(self, number):
        #увеличиваем число обслуживаемых посетителей
        self.number_served += number

restaurant = Restaurant('Fast',"USA")
print(f"Number saved {restaurant.number_served}")

restaurant.number_served = 12
print(f"Number saved {restaurant.number_served}")

restaurant.set_number_served(37)
print(f"Number saved {restaurant.number_served}")


restaurant.increment_number_served(25)
print(f"Number saved {restaurant.number_served}")

"""

"""
print("\n\t 9.5 Попытка входа:")

class User():

    def __init__(self, first_name, last_name, age):
        #Инициируем атрибуты first_name и last_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.login_attempts = 0

    def describe_user(self):
        #вывод описания пользователя
        print(f"User name : {self.first_name}.")
        print(f"User last name: {self.last_name}.")
        print(f"Age {self.age}")

    def greet_user(self):
        # Приветствие пользователя
        print(f"Hello, {self.first_name}!!!")

    def increment_login_attempts(self):
        # увеличиваем количество попыток залогигться на 1
        self.login_attempts += 1

    def reset_login_attempts(self):
        # обнуляется число попыток
        self.login_attempts = 0



user_1 = User('Паша', 'Иванов', 24)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(user_1.login_attempts)

user_1.reset_login_attempts()

print(user_1.login_attempts)
"""

"""
print("\n\t 9.6 Киоск с мороженым.")
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}. {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("Restaurant is open.")


class IceCreamStand(Restaurant):
    #Cтенд с мороженым

    def __init__(self, restaurant_name, cuisine_type):
        #инициализация атрибутов родителя родителя
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['banana', 'cherry', 'milk']

    def print_flavors(self):
        for flavor in self.flavors:
            print(f"We have {flavor} flavor ")


icecream = IceCreamStand("Salit" ,"France" )
icecream.print_flavors()

"""

"""
print("\n\t 9.7 Администратор")
class User():

    def __init__(self, first_name, last_name, age):
        #Инициируем атрибуты first_name и last_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def describe_user(self):
        #вывод описания пользователя
        print(f"User name : {self.first_name}.")
        print(f"User last name: {self.last_name}.")
        print(f"Age {self.age}")

    def greet_user(self):
        #Приветствие пользователя
        print(f"Hello, {self.first_name}!!!")

class Administrator(User):
    #Класс администратора

    def __init__(self, first_name, last_name, age):
        #инициализация атрибутов родителя 
        super().__init__(first_name, last_name, age)
        self.privileges = ['разрешено добавлять сообщения',
                           'разрешено удалять пользователя',
                           'разрешено банить пользователей']

    def show_privileges(self):
        #Вывод набора привелегий
        for priv in self.privileges:
            print(f"Администратору {priv}.")

admin_1 = Administrator('Иван', 'Петров', 26)
admin_1.greet_user()

admin_1.show_privileges()
"""

"""
print("\n\t 9.8 Привилегии")
class User():

    def __init__(self, first_name, last_name, age):
        #Инициируем атрибуты first_name и last_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def describe_user(self):
        #вывод описания пользователя
        print(f"User name : {self.first_name}.")
        print(f"User last name: {self.last_name}.")
        print(f"Age {self.age}")

    def greet_user(self):
        #Приветствие пользователя
        print(f"Hello, {self.first_name}!!!")

class Administrator(User):
    #Класс администратора

    def __init__(self, first_name, last_name, age):
        #инициализация атрибутов родителя
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

class Privileges():
    #Класс привелегий
    def __init__(self):
        self.privileges = [
                            'разрешено добавлять сообщения',
                            'разрешено удалять пользователя',
                           'разрешено банить пользователей'
                            ]

    def show_privileges(self):
        #Вывод набора привелегий
        for priv in self.privileges:
            print(f"Администратору {priv}.")

admim_2 = Administrator('Семён', 'Сидоров', 35)
admim_2.privileges.show_privileges()
"""
"""
print("\n\t 9.9 Обновление аккумулятора")
"""

""""""
print("\n\t 9.10 Импортирование класса Restaurant")
