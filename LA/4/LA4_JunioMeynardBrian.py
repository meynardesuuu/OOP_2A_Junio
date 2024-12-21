# Junio, Meynard Brian Y.
# BSIT - 2A

class mlhero():
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def __str__(self):
        return f"{self.name} is a {self.role} hero."
        
hero1 = mlhero("Irithel", "Marksman")
print(hero1)