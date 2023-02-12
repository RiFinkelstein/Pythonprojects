letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def unique_english_letters(word):
    count = 0
    for letter in letters:
        if letter in word:
            count += 1
    print(f"there are {count} unique letters")


print(unique_english_letters(input("enter a word: ")))
