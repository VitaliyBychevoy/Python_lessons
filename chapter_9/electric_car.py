from car import Car

class Battery():
    """Простая модель батареи"""
    def __init__(self,battery_size = 75):
        """Инициализируем атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Вывод характеристики батареи"""
        print(f"This car has a {self.battery_size} - kWh battery." )

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    #Представляет аспекты машины, специфические для электромобилей.

    def __init__(self, make, model, year):
        #инициализируем атрибуты класса-родителя
        super().__init__(make, model, year)
        self.battery = Battery()