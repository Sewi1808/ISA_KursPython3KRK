# DONE: program obliczajacy liczbe liter i cyfr w stringu


s = input('Provide some string: ')

numbers = sum(c.isdigit() for c in s)
alpha   = sum(c.isalpha() for c in s)
#spaces  = sum(c.isspace() for c in s)
#others  = len(s) - numbers - alpha - spaces

print('Total lenght of string is:', len(s))
print('There is', numbers, 'numbers in string')
print('There is', alpha, 'letters in string')
#print('There is', spaces, 'spaces in string')
#print('There is', others, 'other characters in string')