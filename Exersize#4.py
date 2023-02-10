user_word = input('Enter a word: ')
length_of_word = len(user_word)

print("Printing only even index charachters")
for i in range(0, length_of_word - 1, 2):
    print("index[", i, "]", user_word[i])
