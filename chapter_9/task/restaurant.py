class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        #инициируем атрибуты класса
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        #Описание атрибутов
        print(f"Restaurant name is {self.restaurant_name}. {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        #Сообщение, что ресторан открыт
        print(f"Restaurant {self.restaurant_name} is open.")