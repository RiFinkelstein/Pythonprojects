# Function to calculate friendship score
def calculate_friendship_score(name1, name2):
    # Define rules for awarding points
    vowel_points = 1
    friend_points = 2

    # Define vowels and characters in the word "friend"
    vowels = "AEIOUaeiou"
    friend_chars = "FRIENDfriend"

    # Initialize score variables
    score1 = 0
    score2 = 0

    # Loop through characters in name1 and name2
    for char in name1:
        if char in vowels:
            score1 += vowel_points
        if char in friend_chars:
            score1 += friend_points

    for char in name2:
        if char in vowels:
            score2 += vowel_points
        if char in friend_chars:
            score2 += friend_points

    # Calculate total score
    total_score = score1 + score2

    return total_score

# Get names from user input
name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")

# Calculate friendship score
friendship_score = calculate_friendship_score(name1, name2)

# Display personalized message based on score
if friendship_score <= 5:
    print("Not very compatible. Keep working on your friendship!")
elif friendship_score <= 10:
    print("Moderately compatible. There's room for improvement!")
elif friendship_score <= 15:
    print("Very compatible! You make great friends!")
else:
    print("Extremely compatible! You're the best of friends!")
