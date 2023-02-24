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
         percentage_score = (score / 3) * 100
    if percentage_score < 60:
        print(f"Sorry! You got {score}/3 correct ({percentage_score:.2f}%). Better luck next time!")
    elif percentage_score >= 60 and percentage_score < 80:
        print(f"Congratulations! You got {score}/3 correct ({percentage_score:.2f}%). Good job!")
    else:
        print(f"Excellent work! You got {score}/3 correct ({percentage_score:.2f}%). Well done!")


    if score < 2:
        print(f"sorry! you got {score}/3 correct")
    else:
        print(f"you got {score}/3 correct!!")
    play_again = input("Do you want to play again? ")
    if play_again.lower() != "yes":
        break
print("Thanks for playing!")
