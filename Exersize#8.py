def count_multi_char(word, x):
    amount_of_splits = word.split(x)
    count = len(amount_of_splits)-1
    print(f"you have {x} in your word, {word}, {count} amount of times")


count_multi_char(word=input("enter a word: "), x=input(
    "enter a group of charachters in your word: "))
