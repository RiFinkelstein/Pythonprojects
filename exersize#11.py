#Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False
def find_list(lst):
    if lst.count(19) != 2 or lst.count(5) < 3:
        return False
    else:
        return True

# Example usage
list1 = [5, 19, 5, 19, 5, 8]
list2 = [5, 19, 5, 19, 5, 19, 8]
print(find_list(list1))  # Output: False
print(find_list(list2))  # Output: True
