# Junio, Meynard Brian Y.
# BSIT - 2A

class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
        
    def introduce(self, func):
        def execution(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return execution
    
char1 = AnimeCharacter("Naruto", "Shadow Clone Jutsu")

@char1.introduce
def character_intro():
    print(f"I am {char1.name} and I can use {char1.ability}")    
character_intro()