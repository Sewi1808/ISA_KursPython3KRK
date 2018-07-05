# program kadrowy / ksiegowy
# funkcjonalnosci:
# druk fatkur
# suma wynagrodzen mc
# suma wynagrodzen rok
# operajac sie na static method/classmethod etc.
# normalizacja wynagrodzenia do wartosci rocznej
# wynagrodzenie = int
# wprowadzenie wynagrodzenia /h/d/m/y
# porownanie pracownikow (porownanie wynagrodzen)
# metoda ktora automatycznie zatrudnia sprzataczki i kierowcow
# lista pracownikow (chronione)
# wylistowanie (oddzielone spacjami, imie nazwisko i wynagrodzenie)
# metody obliczajace stanowiska/dzialy na wynagrodzenia i per firma

employee = {"00000":
                {"Name": "Place_Holder", "Surname": "Place_Holder", "Salary": "Place_Holder",
                 "Position": "Place_Holder"
                 }
            }


class Pracownik:

    # pola klasy



    def __init__(self, imie, nazwisko, pensja, stanowisko):
        self.__nazwisko = nazwisko
        self.__pensja = pensja
        self.__imie = imie
        self.__stanowisko = stanowisko

    @property
    def pracownik_return(self):
        return str(f"{self.__nazwisko}, {self.__imie}")


class Position:
    def __init__(self, name, default_salary):
        self.__name = name
        self.__default_salary = default_salary

    @property
    def position_return(self):
        return str(f"{self.__name}, {self.__default_salary}")


Adam = Pracownik("Adam", "Kowalski", 2500, "Kierowca")
Kierowca = Position("Kierowca", 3200)
print(Adam.pracownik_return)
print(Kierowca.position_return)
