# lista z duplikatami

duplicates = [1, 2, 5, 1, 4, 7, 2, 6, 5, 10, 10, 30, 10, 10]
without_duplicates = []

for i in duplicates:
    if i not in without_duplicates:
        without_duplicates.append(i)
print(without_duplicates)