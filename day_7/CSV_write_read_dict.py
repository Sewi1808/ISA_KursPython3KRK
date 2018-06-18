import csv
import sys

d0 = {'Imie': '_', 'Nazwisko': '_', 'Adres': '_', 'Telefon': '_'}
d1 = {'Imie': 'Joanna', 'Nazwisko': 'Kowalska', 'Adres': 'Gdansk Przytulna', 'Telefon': '64 654-65-45'}
d2 = {'Imie': 'Adam', 'Nazwisko': 'Nowak', 'Adres': 'Gdynia Swietojanska', 'Telefon': '0700325487'}

d_d = {0: d0, 1: d1, 2: d2}

with open('my_csv_dict.csv', 'w+', newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fields)
