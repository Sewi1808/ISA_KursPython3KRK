num = int(input("Podaj gorny zakres: \n"))

r = range(num + 1)
even = []
odd = []
o = int(0)
e = int(0)

for check in r:
    if check % 2:
        odd.append(check)
        o +=1
    else:
        even.append(check)
        e +=1

print("Parzyste liczby z zakresu: \n", even)
print("Nieparzyste liczby z zakresu: \n", odd)
print("Ilosc liczb parzystych: \n", e)
print("Ilosc liczb nieparzystych: \n", o)