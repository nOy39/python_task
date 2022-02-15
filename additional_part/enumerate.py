_str = 'asldkjasdasdaghsdgaisdg'

_enum = enumerate(_str)


def accum(_str):
    return "-".join((v * c).title() for c, v in enumerate(_str))


def square_sum(_number_array):
    return sum(x ** 2 for x in _number_array)

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print(square_sum([5, 7, 3]))
print(accum(_str))

