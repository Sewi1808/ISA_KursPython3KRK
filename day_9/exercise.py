class Samochod(object):
    def __init__(self, marka, model):
        self.marka = print("Marka: ", marka)
        self.model = print("Model: ", model)
    def klakson(self):
        self.klakson = print("Beep")


VW = Samochod(input("Podaj Marke: \n"), input("Podaj Model: \n"))

Samochod.klakson(VW)
