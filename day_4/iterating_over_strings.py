# done: co druga litera wielka


text = str(input("podaj string: \n"))

replaced = ""
replaced = text



a = list(text)
a[2::2] = [x.upper() for x in a[2::2]]

text = ''.join(a)

# for idx, _ in enumerate(replaced):
#     if idx % 2:
#         replaced += text[idx].lower()
#     else:
#         replaced += text[idx].upper()



print(text)