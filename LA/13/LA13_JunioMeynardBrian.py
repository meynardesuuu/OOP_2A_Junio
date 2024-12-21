# Junio, Meynard Brian Y.
# BSIT - 2A

class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def describeAnimal(self):
        print(f"Name: {self.name}\nType: {self.type}\nCan Swim?: {self.can_swim}")
        
class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim

exFish = Fish("Tilapia", "Fish", True)
exFish.describeAnimal()
