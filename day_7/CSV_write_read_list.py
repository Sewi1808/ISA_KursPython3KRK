import csv

lista1 = ['Imie', 'Nazwisko', 'Adres', 'Telefon']
lista2 = ['Joanna', 'Kowalska', 'Gdansk Przytulna', '64 654-65-45']
lista3 = ['Adam', 'Nowak', 'Gdynia Swietojanska' , '0700325487']

lista_list = [lista1, lista2, lista3]

with open('my_csv.csv', 'w+', newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(lista_list)
    csv_file.seek(0, 0)
    reader = csv.reader(csv_file)
    for row in reader:
        print(', '.join(row))
