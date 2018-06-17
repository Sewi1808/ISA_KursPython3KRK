import sys
"""Phone book program"""

"""varebiles"""
main_menu_options = ['Q', '1', '2', '3']
y_n_option = ['y', 'n']
search_menu_options = ['1', '2', '3', '4', '5', '6', 'Q', 'B']
""" dictionary "book" is an temporary solution, will be replaced by save/read file feature"""
book = {
        0: {'First Name': '_', 'Second Name': '_', 'Age': '_', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'},
        1: {'First Name': 'Adam', 'Second Name': 'ASDF', 'Age': '35', 'Phone Number': '_',
            'City': '_', 'Postal Code': '_',
            'Street': '_'},
        2: {'First Name': 'Aleksandra', 'Second Name': 'QWE', 'Age': '31', 'Phone Number': '_',
            'City': '_', 'Postal Code': '_',
            'Street': '_'},
        3: {'First Name': 'Sebastian', 'Second Name': 'Sza', 'Age': '31', 'Phone Number': '_',
            'City': '_', 'Postal Code': '_',
            'Street': '_'},
        4: {'First Name': 'Adam', 'Second Name': 'Sza', 'Age': '51', 'Phone Number': '_',
            'City': '_', 'Postal Code': '_', 'Street': '_'},
        }

"""Functions"""


def search():
    """Search module, looks for value in every nested dictionary, returns value of parent dictionary,
    allow program to print full data of entry"""
    search_result = []  #storage of "parent dictionaries"
    search_data = input("Provide data to find: \n")
    for i in book:
        for k in book[i].items():
            if k[1] == search_data:
                search_result.append(i)

    for i in search_result:
        print(book[i])


def search_menu():
    """choose action menu, description according to input string 1 - print whole dictionary, 2 len of dictionary,
    3 data search, Q - quit, B - back to main menu #TODO: 4 which will stand for delete from dictionary"""
    search_menu_input = input("Choose action:\n"
                              "1 - show whole list\n2 - len of list\n3 - search data \n"
                              "Q - quit\nB - Back to main menu\n\nYour choice:\n").upper()
    if search_menu_input in search_menu_options:
        if search_menu_input == 'Q':
            print('sys exit search menu')
            sys.exit()
        elif search_menu_input == 'B':
            print("Going back to main menu")
            main_menu()
        elif search_menu_input == '1':
            for book_id, book_info in book.items():
                print("\nBook ID:", book_id)
                for key in book_info:
                    print(key + ":", book_info[key])
            print("\n\n")
            search_menu()
        elif search_menu_input == '2':
            print(f"Your phone book list have {len(book)} entry(ies)\n")
            search_menu()
        elif search_menu_input == '3':
            search()
            search_menu()
    else:
        wrong_input()


def wrong_input():
    """module which stand for 'wrong input' message for user"""
    print("Invalid input provided, do you want continue(y/n): \n")
    user_input = input().lower()
    if user_input in y_n_option:
        if user_input == 'y':
            main_menu()
        else:
            print("sys exit in wrong_input")
            sys.exit()
    else:
        wrong_input()


def print_book():
    """module stands for printing address book line by line"""
    for line in book:
        print(line, book[line])


def entry():
    """
    Function "ENTRY" responsible for add single entry to "book" dictionary which is currently my "database"
    Variable first_name/second_name/phone_number/etc are responsible exactly same as named.
    """

    first_name = input("Provide first name: \n")
    second_name = input("Provide second name: \n")
    age = input("Provide Age: \n")
    phone_number = input("Provide phone number: \n")
    city = input("Provide city: \n")
    postal_code = input("Provide postal code: \n")
    street = input("Provide street: \n")

    if first_name == second_name == phone_number == age == city == postal_code == street == "":
        # check if user provide 7 times nothing, if yes just pass
        print("No entry data provided")
        pass
    elif first_name in book and second_name in book and age in book and phone_number in book and city in book \
            and postal_code in book and street in book:
        print("Mentioned user already exist")
        user_already_exist = input("Do you want continue(y/n): \n").lower()
        if user_already_exist == 'y':
            entry()
        else:
            pass

    else:
        book[len(book)] = {'First Name': first_name, 'Second Name': second_name, 'Age': age,
                           'Phone Number': phone_number, 'City': city, 'Postal Code': postal_code,
                           'Street': street}


def main_menu():
    """Main menu"""
    user_first_input = input("Q - Quit\n1 - search menu\n2 - append menu\n3 - "
                             "delete menu\n YOUR CHOICE (Q/1/2/3):\n").upper()
    if user_first_input not in main_menu_options:
        wrong_input()

    elif user_first_input == 'Q':
        print("sys exit in main_menu=>user_first_input = Q")
        sys.exit()
    elif user_first_input == '1':
        search_menu()
    elif user_first_input == '2':
        entry()
        print_book()
        main_menu()
    else:
        main_menu()


"""Executive part"""
main_menu()
