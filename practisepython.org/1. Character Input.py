# Character input

import datetime

name = str(input("Podaj Imie: "))
age = int(input("Podaj wiek: "))
now = datetime.datetime.now()
Y = int(100)
X = str(now.year + Y - age)

print(name + " bedzie mial 100 lat w roku: " + X)
