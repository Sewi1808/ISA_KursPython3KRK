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
"""Phone book program"""


first_names = ["_"]
second_names = ["_"]
phone_numbers = ["_"]
zipped = []


def entry():

    """
    Function "ENTRY" responsible for add single entry to "zipped" list which is currently my "database"
    Variable first_name/second_name/phone_number are responsible exactly same as named.
    """

    first_name = input("Provide first name: \n")
    second_name = input("Provide second name: \n")
    phone_number = input("Provide phone number: \n")
    global zipped

    if first_name == second_name == phone_number == "":  # check if user provide 3 times nothing, if yes just pass
        pass
    elif first_name in first_names and second_name in second_names and phone_number in phone_numbers:
        print("Mentioned user already exist")

    else:

        first_names.append(first_name)
        second_names.append(second_name)
        phone_numbers.append(phone_number)
        zipped = list(enumerate(zip(first_names, second_names, phone_numbers)))
        return True


def print_zipped():
    for line in zipped:
        print(line)


# entry()
# print_zipped()
