# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:

  #
 ###
#####

wysokosc = input('Podaj wysokosc piramidy Mario: ').lstrip('-+')

#print(type(wysokosc))
wysokosc = int(wysokosc)
#print(type(wysokosc))

print((" " * (wysokosc + 1)) + "#")
for i in range(wysokosc):
     print((" " * (wysokosc - i)) + "#" +("#" * (i + 1))+("#" * (i + 1)))