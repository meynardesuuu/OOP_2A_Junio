# Junio, Meynard Brian Y.
# BSIT - 2A

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} damaged {target.name} health (-{self.attack_power})")
        if target.health <= 0:
            print(f"{target.name}'s Health: {target.health}")
            print(f"{self.name} won!")
        else:
            print(f"{target.name}'s Health: {target.health}")
        
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} has been healed by {amount} points")
        print(f"{self.name}'s Health: {self.health}")
        
        
p1 = Player("Yudi", 500, 50)
p2 = Player("Myx", 800, 100)

p2.attack(p1)
p1.heal(100)
p2.attack(p1)
p1.attack(p2)
p2.attack(p1)
p1.attack(p2)
p2.attack(p1)
p1.attack(p2)
p2.attack(p1)
p1.attack(p2)
p2.attack(p1)
