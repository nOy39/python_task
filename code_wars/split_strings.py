""" Complete the solution so that it splits the string into pairs of two characters.
    If the string contains an odd number of characters then it should replace
    the missing second character of the final pair with an underscore ('_')."""


def solution(s):
    ls = []
    for i in range(0, len(s), 2):
        ls.append(s[i:i+2]
                  if len(s[i: i + 2]) > 1
                  else s[i: i + 2] + '_')
    return ls


s1 = "asdfadsf"
s2 = "asdfads"
leng = len(s1)
print(solution(s2))
