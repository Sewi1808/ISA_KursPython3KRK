# DONE: Narysuj piramidę Mario - jako input - wysokość piramidy
# DONE: np. piramida wysokości 3 ma wyglądać:

  #
 ###
#####


# TODO: program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# TODO: continue

# program obliczajacy liczbe liter i cyfr w stringu

ilosc_liter = str(len("Tomek36"))
print(ilosc_liter)

# program wypisujący tabliczkę mnozenia (1 do 10) dla podanej przez użytkownika liczby
# np: 3 x 1 = 3
#     3 x 2 = 6
#     3 x 3 = 9 itp

# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata


#wpisz wiek psa
wiek_psa = int(input("Podaj wiek psa?: "))
wiek2 = wiek_psa * 4 - 8

#jesli 1 lub 2 to x10,5
if wiek_psa < 3:
    wiek = wiek_psa * (10.5)
    print("Twoj pies ma {} lat".format(wiek))

elif wiek_psa > 2:
     wiek_staregopsa = wiek2 + 21
     print("Twoj pies jest stary i ma {} lat".format(wiek_staregopsa))




#jesli 3 lub wiecej to x4
#podaj wiek w ludzkich latach