# Junio, Meynard Brian Y.
# BSIT - 2A

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("ERROR: Amount is negative")
    def withdraw(self, amount):
        if amount > 0:
            self.__balance = self.__balance - amount
        else:
            print("ERROR: Amount is negative")
    def display_account_info(self):
        return f'''Account Number: {self.__account_number}
Current Balance: P{self.__balance}'''
    # Getter Methods
    def get_account_number(self):
        return f"Account Number: {self.__account_number}"
    def get_balance(self):
        return f"Current Balance: P{self.__balance}"
    # Setter Methods
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
        else:
            print("ERROR: Amount is negative")
        
account1 = BankAccount(12345678, 250.00)
print(account1.get_balance())
account1.deposit(150.00)
print(account1.get_balance())
account1.withdraw(200.00)
print(account1.get_balance())
account1.set_balance(-10)
print(account1.display_account_info())
