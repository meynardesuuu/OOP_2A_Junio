# Junio, Meynard Brian Y.
# BSIT - 2A

class mlhero():
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def introduction(self):
        print(f"{self.name} is a {self.role} hero.")
        
hero1 = mlhero("Irithel", "Marksman")
hero1.introduction()