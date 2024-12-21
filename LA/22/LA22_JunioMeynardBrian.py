# Junio, Meynard Brian Y.
# BSIT - 2A

class BdayParty:
    def __init__(self, theme, foodList, secDish):
        self.theme = theme
        self.foodList = foodList
        self.__secDish = secDish
        
    def listOfFoods(self): # Public
        print(self.theme)
        print(f"Food list: {self.foodList}")
        self.__secretDish()
        
    def __secretDish(self): # Private
        print(f"The secret dish is {self.__secDish}")
        
xmas = BdayParty("Christmas Eve", "Fruit Salad, Hamonado, Lechon Manok", "Graham")
fiesta = BdayParty("Barangay Fiesta", "Pancit, Lechon, Menudo", "Lumpia")
bday = BdayParty("21st Birthday", "Carbonara, Mocha Cake, Caldereta", "Tiramisu Cake")

xmas.listOfFoods()
fiesta.listOfFoods()
bday.listOfFoods()

