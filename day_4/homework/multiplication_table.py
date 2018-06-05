# DONE: program wypisujący tabliczkę mnozenia (1 do 10) dla podanej przez użytkownika liczby
# np: 3 x 1 = 3
#     3 x 2 = 6
#     3 x 3 = 9 itp

n = input("Provide digit (1-X): ")
#n = int(n)
if n.isdigit():
    n = n.lstrip('+-')
    n = int(n)
    if n != 0:
        print(n, 'x 1 =', n*1)
        print(n, 'x 2 =', n*2)
        print(n, 'x 3 =', n*3)
        print(n, 'x 4 =', n*4)
        print(n, 'x 5 =', n*5)
        print(n, 'x 6 =', n*6)
        print(n, 'x 7 =', n*7)
        print(n, 'x 8 =', n*8)
        print(n, 'x 9 =', n*9)
    else:
        print("Provided digit is 0!")
else:
    print("Provided data isn't digit")