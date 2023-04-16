class Car:
    """A simple attempt to represent a car."""
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
    
    def is_amg(self, special):
        """Tells if it is an AMG or not"""
        if special == 'AMG':
            special = self.special
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

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt at describing an electric vehicles battery."""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range a battery gets."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_method(self):
        """Upgrades battery size if less than 100."""
        if self.battery_size < 100:
            print(f"Battery size will be upgraded to be 100-kHw.")
            self.battery_size = 100
    def new_battery(self):
        print(f"Battery size upgraded to {self.battery_size}-kWh.")
            


class ElectricCar(Car):
    """Represents the aspects specific to an Electric car."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()