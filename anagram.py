string_one = "race"
string_two = "care"


def is_anagram(srting_one, string_two):
    # Convert both strings to lowercase and remove whitespace
    srting_one = srting_one.lower().replace(" ", "")
    string_two = string_two.lower().replace(" ", "")

   # Check if the two strings have the same length
    if len(string_one) != len(string_two):
        return False

    # Create a dictionary to count the frequency of each character in str1
    char_count = {}
    for char in string_one:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Iterate over the characters in str2 and decrement their counts in the dictionary
    for char in string_two:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # Check if all the counts in the dictionary are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True


print(is_anagram(string_one, string_two))
