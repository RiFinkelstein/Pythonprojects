print("welcome to my quiz!")

while True:
    playing = input("do you want to play? ")
    if playing.lower() != "yes":
        break

    print("okay! let's play :)")

    score = 0
    answer = input("what is my full name? ").lower()
    if answer == "rivka finkelstein":
        print('correct!')
        score += 1
    else:
        print("incorrect")

    answer = input("What month was I born in? ").lower()
    if answer == "july":
        print('correct!')
        score += 1
    else:
        print("incorrect")

    answer = input("Where did I grow up? ").lower()
    if answer == "woodmere":
        print('correct!')
        score += 1
    else:
        print("incorrect")

    if score < 2:
        print(f"sorry! you got {score}/3 correct")
    else:
        print(f"you got {score}/3 correct!!")
    play_again = input("Do you want to play again? ")
    if play_again.lower() != "yes":
        break
print("Thanks for playing!")
