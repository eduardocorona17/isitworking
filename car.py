class Car:
    """A simpple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.special = ''

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    # FIX THIS DEF BELOW
    def is_amg(self, special):
        """Tells if it is an AMG or not"""
        if special == 'AMG':
            special == self.special
            print(f"This {self.make} is an AMG")
        else:
            print(f"This {self.make} is not an AMG")    



    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")
            

my_new_car = Car('audi', 'r8', 2023)
amg = Car('Benz', 'CLA',2023)
print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(25)
my_new_car.read_odometer()
amg.is_amg('CLS')