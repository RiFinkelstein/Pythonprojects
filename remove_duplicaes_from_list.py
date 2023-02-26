list_a = [1, 5, 3, 4, 2, 6, 1, 6]
list_c = []

for i in list_a:
    if i not in list_c:
        list_c.append(i)
print(list_c)
