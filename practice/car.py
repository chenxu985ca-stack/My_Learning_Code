# ----------------------------

class Cars:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odmeter = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odmeter(self):
        print(f"This car has {self.odmeter} km on it")

    def update_odmeter(self, mileage):
        self.odmeter = mileage


# my_car = Cars('audi', 'rs7', '2022')

# print(my_car.get_descriptive_name())
# my_car.update_odmeter(20000)
# my_car.read_odmeter()

# -------组合-------------------------


class Battery:
    def __init__(self, battery_size=65):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 200
        print(F"This car has {range}km on a full charge")

# -------继承-------------------------


class ElectricCars(Cars):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has {self.battery_size}km on it")


# my_leaf = ElectricCars('nissan', 'leaf', 2024)

# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
