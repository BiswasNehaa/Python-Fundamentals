"""
Write a function that takes a string input and returns 1 or -1 according to these rules:

    Ignore leading and trailing punctuation attached to words (keep internal punctuation like "can't").

    Split the input on whitespace to get words, then remove punctuation from the start and end of each token.

    If the resulting string is empty or contains only one word, return 1.

    Otherwise, for every adjacent pair of words, check whether the last character of the first word is equal (case-sensitive) to the first character of the next word.

    If all adjacent pairs match, return 1; if any pair does not match, return -1.

Examples:

    "" -> 1

    "Hello" -> 1

    "apple eat tea" -> 1 (checks 'e' == 'e', 't' == 't')

    "Hello, oops!" -> 1 (commas and exclamation ignored)

    "abc def" -> -1 ('c' != 'd')

Constraints/Notes (optional):

    Treat None as an empty string only if you want; otherwise assume input is a string.

    The check is case-sensitive by default. Change to case-insensitive by converting characters with .lower() before comparison
"""

import string

def  words_chain_check(s: str):
    
    # If Empty String
    if s is None:
        return 1
    
    tokens=s.split()
    cleaned=[]
    for i in tokens:
        tok_cleaned= i.strip(string.punctuation)
        if tok_cleaned:
            cleaned.append(tok_cleaned)
    
    
    if len(cleaned) <=1:
        return 1
    
    for i in range(len(cleaned)-1):
        if cleaned[i][-1] != cleaned[i+1][0]:
            return -1

    
    return 1