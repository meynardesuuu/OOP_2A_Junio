# Junio, Meynard Brian Y.
# BSIT - 2A

from abc import ABC, abstractmethod
class Character(ABC): #abstract class
    def __init__(self, name):
        self.name = name
    
    @property
    @abstractmethod 
    def alias(self): 
        pass

class Batman(Character):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias
    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"

Bruce_Wayne = Batman("Bruce Wayne", "Batman") 
print(Bruce_Wayne.alias) 