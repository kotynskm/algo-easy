""" Find the first non repeating character in a string. """

def firstNonRepeatingCharacter(string):
    # create dictionary to store character counts
    count_dict = {}

    # loop string and check if char is in the count dict, if not, add it
    # if it is already present, increment the count
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    # loop the keys in the count dict and check if the value is equal to 1,
    # then return the index of that char in the string
    for key in count_dict.keys():
        if count_dict[key] == 1:
            return string.index(key)
    return -1