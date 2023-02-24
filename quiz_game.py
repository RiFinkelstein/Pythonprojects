print("welcome to my quiz!")

while True:
    playing = input("do you want to play? ")
    if playing.lower() != "yes":
        break

    print("okay! let's play :)")

    score = 0
    answer = input(
        "What year was the Declaration of Independence signed? ").lower()
    if answer == "1776":
        print('correct!')
        score += 1
    else:
        print("incorrect")

    answer = input(
        "Who was the first president of the United States? ").lower()
    if answer == "George Washington".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")

    answer = input("Which state is known as the \"Sunshine State\"? ").lower()
    if answer == "Florida".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")

    answer = input("What is the tallest mountain in North America? ").lower()
    if answer == "Denali".lower() or "Mount McKinley".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")
    answer = input("What is the capital of California? ").lower()
    if answer == "Sacramento".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")
    answer = input(
        "Which US state is known as the \"Lone Star State\"? ").lower()
    if answer == "Texas".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")
    answer = input("Who wrote the Star-Spangled Banner? ").lower()
    if answer == "Francis Scott Key".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")
        answer = input(
            "Which US city is known as the \"Windy City\"? ").lower()
    if answer == "Chicago".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")
        answer = input("Who invented the telephone? ").lower()
    if answer == "Alexander Graham Bell".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")
        answer = input(
            "What is the name of the river that flows through the Grand Canyon? ").lower()
    if answer == "Colorado River".lower():
        print('correct!')
        score += 1
    else:
        print("incorrect")

    percentage_score = (score / 3) * 100
    if percentage_score < 60:
        print(
            f"Sorry! You got {score}/3 correct ({percentage_score:.2f}%). Better luck next time!")
    elif percentage_score >= 60 and percentage_score < 80:
        print(
            f"Congratulations! You got {score}/3 correct ({percentage_score:.2f}%). Good job!")
    else:
        print(
            f"Excellent work! You got {score}/3 correct ({percentage_score:.2f}%). Well done!")

    play_again = input("Do you want to play again? ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
