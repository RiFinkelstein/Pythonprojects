adjective = input("adjective: ")
number= input("number: ")
adjective1 = input("adjective: ")
ammount = input("ammount: ")
verb = input("verb: ")
measurment = input("measurment: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
noun = input("noun: ")
adjective2 = input("adjective: ")
location= input("location: ")
people = input("group of people: ")

MadLib=f"Recipe for {adjective}: \n \
    {number} of effort \n \
    6TBSP of {adjective1} \n \
    {ammount} of kindness \n \
    A handful of {verb} \n \
    {measurment} of teamwork \n \
    Sprinkling of {verb1} \n \n \
    Instructions: \n \
    {verb2} all the {noun} together and add a {adjective2} heart on {location}. {verb} with {people}"

print(MadLib)