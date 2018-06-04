ADMIN_USERNAME = 'piotr'
name = input('Podaj imie: ')
#name lower -> then capitalized
name_capitalized = name.lower().capitalize()

if name.lower() == ADMIN_USERNAME:
    print('Hello', name_capitalized)
else:
    print('Hej', name_capitalized,  'polkikash?')