
class Car:                      #public class that can be access by everyone
    number_of_wheel = 4
    _color = "Black"
    __fav_brand = "Audi"
                   
class buy_car(Car):           #protected class contains base class and derived class
    def __init__(self):
        print("buy any car of your choice:", self._color)

car = Car()
print("public no of attribute:", car.number_of_wheel)
Buy_car = buy_car()
print("private your fav car is : ", car._Car__fav_brand)
