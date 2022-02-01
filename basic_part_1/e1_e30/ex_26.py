# Write a Python program to create a histogram from a given list of integers.

char = '@'
hist_format = [2, 3, 6, 5]


def histogram(_ch, _format):
    _hist = ''

    for i in _format:
        _hist = _hist + char * i + '\n'
    return _hist


print(histogram(char, hist_format))
