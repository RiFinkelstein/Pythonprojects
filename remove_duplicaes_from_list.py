list_a = [1, 5, 3, 4, 2, 6]
list_b = [4, 7, 8, 2]
list_c = []

for i in list_a:
    if i not in list_b:
        list_c.append(i)
print(list_c)
