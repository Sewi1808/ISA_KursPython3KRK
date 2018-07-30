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

employee = {0:
                {
                    "Name": "Place_Holder", "Surname": "Place_Holder",
                    "Salary": "Place_Holder", "Position": "Place_Holder"},
            1:
                {
                    "Name": "Anna", "Surname": "Nowak",
                    "Salary": 3300, "Position": "Clean Service"}
            }


class Position:
    def __init__(self, position_name, default_salary):
        self.position_name = position_name
        self.default_salary = default_salary

    @property
    def position_return(self):
        return str(f"{self.position_name}, {self.default_salary}")


class Employe(Position):

    def __init__(self, name, surname, salary, position_name):
        self.surname = surname
        self.salary = salary
        self.name = name
        self.position_name = position_name

    @property
    def emp_return(self):
        return str(f"{self.surname} {self.name} {self.salary}")

    def emp_append(self):
        employee[len(employee)] = {"Name": self.name, "Surname": self.surname,
                                   "Salary": self.salary, "Position": self.position_name
                                   }

    def emp_comparision(self):
        if self.salary == employee[1]["Salary"]:
            return str("Salary Equal")
        elif self.salary > employee[1]["Salary"]:
            return str(f"{self.name} has bigger salary")
        elif self.salary < employee[1]["Salary"]:
            return str(f"{self.name} has smaller salary")
        else:
            return str(f"bug happend")



Adam = Employe("Adam", "Kowalski", 2500, "Kierowca")
#Kierowca = Position("Kierowca", 3200)
# print(Adam.emp_return)
#print(Kierowca.position_return)
Adam.emp_append()
for i in employee.items():
    print(i)

print(Adam.emp_comparision())
