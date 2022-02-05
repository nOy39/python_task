"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:
"""


def likes(names):
    s = ' like this'
    if names.__len__() > 3:
        s = names([0]) + s
    return s


print(likes(["Alex", "Jacob", "Mark", "Max"]))
print(likes(["Max", "John", "Mark"]))
print(likes([]))
