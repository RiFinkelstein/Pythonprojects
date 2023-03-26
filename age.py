import datetime

# Get the user's name
name = input("Please enter your name: ")

# Get the user's birthdate
birthdate = input("Please enter your birthdate (format: MM/DD/YYYY): ")

# Calculate the user's age
today = datetime.date.today()
birthdate_obj = datetime.datetime.strptime(birthdate, "%m/%d/%Y").date()
age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))

# Display the user's age
print(f"{name}, you are {age} years old.")
