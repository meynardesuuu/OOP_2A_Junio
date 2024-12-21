# Junio, Meynard Brian Y.
# BSIT - 2A

class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def toyDeets(self):
        print(f"{self.name} retails for P{self.price}")
        
class Doll(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
        
toyEx = Doll("Barbie", 170)
toyEx.toyDeets()