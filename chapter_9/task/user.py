class User():
    #Класс для всех пользователей
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