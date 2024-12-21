class hero():
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
        
    def describe(self):
        return f"{self.name} is a {self.role} with a damage type of {self.dmg_type}"
    
hero_mm = hero("Irithel", "marksman", "physical damage", 2300,125)
hero_assas = hero("Fanny", "assassin", "physical damage", 2426, 126)
hero_support = hero("Rafaela", "support", "magic damage", 2441, 117)
hero_mage = hero("Cecilion", "mage", "magic damage", 2456, 105)
hero_tank = hero("Tigreal", "tank", "physical damage", 2690, 112)

print(f'''
      {hero_mm.name}
      {hero_mm.role}
      {hero_mm.health} HP
      {hero_mm.auto_atk_dmg} basic attack damage
      {hero_mm.dmg_type}
      {hero_mm.describe()}
      
      {hero_assas.name}
      {hero_assas.role}
      {hero_assas.health} HP
      {hero_assas.auto_atk_dmg} basic attack damage
      {hero_assas.dmg_type}
      {hero_assas.describe()}
      
      {hero_support.name}
      {hero_support.role}
      {hero_support.health} HP
      {hero_support.auto_atk_dmg} basic attack damage
      {hero_support.dmg_type}
      {hero_support.describe()}
      
      {hero_mage.name}
      {hero_mage.role}
      {hero_mage.health} HP
      {hero_mage.auto_atk_dmg} basic attack damage
      {hero_mage.dmg_type}
      {hero_mage.describe()}
      
      {hero_tank.name}
      {hero_tank.role}
      {hero_tank.health} HP
      {hero_tank.auto_atk_dmg} basic attack damage
      {hero_tank.dmg_type}
      {hero_tank.describe()}''')