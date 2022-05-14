from car import Car

my_new_car = Car("ZAZ", 'Slavuta', 1997)
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading = 41
my_new_car.read_odometer()


