class Dog():
    #Простая модль собаки

    def __init__(self, name, age):
        """Инициализируем атрибуты name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """собака садится по команде"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """собака перекатывается по команде."""
        print(f"{self.name} rolled over!")


my_dog = Dog("Shrick", 23)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")