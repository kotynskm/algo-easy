""" Return a new string obtained by shifting every letter by k positions, where k is the key. Letters should wrap around the alphabet. """

def caesarCipherEncryptor(string, key):
   # use ord() to determine the unicode
   # use chr() to convert to a letter

    # mod key by 26 letters in the alphabet - edge case for large key values
    key = key % 26
    cipher_string = ""

    for char in string:
        # get unicode for the character in the string
        converted = ord(char)
        # add the key to the unicode number
        cipher_unicode = converted + key
        if cipher_unicode <= 122:
            # use chr() to convert unicode back to a letter
            cipher_string += chr(cipher_unicode)
        else:
            # get the remainder using % and add that to 96
            cipher_string += chr(96 + cipher_unicode % 122)
    return cipher_string