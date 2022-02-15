def minimum_sum(values, n):
    """ sum the n smallest integers in the array values (not necessarily ordered) """
    return sum(sorted(values)[:n])


def maximum_sum(values, n):
    return sum(sorted(values, reverse=True)[:n])


values = [5, 3, 4, 1, 2]

print(minimum_sum(values, 2))
print(minimum_sum([], 2))
print(minimum_sum(values, 0))
print(minimum_sum(values, 6))

print(maximum_sum(values, 3))
print(maximum_sum([], 2))
print(maximum_sum(values, 0))
print(maximum_sum(values, 6))
