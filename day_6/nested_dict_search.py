book = {
        0: {'First Name': '_', 'Second Name': '_', 'Age': '_', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        1: {'First Name': 'Adam', 'Second Name': 'ASDF', 'Age': '35', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        2: {'First Name': 'Aleksandra', 'Second Name': 'QWE', 'Age': '31', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        3: {'First Name': 'Sebastian', 'Second Name': 'Sza', 'Age': '31', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        }

"""szukajka"""
for dicts in book:
    for entry in book[dicts]:
        if book[dicts][entry][ 'First Name' == 'Adam']:
            print(entry, " : ", book[dicts][entry])
