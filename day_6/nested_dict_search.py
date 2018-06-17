
book = {
        0: {'First Name': '_', 'Second Name': '_', 'Age': '_', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        1: {'First Name': 'Adam', 'Second Name': 'ASDF', 'Age': '35', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        2: {'First Name': 'Aleksandra', 'Second Name': 'QWE', 'Age': '31', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        3: {'First Name': 'Sebastian', 'Second Name': 'Sza', 'Age': '31', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        4: {'First Name': 'Adam', 'Second Name': 'Sza', 'Age': '51', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        }

"""szukajka"""


def search():
    search_result = []
    search_data = input("Provide data to find: \n")
    for i in book:
        for k in book[i].items():
            if k[1] == search_data:
                search_result.append(i)

    for i in search_result:
        print(book[i])