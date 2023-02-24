import time

print("Welcome to my quiz!")

while True:
    playing = input("Do you want to play? ")
    if playing.lower() != "yes":
        break

    print("Okay! Let's play :)")

    score = 0

    # Question 1
    print("Question 1: What year was the Declaration of Independence signed?")
    time.sleep(5)
    answer = input().lower()
    if answer == "1776":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 2
    print("Question 2: Who was the first president of the United States?")
    time.sleep(5)
    answer = input().lower()
    if answer == "george washington":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 3
    print("Question 3: Which state is known as the \"Sunshine State\"?")
    time.sleep(5)
    answer = input().lower()
    if answer == "florida":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 4
    print("Question 4: What is the tallest mountain in North America?")
    time.sleep(5)
    answer = input().lower()
    if answer == "denali" or answer == "mount mckinley":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 5
    print("Question 5: What is the capital of California?")
    time.sleep(5)
    answer = input().lower()
    if answer == "sacramento":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 6
    print("Question 6: Which US state is known as the \"Lone Star State\"?")
    time.sleep(5)
    answer = input().lower()
    if answer == "texas":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 7
    print("Question 7: Who wrote the Star-Spangled Banner?")
    time.sleep(5)
    answer = input().lower()
    if answer == "francis scott key":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 8
    print("Question 8: Which US city is known as the \"Windy City\"?")
    time.sleep(5)
    answer = input().lower()
    if answer == "chicago":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 9
    print("Question 9: Who invented the telephone?")
    time.sleep(5)
    answer = input().lower()
    if answer == "alexander graham bell":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    # Question 10
    print("Question 10: What is the name of the river that flows through the Grand Canyon?")
    time.sleep(5)
    answer = input().lower()
    if answer == "colorado river":
        print('Correct!')
        score += 1
    else:
        print("Incorrect")

    percentage_score = (score / 10) * 100
    if percentage_score < 60:
        print(
            f"Sorry! You got {score}/10 correct ({percentage_score:.2f}%). Better luck next time!")
    elif percentage_score >= 60 and percentage_score < 80:
        print(
            f"Congratulations! You got {score}/10 correct ({percentage_score:.2f}%). Good job!")
    else:
        print(
            f"Excellent work! You got {score}/10 correct ({percentage_score:.2f}%). Well done!")

    play_again = input("Do you want to play again? ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
