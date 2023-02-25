print("Welcome to my quiz!")

while True:
    playing = input("Do you want to play? ")
    if playing.lower() != "yes":
        break

    print("Okay! Let's play :)")

    score = 0
    num_questions = 10

    for i in range(num_questions):
        # ask question
        if i == 0:
            question = "What year was the Declaration of Independence signed?"
            answer = "1776"
        elif i == 1:
            question = "Who was the first president of the United States?"
            answer = "George Washington"
        elif i == 2:
            question = 'Which state is known as the "Sunshine State"?'
            answer = "Florida"
        elif i == 3:
            question = "What is the tallest mountain in North America?"
            answer = "Denali"
        elif i == 4:
            question = "What is the capital of California?"
            answer = "Sacramento"
        elif i == 5:
            question = 'Which US state is known as the "Lone Star State"?'
            answer = "Texas"
        elif i == 6:
            question = "Who wrote the Star-Spangled Banner?"
            answer = "Francis Scott Key"
        elif i == 7:
            question = 'Which US city is known as the "Windy City"?'
            answer = "Chicago"
        elif i == 8:
            question = "Who invented the telephone?"
            answer = "Alexander Graham Bell"
        elif i == 9:
            question = "What is the name of the river that flows through the Grand Canyon?"
            answer = "Colorado River"

        print(f"Question {i+1}: {question}")

        # get answer and check if correct
        user_answer = input().strip()
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is {answer}")

    percentage_score = (score / num_questions) * 100

    if percentage_score < 60:
        print(
            f"Sorry! You got {score}/{num_questions} correct ({percentage_score:.2f}%). Better luck next time!")
    elif percentage_score >= 60 and percentage_score < 80:
        print(
            f"Congratulations! You got {score}/{num_questions} correct ({percentage_score:.2f}%). Good job!")
    else:
        print(
            f"Excellent work! You got {score}/{num_questions} correct ({percentage_score:.2f}%). Well done!")

    play_again = input("Do you want to play again? ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
