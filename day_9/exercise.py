class PojazdMechaniczny(object):
    def __init__(self, silnik, pojemnosc):
        self.silnik = silnik
        self.pojemnosc = pojemnosc

    def odpal_silnik(self):
        return "kle kle kle (diesel)"

    def all_ret(self):
        return f"silnik: {self.silnik} \npojemnosc: {self.pojemnosc}"

class Samochod(PojazdMechaniczny):
    def __init__(self, marka, model, pojemnosc):
        super().__init__(True, pojemnosc)
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



VW = Samochod("VW", "Polo", "1.4")
# input("Podaj Marke: \n"), input("Podaj Model: \n")
# Samochod.klakson(VW, int(input("Podaj ilosc klaksonow:\n")))
#
# print(VW.silnik)
# print(VW.odpal_silnik())

poj_m = PojazdMechaniczny(VW.silnik, VW.pojemnosc)
print(poj_m.all_ret())