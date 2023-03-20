birthdays = {
    'alice': 'April 1, 1990',
    'bob': 'July 12, 1995',
    'charlie': 'December 25, 1985'
}

name= input("enter a name: ").lower()
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}")
else:
    print("sorry that name is not in our database")
