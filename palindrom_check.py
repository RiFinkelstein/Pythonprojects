
word = str(input("enter a word: "))
backwords = word[::-1]

if word == backwords:
    print("your word is a palindrome")
else:
    print("your word is not a palindrom")
