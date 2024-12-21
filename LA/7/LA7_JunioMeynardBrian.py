# Junio, Meynard Brian Y.
# BSIT - 2A

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
car1 = Car("Toyota", "Red")
car2 = Car("Nissan", "Brown")

print(f"1. Brand: {car1.brand} Color: {car1.color}")
print(f"2. Brand: {car2.brand} Color: {car2.color}")

car1.color = "Black"

print(f"1. Brand: {car1.brand} Color: {car1.color}")
print(f"2. Brand: {car2.brand} Color: {car2.color}")
