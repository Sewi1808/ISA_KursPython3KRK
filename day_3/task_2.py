#  napisz program ktory sprawdzi ktory sprawdzi czy liczba jest parzysta
#  liczba do sprawdzenia jest podawana przez uzyszkodnika

num = input("Give me a number to check: ")

#  sprawdz czy podane dane to liczba
if num.lstrip('-+').isdigit():
    x = int(num) % 2
    if x > 0:
        print(num, "is odd number")
    else:
        print(num, "is even number")
else:
    print("provided data isn't number")