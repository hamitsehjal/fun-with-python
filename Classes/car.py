class Battery:
    def __init__(self):
        self.battery_size=40

    def describe_battery(self):
        print(f"The Battery size is {self.battery_size}")

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def fill_gas_tank(self,quantity):
        print(f"filling the tank with {quantity} litres")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

## child class
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def describe_battery(self):
        print(f"{self.make} {self.model} {self.year} has a battery size of {self.battery.battery_size}")
    
    def fill_gas_tank(self):
        print("Electric vehicles don't need gas tanks")
my_leaf=ElectricCar('Nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
