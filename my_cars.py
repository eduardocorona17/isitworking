from carrss import Car, ElectricCar

my_i4 = ElectricCar('BMW', 'i4', '2023')
my_i7 = Car('BMW', 'i7', 2023)
print(my_i4.get_descriptive_name())
print(my_i7.get_descriptive_name())
my_i4.battery.upgrade_method()
my_i4.battery.get_range()