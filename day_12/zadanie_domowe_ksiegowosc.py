#program kadrowy / ksiegowy
#funkcjonalnosci:
#druk fatkur
#suma wynagrodzen mc
#suma wynagrodzen rok
#operajac sie na static method/classmethod etc.
#normalizacja wynagrodzenia do wartosci rocznej
#wynagrodzenie = int
#wprowadzenie wynagrodzenia /h/d/m/y
#porownanie pracownikow (porownanie wynagrodzen)
#metoda ktora automatycznie zatrudnia sprzataczki i kierowcow
#lista pracownikow (chronione)
#wylistowanie (oddzielone spacjami, imie nazwisko i wynagrodzenie)
#metody obliczajace stanowiska/dzialy na wynagrodzenia i per firma



class Pracownik:
    def __init__(self, imie, nazwisko, pensja, stanowisko):
        self.__nazwisko = nazwisko
        self.__pensja = pensja
        self.__imie = imie
        self.__stanowisko = stanowisko


    @property
    def  pracownik(self):
        return str(f"{self.__nazwisko}, {self.__imie}")


Adam = Pracownik("Adam", "Kowalski", "2500")
print(Adam.Pracownik)