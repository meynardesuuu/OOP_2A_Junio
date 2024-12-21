# Junio, Meynard Brian Y.
# BSIT - 2A

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.resetPower = power
        
    def attack(self, target):
        target.health -= self.power
        print(f"{target.name} got attacked by {self.name} (-{self.power})")
        print(f"{target.name}'s Remaining Health: {target.health}")
        self.power = self.resetPower
        
    def defend(self, attacker):
        damageTaken = attacker.power / 2
        self.health = self.health + damageTaken
        print(f"{self.name} defended him/herself, the damage is reduced! (-{damageTaken})")
        print(f"{self.name}'s Remaining Health: {self.health}")
        
    def special_move(self):
        pass
    
class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        
    def special_move(self, target):
        powerUp = self.power * 2
        self.power = powerUp
        print("Warrior uses Shield Bash!")
        print(f"{self.name}'s power is now doubled! (+{self.power})")

class Mage(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        
    def special_move(self, target):
        target.health -= 100
        print(f"Mage ({self.name}) casts Fireball! (-100)")
        print(f"{target.name}'s Remaining Health: {target.health}")

class Archer(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        
    def special_move(self, target):
        target.health -= self.power * 2.5
        print(f"Archer ({self.name}) shoots a Piercing Arrow! (-{self.power * 2.5})")
        print(f"{target.name}'s Remaining Health: {target.health}")
        
class Monster(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        
    def special_move(self, target):
        self.health += 50
        print(f"Monster ({self.name}) roars and gains extra health! (+50)")
        print(f"{self.name}'s Remaining Health: {self.health}")
        
warrior = Warrior("Warrior", 500, 50)
mage = Mage("Mage", 550, 35)
archer = Archer("Archer", 600, 65)
monster = Monster("Monster", 800, 85)
charList = [warrior, mage, archer, monster]

def battleRound():
    # Each character attacks and uses special_move to the monster
    for perChar in range(0, 3):
        charList[perChar].special_move(monster)
    for perChar in range(0, 3):  
        charList[perChar].attack(monster)
    warrior.attack(mage)
    print("==========")
    # Monster retaliates by attacking back 
    for perChar in range(1, 4):
        monster.special_move(charList[perChar])
        monster.attack(charList[perChar])
    print("==========")
    # Demonstrate polymorphism
    for perChar in charList:
        perChar.special_move(monster)
    print("==========")
        
battleRound()

