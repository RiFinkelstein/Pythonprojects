def Fizz_Buzz(input=input("enter a number: ")):
    if (input % 5 == 0) and input % 3 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(Fizz_Buzz(int(input)))
