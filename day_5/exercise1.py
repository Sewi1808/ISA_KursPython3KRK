names = ['pawel', 'michal', 'magda', 'ania', 'paulina']

print(len(names))

first_element = names[0]
last_element = names[-1]

print(f"{first_element}\n{last_element}")

#dodawanie elemenu na koniec listy
names.append('sebastian')
print(names)

names_count = names.count('przemek')



print(names)
names.append('przemek')
names.append('ania'),
names_count = names.count('ania')
print(names_count)

name_to_find = 'ania'

foo = names.index(name_to_find)

if name_to_find in names:
    print(name_to_find, "included in: names")
else:
    print("not found")

second_row = names[1:3]
print(second_row)

for name in names:
    print(name)
#
additional_names = ['piotrek', 'kasia']
# names.extend(additional_names)
# print(names)

my_list = names + additional_names
print(my_list)

name_to_remove = 'ania'
my_list.remove(name_to_remove)
print(my_list)

removed_item = my_list.pop()

