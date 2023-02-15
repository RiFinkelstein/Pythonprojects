number = int(input("enter a number: "))

numbers = list(range(1, number+1))

divisors = []

for x in numbers:
    if number % x == 0:
        divisors.append(x)
print(f"{divisors} are the divisors for {number}")
