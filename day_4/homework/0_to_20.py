# DONE: program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# DONE: continue

x = range(0,21)
#print(list(x))
y =[]

for i in x:
    if i % 4:
        y.append(i)

print(y)