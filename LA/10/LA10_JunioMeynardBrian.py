# Junio, Meynard Brian Y.
# BSIT - 2A

class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        
    def describeVehicle(self):
        print(f"{self.brand} {self.model} uses a fuel type of {self.fuel_type}")
        
class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

sampleCar = Car("Tesla", "Model 3", "Electric")
sampleMotor = Motorcycle("Honda", "Click", "Gasoline")    
sampleCar.describeVehicle()
sampleMotor.describeVehicle()    
        