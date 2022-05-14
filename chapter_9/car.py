class Car():
    """Классы для представления машин с бензиновым и электродвигателем."""

    def __init__(self, make, model, year):
        #Инициируем атрибуты машины
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        #отформатированное описание
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        #Вывод пробега машины в милях
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Установка заданного значения одометра.
        При попытке обратной прокрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")

    def increment_odometer(self, miles):
        # Увеличение показания одометра с заданным приращением
        self.odometer_reading += miles

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
"""
my_new_car = Car('Audi', 'A4', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(21_000)
my_new_car.read_odometer()

my_new_car.increment_odometer(4_000)
my_new_car.read_odometer()
"""

