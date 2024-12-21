# Junio, Meynard Brian Y.
# BSIT - 2A

from abc import ABC, abstractmethod
class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass
    
class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")
    
class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")
        
class Healer(GameCharacter): # Bonus +5
    def attack(self):
        print("Casts healing spell on ally!")
        
char1 = Warrior()
char2 = Mage()
char3 = Archer()
char4 = Healer()

char1.attack()
char2.attack()
char3.attack()
char4.attack()
