# Junio, Meynard Brian Y.
# BSIT - 2A

class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return "Brand of a car"

car_ko = Car("Mitsubishi")
print(car_ko)
del car_ko
print(car_ko)