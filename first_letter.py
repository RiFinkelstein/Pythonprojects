sentance = "Hello World"


def get_first_letter(sentance):
    words = sentance.split()
    first_letters = [word[0] for word in words]
    result = ''.join(first_letters)
    return result


print(get_first_letter(sentance))
