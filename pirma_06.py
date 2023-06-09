"""Pirma užduotis - OOP #1:
Susikurti klasę “BankoSąskaita”, kuri saugotų sąskaitos numerį ir balansą.
 Klasė turi turėti metodus pinigų pridėjimui
 prie balanso, pinigu išėmimui bei balanso grąžinimui.

Susikurti “BankoSąskaita” klasės objektą ir išbandyti visus metodus bent po vieną kartą.


# Create a bank account object
account = BankAccount("1234567890")

# Deposit funds
print(account.deposit(1000))

# Withdraw funds
print(account.withdraw(500))

# Check account balance
balance = account.get_balance()
print("Account Balance:", balance)
"""

class BankAccount:
    def __init__(self, account, deposit):
        self.account = account
        self.deposit = deposit

    def __str__(self):
        return f"{self.account}: {self.deposit}"


    # likutis = []
    def pinigu_pridejimas(self, prideti):
         self.deposit += prideti

    def pinigu_isejimas(self, atimti):
         self.deposit -= atimti




account1 = BankAccount("Ginas 13254645", 100)
print(account1)

print(account1.pinigu_pridejimas(50))
print(account1.pinigu_isejimas(200))
print(account1.pinigu_isejimas(300)) #reikejo su return( kad nebutu None) ir naudoti append, bet tada "+= neveikia"
print(account1.pinigu_pridejimas(100))

print("Likutis", account1.deposit)




