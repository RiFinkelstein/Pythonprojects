def showNumbers(limit):
    for num in range(limit + 1):
        if num % 2 == 0:
            print(num, "EVEN")
        else:
            print(num, "ODD")
showNumbers(3)
