# done: pobierz od uzyszkodnika 2 liczby
# done: w petli while sprawdz czy a jest wieksze od b
# done: jesli tak to a zmienjsz o 1

a = int(input("Podaj A: \n").lstrip("-+"))
b = int(input("Podaj B: \n").lstrip("-+"))

z = []

while a > b:
    z.append(a)
    print(a)
    a = a-1

print("lista Z zawiera: \n",z)