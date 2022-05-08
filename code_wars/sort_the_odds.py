def sort_array(source_array):
    a = []
    b = 0
    if source_array:
        a = [i for i in source_array if i % 2 != 0]
        a.sort()
        for i in range(len(source_array)):
            if source_array[i] % 2 != 0:
                source_array[i] = a[b]
                b += 1
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 1, 8, 0]))
print(sort_array([]))
