def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count


print(count_char_x("mississippi", "s"))
