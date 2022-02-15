arr = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def binary_search(array, item):
    mid = len(array) // 2
    current_value = array[mid]
    if item > current_value:
        current_index = binary_search(array[mid:len(array)], item)
    elif item < array[mid]:
        current_index = binary_search(array[0:mid], item)
    else:
        current_index = array[mid]
        return current_index
    return current_index


print(binary_search(arr, 5))
