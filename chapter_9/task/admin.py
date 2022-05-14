from users import  User

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