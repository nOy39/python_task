arr = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def binary_search(array, item):
    low = 0
    high = len(array)
    while(True):
        if array[high/2] < item:
            high /= 2
    return True


print(binary_search(arr, 7))