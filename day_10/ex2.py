class Person(object):
    def __init__(self, imie, nazwisko, pseudonim="okon"):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pseudonim = pseudonim

    def przedstaw_sie(self):
        return self.imie + " " + self.pseudonim + " " + self.nazwisko

    def __str__(self):
        return self.przedstaw_sie()


Jas = Person("Jas", "Jezioro", "inny")
Ola = Person("Ola", "Nowak")

# Jas.przedstaw_sie()
# Ola.przedstaw_sie()
print(Jas)
print(Ola)