# program wydający resztę z podanych monet []
# do debugowania
monety =        [5, 2, 1, 0.5, 0.2, 0.1]
monety_reszta = [0, 0, 0,   0,   0,   0]

banknot = 20
zakup = 8.30
reszta = banknot - zakup

print(reszta)

indeks_mon_reszta = 0

for moneta in monety:
    if reszta >= moneta:
        ilosc = reszta // moneta
        wartosc = ilosc * moneta
        reszta = reszta - wartosc
        monety_reszta[indeks_mon_reszta] = ilosc
    indeks_mon_reszta += 1
print(monety_reszta)
print(sum(monety_reszta))