# Junio, Meynard Brian Y.
# BSIT - 2A

class Pasta:
    def __init__(self, pasta, sauce, pork):
        self.pasta = pasta
        self.sauce = sauce
        self.pork = pork
    def __str__(self):
        return f"My pasta has {self.sauce} and {self.pork}, mixed in {self.pasta} type of pasta."
    
spaghetti = Pasta("spaghetti", "tomato sauce", "ground pork")
carbonara = Pasta("fettuccine", "creamy carbonara sauce", "bacon")
lasagna = Pasta("lasagna", "marinara sauce", "ground beef")
print(spaghetti)
print(carbonara)
print(lasagna)
print(spaghetti.pasta)

