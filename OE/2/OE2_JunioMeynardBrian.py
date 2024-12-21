# Junio, Meynard Brian Y.
# BSIT - 2A

phones = []

class Phone:
    def __init__(self, pbrand, pmodel, pcolor, prom):  
        self.pbrand = pbrand
        self.pmodel = pmodel
        self.pcolor = pcolor
        self.prom = prom    
        
    def add_phone(self):
        print('\n' * 100)
        print("================ ADD PHONE =================")
        pbrand = input("Enter phone brand: ")
        pmodel = input("Enter phone model: ")
        pcolor = input("Enter phone color variant: ")
        prom = input("Enter phone storage variant: ")
        in_phone = Phone(pbrand, pmodel, pcolor, prom)
        phones.append({'Brand': in_phone.pbrand, 'Model': in_phone.pmodel, 'Color': in_phone.pcolor, 'Storage': in_phone.prom})
        print('\n' * 100)
        print("============================================")
        print(f"{pbrand} successfully added!")
        self.mainmenu()
        
    def mod_phone(self):
        print('\n' * 100)
        print("========== MODIFY PHONE PROPERTIES =========")
        for i in range(len(phones)):
            cp = phones[i]
            print(f"{i+1}. {cp['Brand']}")
        print('')
        while True:
            user_in = input("Select Phone to be edited (Press ENTER to cancel): ")
            if user_in == '':
                print('\n' * 100)
                self.mainmenu()
                break
            else:
                break
        print(f"SELECTED: {phones[int(user_in)-1]['Brand']}")
        print("1.) Edit Brand")
        print("2.) Edit Model")
        print("3.) Edit Color")
        print("4.) Edit Storage")
        while True:
            opt = input("Enter selection: ")
            if opt == '1':
                pbrand = input("Enter new brand value: ")
                phones[int(user_in)-1]['Brand'] = pbrand
                print('\n' * 100)
                print("============================================")
                print(f"Brand updated to {pbrand}")
                self.mainmenu()
                break
            elif opt == '2':
                pmodel = input("Enter new model value: ")
                phones[int(user_in)-1]['Model'] = pmodel
                print('\n' * 100)
                print("============================================")
                print(f"Model updated to {pmodel}")
                self.mainmenu()
                break
            elif opt == '3':
                pcolor = input("Enter new color value: ")
                phones[int(user_in)-1]['Color'] = pcolor
                print('\n' * 100)
                print("============================================")
                print(f"Color updated to {pcolor}")
                self.mainmenu()
                break
            elif opt == '4':
                prom = input("Enter new storage value: ")
                phones[int(user_in)-1]['Storage'] = prom
                print('\n' * 100)
                print("============================================")
                print(f"Storage updated to {prom}")
                self.mainmenu()
                break
            else:
                print("Invalid Input!")
    
    def rev_phone(self):
        print('\n' * 100)
        print("=============== DELETE PHONE ================")
        for i in range(len(phones)):
            cp = phones[i]
            print(f"{i+1}. {cp['Brand']}")
        print('')
        while True:
            print("Select Phone to be deleted")
            index = input("Press ENTER to return back to main menu: ")
            if index == '':
                print('\n' * 100)
                self.mainmenu()
                break
            else:
                break
        del phones[int(index)-1]
        print('\n' * 100)
        print("============================================")
        print(f"Phone has been deleted")
        self.mainmenu()
            
    def rev_phoneatt(self):
        print('\n' * 100)
        print("=============== DELETE PHONE ================")
        for i in range(len(phones)):
            cp = phones[i]
            print(f"{i+1}. {cp['Brand']}")
        print('')
        while True:
            user_in = input("Select Phone to be modified (Press ENTER to cancel): ")
            if user_in == '':
                print('\n' * 100)
                self.mainmenu()
                break
            else:
                break
        print('\n' * 100)
        print("============================================")
        print(f"SELECTED: {phones[int(user_in)-1]['Brand']}")
        print("1.) Delete Brand")
        print("2.) Delete Model")
        print("3.) Delete Color")
        print("4.) Delete Storage")
        while True:
            opt = input("Enter selection (Press ENTER to cancel): ")
            if opt == '1':
                del phones[int(user_in)-1]['Brand']
                print('\n' * 100)
                print("============================================")
                print("Brand deleted successfully!")
                self.mainmenu()
                break
            elif opt == '2':
                del phones[int(user_in)-1]['Model']
                print('\n' * 100)
                print("============================================")
                print("Model deleted successfully!")
                self.mainmenu()
                break
            elif opt == '3':
                del phones[int(user_in)-1]['Color']
                print('\n' * 100)
                print("============================================")
                print("Color deleted successfully!")
                self.mainmenu()
                break
            elif opt == '4':
                del phones[int(user_in)-1]['Storage']
                print('\n' * 100)
                print("============================================")
                print("Storage deleted successfully!")
                self.mainmenu()
                break
            elif opt == '':
                print('\n' * 100)
                self.mainmenu()
                break
            else:
                print("Invalid Input!")
        
    def list_phone(self):
        print('\n' * 100)
        print("============================================")
        print("ITEM/S IN THE INVENTORY:")
        if len(phones) == 0:
            print('Empty')
        elif len(phones) >= 1:
            for i in range(len(phones)):
                cp = phones[i]
                '''print(f"{i+1}. Brand: {cp['Brand']}\n   Model: {cp['Model']}\n   Color: {cp['Color']}\n   Storage: {cp['Storage']}")'''
                print(f"{i+1}. {cp}")
            print('')
        while True:
            user_in = input("Press ENTER to return to main menu")
            if user_in == '':
                print('\n' * 100)
                self.mainmenu()
                break
            else:
                print("Invalid Input!")
        
    def mainmenu(self):
        print("=============== PHONE INVENTORY ===============")
        print("1.) Add Phone")
        print("2.) Modify Phone")
        print("3.) Delete Phone Attributes")
        print("4.) Delete Phone")
        print("5.) List All Phones")
        print("6.) Exit Program")
    
        while True:
            user_in = input("Enter Selection: ")
            if user_in == '1':
                self.add_phone()
                break
            elif user_in == '2' and len(phones) == 0:
                print("Add items first!")
            elif user_in == '2':
                self.mod_phone()
                break
            elif user_in == '3' and len(phones) == 0:
                print("Add items first!")
            elif user_in == '3':
                self.rev_phoneatt()
                break
            elif user_in == '4' and len(phones) == 0:
                print("Add items first!")
            elif user_in == '4':
                self.rev_phone()
                break
            elif user_in == '5' and len(phones) == 0:
                print("Add items first!")
            elif user_in == '5':
                self.list_phone()
                break
            elif user_in == '6':
                print("Exiting script....")
                break
            else:
                print("Invalid input!")
        

main = Phone(None, None, None, None)
print('\n' * 100)
main.mainmenu()