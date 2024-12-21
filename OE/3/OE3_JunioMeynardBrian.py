# Junio, Meynard Brian Y.
# BSIT - 2A

class SocialMediaAccount():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def login(self):
        pass
    
    def post(self):
        pass
    
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, fol_num):
        super().__init__(username, password, fol_num)
        self.fol_num = fol_num
        
    def share_story(self):
        pass
    
class XAccount(SocialMediaAccount):
    def __init__(self, username, password, fol_twts):
        super().__init__(username, password, fol_twts)
        self.fol_twts = fol_twts
        
    def tweet(self):
        pass
    
ig_acc = InstagramAccount("meynardesuuu", "1234", 120)
x_acc = XAccount("meymey", "2004", 56)
        

        

    