import datetime
while True:
    # Ask the user to enter their name and age
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    
    # Validate age input
    try:
        age = int(age)
    except ValueError:
        print("Invalid age input. Please enter a valid integer.")
        continue
    
    # Calculate the year they will turn 100
    current_year = datetime.datetime.now().year
    year_when_100 = current_year + (100 - age)

    print(f"Hi {name}! You will turn 100 years old in the year {year_when_100}.")
    
    
    # Ask if the user wants to continue
    answer = input("Do you want to continue? (y/n)")
    if answer.lower() == "n":
        break
