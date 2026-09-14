# 将类作为参数传递的方式
class CarColor:
    color = None


def chage_color(car, color):
    car.color = color


car_1 = CarColor()

chage_color(car_1, "red")
print(car_1.color)
