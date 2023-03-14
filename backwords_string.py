def reverse_words(string):
    # Split the string into a list of words
    words = string.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join the reversed list of words back into a string
    reversed_string = " ".join(reversed_words)

    return reversed_string


# Prompt the user to enter a string
user_input = input("Enter a long string containing multiple words: ")

# Call the function and print the result
result = reverse_words(user_input)
print(result)
