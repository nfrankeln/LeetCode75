# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

# solution
# s and t are input strings
def is_isomorphic(s,t):
    conversions={}
    for index,letter in enumerate(s):
        if letter not in conversions:
            if t[index] not in conversions.values():
                conversions[letter]=t[index]
            else:
                return False
        elif letter in conversions:
            if conversions[letter]!=t[index]:
                return False
    return True
