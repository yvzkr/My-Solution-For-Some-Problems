"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

"""


def first_non_repeating_letter(str1):
    # your code here

    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        elif c.lower() in ctr:
            ctr[c.lower()] += 1
        elif c.upper() in ctr:
            ctr[c.upper()] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return ""

print(first_non_repeating_letter("stress"))