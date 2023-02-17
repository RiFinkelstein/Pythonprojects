import sys
number = int(input("enter a number: "))
prime = False
if number > 0:
    for x in range(2, number-1):
        if number % x != 0:
            continue
        elif number % x == 0:
            sys.exit("your number is not prime")
    sys.exit("the number is prime")
if number == 0:
    sys.exit("your numebr is not prime")
else:
    sys.exit("your numebr is not prime")
