a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = []
odd_list = []

for x in a:
    if x % 2 == 0:
        even_list.append(x)
    if x % 2 != 0:
        odd_list.append(x)
print(f"the origanal list was: {a}")
print(f"here is a list of even numbers: {even_list}")
print(f"here is a list of odd numbers: {odd_list}")
