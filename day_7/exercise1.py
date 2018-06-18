# import datetime
# import csv

# .seek - 2 argumeny (0,0) od poczatku, drugi argument przyjmuje jedna z 3
# wartosci 0,1,2

plik = open('Test1', 'r+')
# plik_py = open('Test.py', 'w')


print(plik.tell())
print(plik.readlines())
print(len(plik.readlines()))
print(plik.tell())

plik = open('Test1', 'r')

print("tell _1_ plik:\n:", plik.tell())
print("len of plik:\n:", len(plik.readlines()))
print("tell _2_ plik:\n:", plik.tell())
plik.seek(0, 0)
print("tell _3_ plik:\n:", plik.tell())



plik.close()
