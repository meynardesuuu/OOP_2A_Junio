# Junio, Meynard Brian Y.
# BSIT - 2A

class Pasta:
    def __init__(self, pasta, sauce, pork):
        self.pasta = pasta
        self.__sauce = sauce
        self.pork = pork
    def __str__(self):
        return f"My pasta has {self.__sauce} and {self.pork}, mixed in {self.pasta} type of pasta."
    def sauce(self):
        return self.__sauce
    def set_sauce(self, newval):
        self.__sauce = newval
    
spaghetti = Pasta("spaghetti", "tomato sauce", "ground pork")
carbonara = Pasta("fettuccine", "creamy carbonara sauce", "bacon")
lasagna = Pasta("lasagna", "marinara sauce", "ground beef")

print(spaghetti)
print(spaghetti.sauce())
spaghetti.set_sauce("ketchup")
print(spaghetti.sauce())