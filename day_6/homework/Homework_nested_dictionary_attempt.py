# Zadania domowe:
# a. Napisz program, który będzie bazą kontaktów, program ma pytać
# użytkownika, co chce zrobić, dając mu minimum te opcje: dodanie imienia,
# usuniecie imienia, sprawdzenie czy imię jest w bazie, usunięcie imienia,
# sprawdzenie ilości imion w bazie oraz zakończenie programu.
# Jeśli czujesz się pewniej to postaraj się aby użytkownik mógł podać więcej
# szczegółów np. nazwisko, nr telefonu, adres itp.
# Program ten będziemy pomału rozbudowywać, w kolejnych tygodniach
# Oczywiście piszemy już „Czysty kod” stosując się do konwencji
# Python’owych: piszemy docstringi, właściwe i znaczące nazwy zmiennych
# oraz funkcji. I jeśli damy radę to możemy postarać się stworzyć moduły z
# oddzielnymi funkcjonalnościami.
######################################################################################################################
import sys
"""Phone book program"""
main_menu_options = ['Q', '1', '2', '3']
y_n_option = ['y','n']
book = {0: {'First Name': '_', 'Second Name': '_', 'Age': '_', 'Phone Number': '_', 'City': '_', 'Postal Code': '_',
            'Street': '_'}, }
#done
def wrong_input():
    print("Invalid input provided, do you want continue(y/n): \n")
    user_input = input().lower()
    while user_input not in y_n_option:
        wrong_input()
    else:
        main_menu()

#done
def print_book():
    for line in book:
        print(line, book[line], "print book")

#done
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
                           'Street': street},

#work in progress
def main_menu():    # work in progress
    user_first_input = input("Q - Quit\n1 - search menu\n2 - append menu\n3 - "
                             "delete menu\n YOUR CHOICE (Q/1/2/3):\n").upper()
    if user_first_input not in main_menu_options:
        comunicate1 = input("Wrong input provided, do you want to continue (y/n):\n").lower()
        while comunicate1 in y_n_option:
            if comunicate1 == 'y':
                main_menu()
            elif comunicate1 == 'n':
                sys.exit()
            else:
                wrong_input()
    elif user_first_input == 'Q':
        sys.exit()
    elif user_first_input == '1':
        pass    # placeholder
    elif user_first_input == '2':
        entry()
        print_book()
        main_menu()
    else:
        main_menu()

main_menu()
# entry()
# print_book()
# entry()
# print_book()

# # def tpye_of_search()
# def search():
#     search_cond = input("Type fraze: \n")
#     idx_search = None
#     if search_cond in first_names:
#         idx_search = first_names.index(search_cond)
#     elif search_cond in second_names:
#         idx_search = second_names.index(search_cond)
#     elif search_cond in phone_numbers:
#         idx_search = phone_numbers.index(search_cond)
#     else:
#         print("Fraze was not found!")


# print(zipped.index(search_cond)

# if search_cond in zipped:
#     for _ in zipped:
#         if _ in zipped:
#             print(_)

#
# def search_menu():
#     print("choose action:\n 1 - show full contact list \n 2 - search in contact list")
#     action = input("Input action: \n")
#     if action == 1:
#         print_zipped()
#     elif action == 2:
#         pass  # placeholder na szukajke
#     else:
#         pass

        # action != 1 or action != 2:
        # print("please input 1 or 2 according to action menu")
        # search_menu()
        #