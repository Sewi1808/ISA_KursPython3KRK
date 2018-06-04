#  napisz program ktory sprawdzi ktory sprawdzi czy liczba jest parzysta
#  liczba do sprawdzenia jest podawana przez uzyszkodnika

num = int(input("Give me a number to check: "))
x = num % 2


if x > 0:
    print(num, "is odd number")
else:
    print(num, "is even number")



