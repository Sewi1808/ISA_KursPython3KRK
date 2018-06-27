class PojazdMechaniczny(object):
    def __init__(self, silnik=True):
        self.silnik = silnik


class Samochod(PojazdMechaniczny):
    def __init__(self, marka, model):
        super().__init__()
        self.marka = print("Marka: ", marka)
        self.model = print("Model: ", model)

    def klakson(self, multiple=1):
        self.multiple = multiple
        while True:
            if multiple > 1:
                self.klakson = print("Beep")
                multiple -= 1
            else:
                self.klakson = print("Beep")
                break



VW = Samochod(input("Podaj Marke: \n"), input("Podaj Model: \n"))

Samochod.klakson(VW, int(input("Podaj ilosc klaksonow:\n")))

print(VW.silnik)
