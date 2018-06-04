# Create a program that asks the user for a number X
# and then prints out a list of all the divisors of that number.


# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a
# divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Provide number: "))
list_range = list(range(1, num))
divisor_list = []

for number in list_range:
    if num % number == 0:
        divisor_list.append(number)



print("Full list:", list_range)
print("Divisors list:", divisor_list)
