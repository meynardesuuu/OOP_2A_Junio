# Junio, Meynard Brian Y.
# BSIT - 2A

class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Bark!")

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Meow!")

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Chirp!")
        
class Fish: # +5 Bonus
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(...)
        
dog = Dog("Aspin")
cat = Cat("Persian")
bird = Bird("Parrot")
fish = Fish("Goldfish")

def animal_sounds(animal):
    animal.speak()
    
for animal in [dog, cat, bird, fish]:
    animal_sounds(animal)
    