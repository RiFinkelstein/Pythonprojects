def find_highest_integer(arr):
    """
    Recursively finds the highest integer in a list.

    Args:
    - arr (list): List of integers.

    Returns:
    - int: The highest integer in the list.
    """
    # Base case: If the list has only one element, return it
    if len(arr) == 1:
        return arr[0]

    # Recursive case:
    # Compare the first element with the highest integer in the rest of the list
    # and return the maximum value
    return max(arr[0], find_highest_integer(arr[1:]))

  
# Test the function with a list of integers
my_list = [3, 9, 12, 5, 7, 15, 1, 8]
highest_integer = find_highest_integer(my_list)
print("List:", my_list)
print("Highest Integer:", highest_integer)
