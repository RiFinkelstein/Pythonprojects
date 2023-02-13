def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    print(f"there are {count} {x}'s in the word {word}")

print(count_char_x("mississippi", "s"))
