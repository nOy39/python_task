"""
Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter.
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""
s1 = 'stress'
s2 = 'should handle empty strings'
s3 = 'sTreSS'


def first_non_repeating_letter(string):
    list_of_char = list(string)
    char = ''
    count = 0
    if len(string) > 0:
        for i in list_of_char:
            print('first cycle:')
            char = i
            for j in range(list_of_char, 1):
                print('second cycle')
                if i == j:
                    count += 1
                if count > 1:
                    char = ''
                    break

                else:
                    print(char)
        return 'more'
    return char


# Python program to print the first non-repeating character
NO_OF_CHARS = 256


# Returns an array of size 256 containing count
# of characters in the passed char array


def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
    return count


# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
    count = getCharCountArray(string)
    char = ''
    index = -1
    k = 0

    for i in string:
        print(count)
        if count[ord(i)] == 1:
            index = k
            char = i
            break
        k += 1

    return index


# Driver program to test above function
string = "geeksforgeeks"
index = firstNonRepeating(s1)
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", s1[index])

# This code is contributed by Bhavya Jain


print(firstNonRepeating(s1))
print(firstNonRepeating(s2))
print(firstNonRepeating(''))
