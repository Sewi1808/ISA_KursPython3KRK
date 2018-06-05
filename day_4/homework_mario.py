# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:

  #
 ###
#####

wysokosc = input('Podaj wysokosc piramidy Mario(liczba calkowita): ').lstrip('-+')

if wysokosc.isdigit():
    wysokosc=int(wysokosc)
    for i in range(wysokosc):
        print(" " * (wysokosc - 1 * i) + ("#") + ("#" * (1 * i)) + ("#" * (1 * i)))
else:
    print("Wartosc nie jest liczba calkowita")

#print(type(wysokosc))
#wysokosc = int(wysokosc)
#print(type(wysokosc))

