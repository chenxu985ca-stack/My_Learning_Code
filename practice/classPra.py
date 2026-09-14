class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} is rolling")


my_dog = Dog('旺财', 3)

print(my_dog.name)
print(my_dog.age)
my_dog.roll_over()
my_dog.sit()

# ----------------------------


class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(
            F"My restaurant is {self.name} restaurant, We cook {self.type} food")

    def open_restaurant(self):
        print(f"Our {self.name} is openning!!")


my_restaurant = Restaurant("long", "china")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


# ---------链式调用------------
class Car:

    def turn_on(self):
        print("car is turn on now")
        return self

    def drive(self):
        print("car is driving now")
        return self

    def brake(self):
        print("car is brake now")
        return self

    def turn_off(self):
        print("car is turn off now")
        return self


car = Car()

car.turn_on().drive().brake().turn_off()
