numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []


def sums_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    total = 0
    for even_number in even_numbers:
        total += even_number

    print(total)


sums_even(numbers)
