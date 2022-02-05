"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""


def accum(s):

    new_ls = []
    mult = 1
    for letter in list(s):
        new_ls.append((letter * mult).capitalize())
        mult += 1
    return "-".join(new_ls)


print(accum('dfghjqwerp'))
