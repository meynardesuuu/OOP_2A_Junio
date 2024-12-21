# Junio, Meynard Brian Y.
# BSIT - 2A

class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating!")
    def info(self): # Bonus
        print(f"Brand: {self.brand}, Model: {self.model}")
        
class WashingMachine(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Washing clothes!")
        
class Refrigerator(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Keeping food cold!")
        
class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Heating food!")
        
washmach = WashingMachine("LG", "Wash Tower Washing Machine")
ref = Refrigerator("Samsung", "Two-Door Digital Inverter Refrigerator")
micro = Microwave("Hanabishi", "Digital Microwave Model")

for app in [washmach, ref, micro]:
    app.operate()
    app.info()
    
    