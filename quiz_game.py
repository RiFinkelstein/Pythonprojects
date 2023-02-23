print("welcome to my quiz!")

playing = input("do you want to play? ")
score = 0
if playing != "yes":
    quit()

print("okay! lets play:)")

answer = input("what is my full name? ").lower()
if answer == "rivka finkelstein":
    print('correct!')
    score += 1
else:
    print("incorrect")

answer = input("What month was I born in ").lower()
if answer == "july":
    print('correct!')
    score += 1
else:
    print("incorrect")

answer = input("Where did i grow up? ").lower()
if answer == "woodmere":
    print('correct!')
    score += 1
else:
    print("incorrect")


print(f"you got {score}/3 correct!!")
