"""
    Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013).
    Jaden is also known for some of his philosophy that he delivers via Twitter.
    When writing on Twitter, he is known for almost always capitalizing every word.
    For simplicity, you'll have to capitalize each word,
    check out how contractions are expected to be in the example below.

    Your task is to convert strings to how they would be written by Jaden Smith.
    The strings are actual quotes from Jaden Smith, but they are not capitalized
    in the same way he originally typed them.
"""


# def to_jaden_case(s):
#     result = ''
#     ls_count = 0
#
#     for i in s.split(' '):
#         result += (i.capitalize() + ' '
#                    if ls_count < s.split(' ').__len__() - 1
#                    else i.capitalize())
#         ls_count += 1
#     return result

def to_jaden_case(s):
    return " ".join(w.capitalize() for w in s.split(' '))


