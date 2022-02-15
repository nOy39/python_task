"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog"
is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.
"""

import string


def is_pangram(s):
    alphabet = string.ascii_lowercase
    s_set = set("".join(s.split()).lower())
    return alphabet == "".join(f for f in sorted(s_set) if f.isalpha())


pangram = "The quick, brown fox jumps over the lazy dog!"
not_pangram = "The time is it twelve oclock"
print(is_pangram(pangram))
print(is_pangram(not_pangram))
