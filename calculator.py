number_one = int(input("enter a number: "))
number_two = int(input("enter another number: "))
math_application = input(
    "do you want your numbers to be added, subtracted, multiplied or divided? ")
sum = number_one+number_two
difference = number_one-number_two
product = number_one*number_two
quoteint = number_one/number_two

if math_application == "added":
    print(f'{number_one}+{number_two}= {sum}')
elif math_application == "subtracted":
    print(f'{number_one}-{number_two}= {difference}')
elif math_application == "multiplied":
    print(f'{number_one}*{number_two}= {product}')
elif math_application == "divided":
    print(f'{number_one}/{number_two}= {quoteint}')
else:
    print("invalid input")
