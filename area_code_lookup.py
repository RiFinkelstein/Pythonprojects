area_codes = {
    "201": "New Jersey",
    "212": "New York City",
    "215": "Philadelphia",
    "312": "Chicago",
    "323": "Los Angeles",
    # Add more area codes and locations as needed
}

phone_number = input("Enter a phone number: ")
prefix = phone_number[:3]

if prefix in area_codes:
    print(f"The area code {prefix} is for {area_codes[prefix]}.")
else:
    print("Sorry, I don't recognize that area code.")
