# Junio, Meynard Brian Y.
# BSIT - 2A

class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describeSpiderman(self):
        print(f"Spiderman's Name: {self.name} Age: {self.age}")
        
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
sp1 = Tobey("Tobey Maguire", 49, "Spider-Man")
sp2 = Andrew("Andrew Garfield", 41, "The Amazing Spider-Man")
sp3 = Tom("Tom Holland", 28, "Spider-Man: Homecoming")

print(sp1.name.upper(), sp1.movieTitle)
print(sp2.name.upper(), sp2.movieTitle)
print(sp3.name.upper(), sp3.movieTitle)
