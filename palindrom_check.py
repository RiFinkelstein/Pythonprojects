
# function to check if string is palindrome or not
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


# main function
s = input("Enter a string: ")

ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")