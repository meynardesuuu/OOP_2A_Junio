# Junio, Meynard Brian Y.
# BSIT - 2A
# OE #1

class mlhero():
    def __init__(self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        
    def description(self):
        print(f"{self.name} is a {self.role} with a damage type of {self.dmg_type}")
    
    def __str__(self):
        return f'''OBJECT DETAILS:
CHARACTER_NAME: {self.name}
CHARACTER_ROLE: {self.role}
CHARACTER_DMGTYPE: {self.dmg_type}'''

hero1 = mlhero("Irithel", "marksman", "physical damage")
hero2 = mlhero("Fanny", "assassin", "physical damage")
hero3 = mlhero("Rafaela", "support", "magic damage")
hero4 = mlhero("Cecilion", "mage", "magic damage")
hero5 = mlhero("Tigreal", "tank", "physical damage")

hero1.description()
hero2.description()
hero3.description()
hero4.description()
hero5.description()
print(hero1)