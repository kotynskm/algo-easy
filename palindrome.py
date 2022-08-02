""" Determine whether a string is a palindrome. """

def isPalindrome(string):
    # reverse string using slice
    reversed = string[::-1]

    if reversed == string:
        return True
    return False

def isPalindrome(string):
    # reverse string using backwards for loop
    reversed = ""
    for i in range(len(string)-1,-1,-1):
        reversed += string[i]
    return reversed == string