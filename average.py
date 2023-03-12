numbers = [1, 6, 9, 19, 5, 3]


def find_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


result_sum = find_sum(numbers)
number_of_elements = (len(numbers))
average = result_sum/number_of_elements
print(f"the average is: {average}")
