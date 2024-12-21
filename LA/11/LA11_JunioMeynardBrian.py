# Junio, Meynard Brian Y.
# BSIT - 2A

class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def describePhone(self):
        print(f"PHONE_BRAND: {self.brand}\nPHONE_MODEL: {self.model}")
        
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

ex_phone = Android("Google", "Pixel 6")
ex_phone.describePhone()
