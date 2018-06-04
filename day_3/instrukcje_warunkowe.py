ADMIN_USERNAME = 'piotr'

name = input('Podaj imie: ')
if name.lower() == ADMIN_USERNAME:
    print('Hello', name)
else:
    print('Hej', name,  'polkikash?')