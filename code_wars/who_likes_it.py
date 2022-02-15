"""
Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
"""


def likes(names):
    case = len(names)
    if case == 0:
        template = 'no one like this'
    elif case == 1:
        template = f'{names[0]} like this'
    elif case == 2:
        template = f'{names[0]} and {names[1]} like this'
    elif case == 3:
        template = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        template = f'{names[0]}, {names[1]} and 2 other like this'
    return template
