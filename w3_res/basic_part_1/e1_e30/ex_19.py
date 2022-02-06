# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def givenString(word):
    if len(word) >=2 and word[:2].lower() != 'is':
        return 'is' + word.replace(word[0], word[0].upper(), 1)
    else:
        return word


print(givenString('empty'))
print(givenString('isBusy'))
