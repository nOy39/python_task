_str = 'asldkjasdasdaghsdgaisdg'

_enum = enumerate(_str)
for _count, _value in _enum:
    print(_count, _value)


def accum(str):
    return "-".join((v * c).title() for c, v in enumerate(str))


print(accum(_str))
