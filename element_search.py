def is_number_in_list(ordered_list, number):
    for i in ordered_list:
        if i == number:
            return True
        elif i > number:
            return False
    return False
