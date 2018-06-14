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


# b. dodatkowe zadanie dla czujących się pewniej:
# "Fair and square"
# Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice).
# A palindrome is just an integer that reads the same backwards and forwards - so 6, 11
# and 121 are all palindromes, while 10, 12, 223 and 2244 are not (even though 010=10,
# we don't consider leading zeroes when determining whether a number is a
# palindrome).
# He recently became interested in squares as well, and formed the definition of a fair
# and square number - it is a number that is a palindrome and the square of a
# palindrome at the same time. For instance, 1, 9 and 121 are fair and square (being
# palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are not fair
# and square: 16 is not a palindrome, 22 is not a square, and while 676 is a palindrome
# and a square number, it is the square of 26, which is not a palindrome.
# Now he wants to search for bigger fair and square numbers. Your task is, given an
# interval Little John is searching through, to tell him how many fair and square numbers
# are there in the interval, so he knows when he has found them all.
# Example data:
# range(from, to(including) ) output(number of fair and square numbers in range)
# 1 4 2
# 10 120 0
# 100 1000 2