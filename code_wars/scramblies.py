"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters
can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

str1 = 'edewaraaossoqqyt'
str2 = 'codewars'
s1, s2 = 'npfrgpxmbxxxk', 'xnxrpxfgkbpmx'

"""
Сравниваем количество символов входящих символов в строке s1 и s2 если 
в s1 указаный символ встречается реже чем в s2 выходим с False
"""
def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


print(scramble(str1, str2))
#print(scramble(s1, s2))
