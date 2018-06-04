# done: program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# done: continue

x = range(1,21)
y = []

for i in x:
    if i % 4:
        y.append(i)
#    else:
#        print(y)
print(y)
#print(type(y))
