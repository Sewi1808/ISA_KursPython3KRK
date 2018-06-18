import csv

lista1 = ['Imie', 'Nazwisko', 'Adres', 'Telefon']
lista2 = ['Joanna', 'Kowalska', 'Gdansk Przytulna', '64 654-65-45']
lista3 = ['Adam', 'Nowak', 'Gdynia Swietojanska' , '0700325487']

lista_list = [lista1, lista2, lista3]

dict_list = {0: lista1, 1: lista2, 2: lista3}

with open('test_csv.csv', 'w+') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= 'fieldnames')

    writer.writeheader()
    writer.writerows(dict_list)
    csvfile.seek(0, 0)
    print(open(csvfile))
